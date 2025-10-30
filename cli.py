#cli.py 
import sys
from core.auth_controller import AuthController
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.align import Align

# my coral colors
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
        "[Q] Quit"
    ])
    panel = Panel(
        Align.center(menu_text),
        title= f"[bold {cyan}]Main Menu[/bold {cyan}]",
        border_style=cyan,
        padding = (1,6)
    )
    console.print(Align.center(panel))



def input_screen(title: str, error: str = ""):
    console.print(Align.center(f"[bold {lavender}]{title}[/bold {lavender}] (press 'Q' to go back)\n"))
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
            "[Q] Logout"
        ])
        console.print(Align.center(Panel(menu_text, title=f"[bold {cyan}]{username}'s Menu[/bold {cyan}]", padding=(1,6))))

        choice = console.input(f"[bold {blue}]\nEnter choice [1/2/Q]: [/bold {blue}]").strip().lower()

        if choice == '1':
            console.clear()
            show_banner()
            console.print(Align.center(f"[bold {green}]Starting test...[/bold {green}]\n"))
            input("Press Enter to return to home menu...") #TODO connect to test starting
        elif choice == '2':
            console.clear()
            show_banner()
            console.print(Align.center(f"[bold {cyan}]Viewing progress...[/bold {cyan}]\n"))
            input("Press Enter to return to home menu...") #TODO connect to progress viewing
        elif choice == 'q':
            break


def main():
    while True:
        console.clear()
        show_banner()
        show_main_menu()

        choice = console.input(f"[bold {blue}]\nEnter choice [1/2/Q]: [/bold {blue}]").strip().lower()

        if choice == '1': #register
            error = ""
            while True:
                console.clear()
                show_banner()
                input_screen("Register", error)
                username = input("Username: ").strip()
                if username.lower() == 'q':
                    break
                password = input("Password: ").strip()
                if password.lower() == 'q':
                    break
                success, msg = auth_controller.register(username, password) 
                if success:
                    console.clear()
                    show_banner()
                    show_home_screen(username)
                    break
                else:
                    error = msg

        elif choice == '2':
            error = ""
            while True:
                console.clear()
                show_banner()
                input_screen("Login", error)
                username = input("Username: ").strip()
                if username.lower() == 'q':
                    break
                password = input("Password: ").strip()
                if password.lower() == 'q':
                    break
                success, msg = auth_controller.login(username, password)
                if success:
                    console.clear()
                    show_banner()
                    show_home_screen(username)
                    break
                else:
                    error = msg

        elif choice == 'q':
            console.clear()
            console.print(Align.center(Text("Quitting!", style=f"bold {green}")))
            sys.exit()

if __name__ == "__main__":
    main()
