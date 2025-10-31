import sys
import time
import random
import difflib
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
from rich.live import Live
from rich.layout import Layout

from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit.formatted_text import HTML



# my coral colours
lavender = "#858cff"
blue = "#2de3ff"
cyan = "#00f4e4"
green = "#00f282"
pink = "#ff9dca"

console = Console()
auth_controller = AuthController()


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
        title=f"[bold {cyan}]Main Menu[/bold {cyan}]",
        border_style=cyan,
        padding=(1, 6)
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

        choice = console.input(f"[bold {blue}]\nEnter choice [1/2/q]: [/bold {blue}]").strip().lower()

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
        if duration.lower() == 'q':
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
    results_list = get_user_progress(username)

    table = Table(title=f"{username}'s Typing Test Progress", show_lines=True)
    table.add_column("Date", justify="center", style=lavender)
    table.add_column("WPM", justify="center", style=green)
    table.add_column("Accuracy (%)", justify="center", style=cyan)

    if hasattr(results_list, "empty") and not results_list.empty:
        for _, row in results_list.iterrows():
            table.add_row(
                str(row.get('date', 'N/A')),
                f"{row.get('wpm', 0):.2f}",
                f"{row.get('accuracy', 0):.2f}"
            )
    else:
        for res in results_list:
            table.add_row(
                str(res.get('date', 'N/A')),
                f"{res.get('wpm', 0):.2f}",
                f"{res.get('accuracy', 0):.2f}"
            )

    console.print(table)
    console.input("Press Enter to return to home menu...")


def main():
    while True:
        console.clear()
        show_banner()
        show_main_menu()
        choice = console.input(f"[bold {blue}]\nEnter choice [1/2/q]: [/bold {blue}]").strip().lower()

        if choice == '1':
            handle_register()
        elif choice == '2':
            handle_login()
        elif choice == 'q':
            console.clear()
            console.print(Align.center(Text("Goodbye!", style=f"bold {green}")))
            sys.exit()


def handle_register():
    error = ""
    while True:
        console.clear()
        show_banner()
        input_screen("Register", error)
        username = console.input("[bold lavender]Username: [/bold lavender]").strip()
        if username.lower() == 'q':
            return
        password = console.input("[bold lavender]Password: [/bold lavender]", password=True).strip()
        if password.lower() == 'q':
            return
        if not username or not password:
            error = "Username and password cannot be empty."
            continue
        success, msg = auth_controller.register(username, password)
        if success:
            show_home_screen(username)
            break
        else:
            error = msg


def handle_login():
    error = ""
    while True:
        console.clear()
        show_banner()
        input_screen("Login", error)
        username = console.input("[bold lavender]Username: [/bold lavender]").strip()
        if username.lower() == 'q':
            return
        password = console.input("[bold lavender]Password: [/bold lavender]", password=True).strip()
        if password.lower() == 'q':
            return
        if not username or not password:
            error = "Username and password cannot be empty."
            continue
        success, msg = auth_controller.login(username, password)
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

    time_left = duration
    game_over = False

    remaining_paragraphs = paragraphs.copy()
    current_paragraph = random.choice(remaining_paragraphs)
    all_paragraphs_shown.append(current_paragraph)
    remaining_paragraphs.remove(current_paragraph)

    typed_line = ""

    # timer thread
    def timer_thread():
        nonlocal time_left, game_over
        while time_left > 0:
            time.sleep(1)
            time_left -= 1
        game_over = True

    threading.Thread(target=timer_thread, daemon=True).start()

    session = PromptSession()

    def bottom_toolbar():
        return HTML(f"<b><style fg='blue'>Time left: {time_left}s</style></b>")

    console.print(Panel(current_paragraph, title="[bold green]Type the following[/bold green]", border_style="green"))

    with patch_stdout():
        while not game_over:
            try:
                user_input = session.prompt("> ", bottom_toolbar=bottom_toolbar)
            except (EOFError, KeyboardInterrupt):
                break

            if user_input.lower() in ("q", "quit"):
                break

            typed_line += user_input.strip() + " "

            # move to next paragraph if done!
            if len(typed_line.strip()) >= len(current_paragraph.strip()):
                total_typed_text += typed_line.strip() + " "
                typed_line = ""
                if not remaining_paragraphs:
                    remaining_paragraphs = paragraphs.copy()
                current_paragraph = random.choice(remaining_paragraphs)
                all_paragraphs_shown.append(current_paragraph)
                remaining_paragraphs.remove(current_paragraph)
                console.print(Panel(current_paragraph, title="[bold green]Type the following[/bold green]", border_style="green"))

    # compute results
    elapsed_time = max(duration - time_left, 1)
    accuracy, wpm, total_chars = compute_results(total_typed_text, all_paragraphs_shown, elapsed_time)
    save_results_to_db(user_id, accuracy, wpm, total_chars)

    console.print("\n[bold green]Test Completed![/bold green]")
    console.print(f"Accuracy: [bold cyan]{accuracy:.2f}%[/bold cyan]")
    console.print(f"WPM: [bold cyan]{wpm:.2f}[/bold cyan]")
    console.print(f"Total Characters: [bold cyan]{total_chars}[/bold cyan]")


if __name__ == "__main__":
    main()
