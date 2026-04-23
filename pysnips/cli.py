# pysnips/cli.py

import argparse
import sys
from .registry import SNIPPETS
from .generator import TemplateEngine
from .utils.console import Console

def parse_placeholders(unknown_args):
    """
    Converts list of ['--key', 'value'] to {key: value}.
    """
    placeholders = {}
    i = 0
    while i < len(unknown_args):
        arg = unknown_args[i]
        if arg.startswith("--"):
            key = arg[2:]
            if i + 1 < len(unknown_args) and not unknown_args[i+1].startswith("--"):
                placeholders[key] = unknown_args[i+1]
                i += 2
            else:
                placeholders[key] = "" # Boolean or empty flag
                i += 1
        else:
            i += 1
    return placeholders

def run_list():
    Console.print_header("pysnips commands")
    
    # Sort by category and then by command
    categories = {}
    for cmd, info in SNIPPETS.items():
        cat = info["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((cmd, info["description"]))

    for cat, items in categories.items():
        print(f"\n{Console.YELLOW}[ {cat} ]{Console.END}")
        for cmd, desc in sorted(items):
            Console.print_item(cmd, desc)
    
    print(f"\nUsage: pysnips <command> [--placeholder value]")

def main():
    parser = argparse.ArgumentParser(
        prog="pysnips",
        description="Production-quality code templates for Python developers.",
        add_help=False
    )
    parser.add_argument("command", nargs="?", help="The snippet command to run (or 'list')")
    parser.add_argument("-h", "--help", action="store_true", help="Show help message")

    args, unknown = parser.parse_known_args()

    if args.help:
        parser.print_help()
        print("\nCommands:")
        print("  list \t Show all 50 commands")
        print("  <cmd> \t Print snippet for specific command")
        sys.exit(0)

    if not args.command or args.command == "list":
        run_list()
    elif args.command in SNIPPETS:
        placeholders = parse_placeholders(unknown)
        try:
            rendered = TemplateEngine.render(args.command, **placeholders)
            print(rendered)
        except Exception as e:
            Console.print_msg(f"Error: {e}", Console.RED)
    else:
        Console.print_msg(f"Error: Unknown command '{args.command}'. Run 'pysnips list' for options.", Console.RED)
        sys.exit(1)

if __name__ == "__main__":
    main()
