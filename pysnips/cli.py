# pysnips/cli.py

import argparse
import sys
from .registry import SNIPPETS
from .generator import TemplateEngine
from .utils.console import Console
from .utils.export import install_vscode, to_vscode_snippets
import json

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
    
    print(f"\nUsage:")
    print(f"  pysnips <command> [--placeholder value]")
    print(f"  pysnips install --vscode")
    print(f"  pysnips export --vscode")

def run_install(args):
    if args.vscode:
        Console.print_msg("Installing snippets for VS Code...", Console.BLUE)
        success, msg = install_vscode()
        if success:
            Console.print_msg(f"Success! Snippets installed at: {msg}", Console.GREEN)
            Console.print_msg("Restart VS Code or use 'Developer: Reload Window' to activate.", Console.YELLOW)
        else:
            Console.print_msg(f"Error: {msg}", Console.RED)
    else:
        Console.print_msg("Error: Specify an editor to install (e.g., --vscode)", Console.RED)

def run_export(args):
    if args.vscode:
        snippets = to_vscode_snippets()
        print(json.dumps(snippets, indent=4))
    else:
        Console.print_msg("Error: Specify a format to export (e.g., --vscode)", Console.RED)

def main():
    parser = argparse.ArgumentParser(
        prog="pysnips",
        description="Production-quality code templates for Python developers.",
        add_help=False
    )
    parser.add_argument("command", nargs="?", help="The snippet command to run (or 'list', 'install', 'export')")
    parser.add_argument("-h", "--help", action="store_true", help="Show help message")
    parser.add_argument("--vscode", action="store_true", help="Target VS Code")

    args, unknown = parser.parse_known_args()

    if args.help:
        parser.print_help()
        print("\nCommands:")
        print("  list \t\t Show all 50 commands")
        print("  install --vscode \t Install snippets into VS Code")
        print("  export --vscode \t Print snippets in VS Code format")
        print("  <cmd> \t\t Print snippet for specific command")
        sys.exit(0)

    if not args.command or args.command == "list":
        run_list()
    elif args.command == "install":
        run_install(args)
    elif args.command == "export":
        run_export(args)
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
