import os
import sys
import subprocess
import yaml
from colorama import init, Fore, Back, Style


BINARY_FILE = '/usr/local/bin/copy'
CONFIG_PATH = os.path.expanduser('~/.config/copy')
CONFIG_FILE = os.path.expanduser('~/.config/copy/config.yml')
CONFIG = {
	'date': '2024-01-27 18:06:00',
	'hist_path': f'{os.path.join(os.getcwd(),"history")}'
}

# Binary File 

def configBinary():
	if not os.path.isfile(BINARY_FILE):
		command = ["sudo", "ln", "-s", os.path.join(os.getcwd(),"copy.py"), BINARY_FILE]
		try:
			result = subprocess.run(command, text=True,capture_output=True)

			if result.returncode == 0:
				print(f"{Fore.GREEN}[+] Binary Created!!!\n{Style.RESET_ALL}")
			else:
				print(f"{Fore.RED}[-] Error while creating copy binary!!!{Style.RESET_ALL}")

		except Exception as e:
			print(f"{Fore.RED}[-] Erros : {e}{Style.RESET_ALL}")

# Configuration file

def configurationFiles():
	if not os.path.exists(CONFIG_PATH):
			os.makedirs(CONFIG_PATH)

	if not os.path.isfile(CONFIG_FILE):
		with open(CONFIG_FILE,"w") as file:
			yaml.dump(CONFIG, file, default_flow_style=False)
			print(f"{Fore.GREEN}[+] Configurations Initiated!!!\n{Style.RESET_ALL}")


# Installing Requirements

def installDependencies():
	print(f"{Fore.GREEN}[+] Installing Dependencies!!!\n{Style.RESET_ALL}")
	command = ["pip","install","-r","requirements.txt"]
	try:
			result = subprocess.run(command, text=True,capture_output=True)

			if result.returncode == 0:
				print(f"{Fore.GREEN}[+] Dependencies Installed!!!\n{Style.RESET_ALL}")
			else:
				print(f"{Fore.RED}[-] Error while Installing Dependencies!!! \n\n Create a VENV first using \n $ python3 -m venv env\n $ source env/bin/activate \n\n or install it manually \n $ pip install -r requirements.txt\n{Style.RESET_ALL}")
	except Exception as e:
		print(f"{Fore.RED}[-] Erros : {e}{Style.RESET_ALL}")



if __name__ == '__main__':
	try:	

		# Installing Dependencies

		installDependencies()

		# Binary File
		configBinary()

		# Configuration file
		configurationFiles()

	except Exception as e:
		print(f"{Fore.GREEN}[-] Erros : {e}{Style.RESET_ALL}")