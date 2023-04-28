import datetime
import colorama
from colorama import Fore, Style as ColorStyle
from prompt_toolkit import PromptSession
from prompt_toolkit.application import get_app
from prompt_toolkit.formatted_text import (
    HTML,
    fragment_list_width,
    merge_formatted_text,
    to_formatted_text,
)
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import set_title, clear
from app.cli.data import Data
from app.cli.completer import TerminalCompleter


colorama.init()
session = PromptSession()

data = Data({
    'headers': '',
    'query': '?hostname',
    'body': '',
    'http_method': 'GET'
})

style = Style.from_dict(
    {
        "username": "#aaaaaa",
        "path": "#1294ff bold",
        "branch": "#5fd700 bold bg:#1c1c1c",
        "env": "bg:#1c1c1c",
        "left-part": "bg:#1c1c1c",
        "right-part": "bg:#1c1c1c",
        "time": "#5f8787",
        "cursor": "ansibrightred blink",
    }
)


def get_prompt() -> HTML:
    """
    Build the prompt dynamically every time its rendered.
    """
    left_part = HTML(
        "╭─"
        "<left-part>"
        " <username></username>   "
        "<path>/home/apexagente</path>"
        "  on "
        "<branch>   main  </branch>"
        "</left-part>"
    )
    right_part = HTML(
        "<right-part> "
        " <env> python </env> "
        "at"
        " <time>%s  </time>"
        "</right-part>"
    ) % (datetime.datetime.now().strftime("%H:%M:%S"),)

    used_width = sum(
        [
            fragment_list_width(to_formatted_text(left_part)),
            fragment_list_width(to_formatted_text(right_part)),
        ]
    )

    total_width = get_app().output.get_size().columns
    padding_size = total_width - used_width

    padding = HTML("<padding>%s</padding>") % (" " * padding_size,)

    return merge_formatted_text([left_part, padding, right_part, "\n", "╰─ "])


def help_command():
    print(Fore.GREEN + "Available commands:")
    print(" - help: Display this help message")
    print(" - all: Get all data")
    print(" - get: Get a data from host name")
    print(ColorStyle.RESET_ALL)


def clear_command():
    clear()


def all_command():
    global data
    data.get_all_data()


def get_command(host):
    global data
    data.check_if_data_exists(host)


commands = {
    "help": help_command,
    "clear": clear_command,
    "all": all_command,
    "get": get_command
}


try:
    clear()
    set_title("Simple-ApexAgente")
    while True:
        # Prompt user for command input using prompt-toolkit
        command_input = session.prompt(get_prompt, style=style,
                                       refresh_interval=1,
                                       completer=TerminalCompleter(),
                                       complete_while_typing=True,
                                       complete_in_thread=True)
        # Look up and execute the corresponding command function
        command_input_split = command_input.split()
        try:
            if command_input_split[0] in commands:
                if len(command_input_split) == 1:
                    commands[command_input_split[0]]()
                elif len(command_input_split) == 2 and command_input_split[0] == 'get':
                    commands[command_input_split[0]](command_input_split[1])
                else:
                    raise ValueError
            else:
                raise KeyError
        except (KeyError, ValueError):
            error_msg = "Invalid command. Type 'help' for a list of available commands."
            print(f"{Fore.RED}{error_msg}{Fore.RESET}")
except KeyboardInterrupt:
    print(f"{Fore.RED} ❯")
