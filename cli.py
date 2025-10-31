import sys
import time
import random
import threading
from core.auth_controller import AuthController
from core.core import (
    get_paragraphs_from_db,
    compute_results,
    save_results_to_db,
    get_user_progress
)
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from rich.table import Table

from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.application import get_app 

# TODO: split this whole loong file.
# my coral colours
lavender = "#858cff"
blue ="#2de3ff"
cyan = "#00f4e4"
green = "#00f282"
pink = "#ff9dca"

console = Console()

auth_controller =AuthController()

# This whole banner thing is probably too much, maybe remove later
typerush_banner = r"""
 _____                     ____               _     
|_   _|_   _  _ __    ___ |  _ \  _   _  ___ | |__  
  | | | | | || '_ \  / _ \| |_) || | | |/ __|| '_ \ 
  | | | |_| || |_) ||  __/|  _ < | |_| |\__ \| | | |
  |_|  \__, || .__/  \___||_| \_\ \__,_||___/|_| |_|
       |___/ |_|                                    
"""


def show_banner():
    console.print(Align.center(Text(typerush_banner, style=f"bold {blue}")))


def show_main_menu():
    menu_text = "\n".join([
        "[1] Register",
        "[2] Login",
        "[q] Quit"
    ])
    panel = Panel(
        Align.center(menu_text),
        title =f"[bold {cyan}]Main Menu[/bold {cyan}]",
        border_style=cyan,
        padding= (1, 6)
    )
    console.print(Align.center(panel))


def input_screen(title: str, error: str = ""):
    console.print(Align.center(f"[bold {lavender}]{title}[/bold {lavender}] (type 'q' to go back)\n"))
    if error:
        console.print(Align.center(f"[bold {pink}]{error}[/bold {pink}]\n"))


def show_home_screen(username: str):
    while True:
        console.clear()
        show_banner()
        console.print(Align.center(f"\n[bold {lavender}]Home[/bold {lavender}]\n"))
        console.print(Align.center(f"Welcome, [bold {green}]{username}[/bold {green}]!\n"))

        menu_text = "\n".join([
            "[1] Start Test",
            "[2] View Progress",
            "[q] Logout"
        ])
        console.print(Align.center(Panel(menu_text, title=f"[bold {cyan}]{username}'s Menu[/bold {cyan}]", padding=(1, 6))))

        choice = console.input(f"[bold {blue}]\nEnter choice [1/2/Q]: [/bold {blue}]").strip().lower()

        if choice == '1':
            start_test(username)
        elif choice == '2':
            view_progress(username)
        elif choice == 'q':
            return


def start_test(username):
    console.clear()
    show_banner()
    console.print(Align.center(f"[bold {green}]Starting test...[/bold {green}]\n"))

    while True:
        duration = console.input(f"[bold {lavender}]Enter test duration in seconds (type 'q' to cancel): [/bold {lavender}]").strip()
        if duration.lower() =='q':
            return
        if duration.isdigit() and int(duration) > 0:
            duration = int(duration)
            break
        else:
            console.print(Align.center(f"[bold {pink}]Please enter a valid positive integer.[/bold {pink}]"))

    console.print(Align.center(f"[bold {lavender}]Timer starts when you begin typing...[/bold {lavender}]\n"))
    cli_typing_game(username, duration)
    console.input("\nPress Enter to return to home menu...")


def view_progress(username):
    console.clear()
    show_banner()
    results_df = get_user_progress(username)

    table = Table(title=f"{username}'s Typing Test Progress", show_lines=True)
    table.add_column("Date", justify="center", style=lavender)
    table.add_column("WPM", justify="center", style=green)
    table.add_column("Accuracy (%)", justify="center", style=cyan)

    if results_df.empty:
        console.print(Align.center(f"[bold {pink}]No progress found for {username}.[/bold {pink}]"))
    else:
        for _, res in results_df.iterrows():
            table.add_row(
                str(res.get('date', 'N/A')),
                f"{res.get('wpm', 0):.2f}",
                f"{res.get('accuracy', 0):.2f}"
            )
        console.print(Align.center(table))

    console.input("\nPress Enter to return to home menu...")


def main():
    while True:
        console.clear()
        show_banner()
        show_main_menu()
        choice = console.input(f"[bold {blue}]\nEnter choice [1/2/Q]: [/bold {blue}]").strip().lower()

        if choice == '1':
            _handle_auth("Register", auth_controller.register)
        elif choice == '2':
            _handle_auth("Login", auth_controller.login)
        elif choice.upper() =='Q':
            console.clear()
            console.print(Align.center(Text("Goodbye!", style=f"bold {green}")))
            sys.exit()

