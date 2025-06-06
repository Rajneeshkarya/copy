#!/usr/bin/python3

import sys
import pyperclip
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from colorama import init, Fore, Back, Style


HISTORY_DIR = os.path.join(os.getcwd(),"history")

# Initialize Colorama
init()

def save_to_history(content):
	print(HISTORY_DIR)
	os.makedirs(HISTORY_DIR,exist_ok=True)
	try:
		load_dotenv()
		last_time = os.getenv("DATE")
		print(last_time)
		last_time = datetime.strptime(str(last_time), "%Y-%m-%d %H:%M:%S")
		print(last_time)
		timestamp = datetime.now()
		print(timestamp)
		if timestamp - last_time > timedelta(hours=1):
			history_file = os.path.join(HISTORY_DIR, f"clipboard_{timestamp.strftime("%Y_%m_%d_%H_0")}")
			with open(history_file,'w') as file:
				file.write(f'{timestamp.strftime("%H:%M:%S : ")}')
				file.write(content)
				file.write('\n')
			
		else:
			history_file = os.path.join(HISTORY_DIR, f"clipboard_{timestamp.strftime("%Y_%m_%d_%H_0")}")
			with open(history_file,'a') as file:
				file.write(f'{timestamp.strftime("%H:%M:%S : ")}')
				file.write(content)
				file.write('\n')
			last_time = timestamp

	except Exception as e:
		print(f"{Fore.RED}[-] Error in saving history {e}{Style.RESET_ALL}")



def copy_file_to_clipboard(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            pyperclip.copy(content)
            save_to_history(content)
            print(f"{Fore.GREEN}[ + ] File Content Copied!!!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error while copying file content: {e}{Style.RESET_ALL}")

def copy_stdin_to_clipboard():
    try:
        content = sys.stdin.read()
        pyperclip.copy(content)
        save_to_history(content)
        print(f"{Fore.GREEN}[ + ] Command Output Copied!!!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error while copying stdin content: {e}{Style.RESET_ALL}")

if __name__ == '__main__':
    if len(sys.argv) == 1: 
        if sys.stdin.isatty():
            print(f"{Back.WHITE}{Fore.RED}{Style.BRIGHT}[*] Usage: copy <filename> or use a pipe: command | copy{Style.RESET_ALL}")
            sys.exit(1)
        else:
            copy_stdin_to_clipboard()
    elif len(sys.argv) == 2:
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
