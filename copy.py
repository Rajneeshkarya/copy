#!/usr/bin/python3

import sys
import pyperclip
import os
from colorama import init, Fore, Back, Style

def copy_file_to_clipboard(filename):
	try:
		with open(filename, 'r') as file:
			content = file.read()
			pyperclip.copy(content)
			print(f"{Fore.GREEN}[ + ]File Content Copied!!!{Style.RESET_ALL}")
	except Exception as e:
		print(f"{Fore.RED}[-] Error while Copying content!!!{Style.RESET_ALL}")


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print(f"{Back.WHITE}{Fore.RED}{Style.BRIGHT}[*] Usage: copy <filename>{Style.RESET_ALL}")
		sys.exit(1)

	filename = sys.argv[1]
	pwd = os.getcwd()
	filename = pwd+'/'+filename
	if os.path.exists(filename):
		copy_file_to_clipboard(filename)
	else:
		print(f"{Back.WHITE}{Fore.RED}{Style.BRIGHT}[-] No Such File or Directory FOUND!!!{Style.RESET_ALL}")	
