#!/usr/bin/python3

import sys
import pyperclip
import os
from colorama import init, Fore, Back, Style

# Initialize Colorama
init()

def copy_file_to_clipboard(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            pyperclip.copy(content)
            print(f"{Fore.GREEN}[ + ] File Content Copied!!!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error while copying file content: {e}{Style.RESET_ALL}")

def copy_stdin_to_clipboard():
    try:
        content = sys.stdin.read()
        pyperclip.copy(content)
        print(f"{Fore.GREEN}[ + ] Command Output Copied!!!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error while copying stdin content: {e}{Style.RESET_ALL}")

if __name__ == '__main__':
    if len(sys.argv) == 1:  # No arguments, expect input from stdin
        if sys.stdin.isatty():
            print(f"{Back.WHITE}{Fore.RED}{Style.BRIGHT}[*] Usage: copy <filename> or use a pipe: command | copy{Style.RESET_ALL}")
            sys.exit(1)
        else:
            copy_stdin_to_clipboard()
    elif len(sys.argv) == 2:  # Single argument, treat it as a filename
        filename = sys.argv[1]
        pwd = os.getcwd()
        filename = os.path.join(pwd, filename)
        if os.path.exists(filename):
            copy_file_to_clipboard(filename)
        else:
            print(f"{Back.WHITE}{Fore.RED}{Style.BRIGHT}[-] No Such File or Directory FOUND!!!{Style.RESET_ALL}")
    else:
        print(f"{Back.WHITE}{Fore.RED}{Style.BRIGHT}[*] Usage: copy <filename> or use a pipe: command | copy{Style.RESET_ALL}")
        sys.exit(1)
