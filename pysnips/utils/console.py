# pysnips/utils/console.py

import sys

class Console:
    """
    Simple utility for ANSI colored console output.
    """
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

    @staticmethod
    def print_msg(msg: str, color: str = ""):
        print(f"{color}{msg}{Console.END}")

    @staticmethod
    def print_header(text: str):
        print(f"\n{Console.BOLD}{Console.BLUE}{text.upper()}{Console.END}")
        print(f"{Console.BLUE}{'=' * len(text)}{Console.END}")

    @staticmethod
    def print_item(cmd: str, desc: str):
        print(f"{Console.GREEN}{cmd.ljust(15)}{Console.END} | {desc}")