def _handle_auth(title: str, auth_function):
    error = ""
    while True:
        console.clear()
        show_banner()
        input_screen(title, error)
        username = console.input("[bold lavender]Username: [/bold lavender]").strip()
        if username.lower() =='q':
            return
        password = console.input("[bold lavender]Password: [/bold lavender]", password=True).strip()
        if password.lower() =='q':
            return

        if not username or not password:
            error = "Username and password cannot be empty."
            continue

        success, msg = auth_function(username, password)
        if success:
            show_home_screen(username)
            break
        else:
            error = msg


def cli_typing_game(user_id, duration=12):
    paragraphs = get_paragraphs_from_db()
    if not paragraphs:
        console.print("[red]No paragraphs available for typing test.[/red]")
        return

    total_typed_text = ""
    all_paragraphs_shown = []
    remaining_paragraphs = paragraphs.copy()

    time_left = duration
    game_over = False
    start_time = None

    current_paragraph = random.choice(remaining_paragraphs)
    all_paragraphs_shown.append(current_paragraph)
    remaining_paragraphs.remove(current_paragraph)

    # timer thread
    def timer_thread():
        nonlocal time_left, game_over, start_time
        while start_time is None and not game_over:
            time.sleep(0.1)
        while time_left > 0 and not game_over:
            time.sleep(1)
            time_left -= 1
        game_over = True

    timer = threading.Thread(target=timer_thread, daemon=True)
    timer.start()

    session = PromptSession()

    def bottom_toolbar():
        nonlocal game_over, start_time, total_typed_text
        try:
            app = get_app()
            current_text = app.current_buffer.text

            # start timer on first keystroke
            if start_time is None and current_text:
                start_time = time.time()

            # timer expired
            if time_left <= 0:
                if current_text.strip():
                    total_typed_text += current_text.strip() + " "
                game_over = True
                app.exit()
                return HTML("<b><style fg='red'>Time's up!</style></b>")

            if start_time is None:
                return HTML(f"<b><style fg='{lavender}'>Time: {time_left}s. Start typing to begin!</style></b>")
            return HTML(f"<b><style fg='{blue}'>Time left: {time_left}s</style></b>")
        except Exception:
            return ""

    console.print(Align.center(Panel(current_paragraph, title="[bold green]Type the following[/bold green]", border_style="green")))
    
    current_input = ""

    
    while not game_over:
        try:
            user_input = session.prompt("> ", bottom_toolbar=bottom_toolbar, refresh_interval=0.2)

            if user_input is None or game_over:
                break

            if user_input.lower() in ("q", "quit"):
                game_over = True
                break

            if user_input.strip() or current_input:
                current_input += user_input.strip() + " "
                    #neww sentence, not paragraph infact TODO refactor paragraph -> sentence
                if len(current_input.strip()) >= len(current_paragraph.strip()) or user_input.strip() == "":
                    total_typed_text += current_input.strip() + " " 
                    current_input =""
                    if not remaining_paragraphs:
                        remaining_paragraphs = [p for p in paragraphs if p not in all_paragraphs_shown]
                    if remaining_paragraphs:
                        current_paragraph = random.choice(remaining_paragraphs)
                        all_paragraphs_shown.append(current_paragraph)
                        remaining_paragraphs.remove(current_paragraph)

                        console.print("\n") 
                        console.print(
                            Align.center(
                                Panel(
                                    current_paragraph,
                                    title="[bold green]Type the following[/bold green]",
                                    border_style="green"
                                )
                            )
                        )

        except (EOFError, KeyboardInterrupt):
            game_over = True
            break

    game_over = True
    timer.join(timeout=0.5)

    if start_time is None:
        console.print("\n[bold red]Test cancelled.[/bold red]")
        return

    elapsed_time = max(time.time() - start_time, 1)
    accuracy, wpm, total_chars = compute_results(total_typed_text, all_paragraphs_shown, elapsed_time)
    save_results_to_db(user_id, accuracy, wpm, total_chars)

    console.print("\n[bold green]Test Completed![/bold green]")
    console.print(f"Accuracy: [bold cyan]{accuracy:.2f}%[/bold cyan]")
    console.print(f"WPM: [bold cyan]{wpm:.2f}[/bold cyan]")
    console.print(f"Total Characters: [bold cyan]{total_chars}[/bold cyan]")

if __name__ == "__main__":
    main()