import pyfiglet
from tools.scanner import scanner
from tools.enumerator import enumerator
from colorama import Fore, Style
from tools.hashscan import hashscan
print(f"{Fore.BLUE}-" * 50)
ascii_banner = pyfiglet.figlet_format(f"INSPECTOR")
print(ascii_banner)
print("Version 0.3.1 BETA")
print("-" * 50)

scanner_instance = scanner.PortScanner()


def weapon():
    mode = input(f"{Style.RESET_ALL}Pick the tool you wanna use: \n 1. Port Scanner\n 2. Enumerator\n 3. Hash Scanner \n")
    if mode == "1" or mode.lower() == "port scanner":
        try:
            scanner_instance.scan_port()
        except KeyboardInterrupt:
            print("Shutting down")
    elif mode == "2" or mode.lower() == "enumerator":
        try:
            enumerator.tool()
        except KeyboardInterrupt:
            print("Shutting down")        
    elif mode == "3" or mode.lower() == "hash scanner":
        try:
            hashscan.start()
        except KeyboardInterrupt:
            print("Shutting down") 

try:
    while True:
        weapon()
except KeyboardInterrupt:
    print("Shutting Down...")



