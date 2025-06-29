import socket
import pyfiglet
from pyfiglet import Figlet
import time
import threading
from colorama import Fore, Back, Style, init
init()
f = Figlet(font="slant")
text1 = f.renderText("Port").splitlines()
text2 = f.renderText("Scanner").splitlines()
for line1, line2 in zip(text1, text2):
    print(Fore.LIGHTGREEN_EX + line1 + Fore.MAGENTA + line2 + Fore.RESET)
print("by kk1lx💻", Fore.CYAN + "https://github.com/kk1lx" + Fore.RESET)
print(Fore.GREEN +  "[+] Enter (1)")
print(Fore.MAGENTA + "[-] Exit (0)")
print(Style.RESET_ALL)
choice = int(input("Enter your choice: "))

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip,port))
        print(f"[✔️] Port {port} is open")
        sock.close()
    except socket.error:
        pass

def main():
    target = (input("[📥] Enter Target IP: ")).strip()
    parts = target.split('.')
    if len(parts) != 4 or not all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
        print("[⚠️] Invalid IP")
        print("Exit through 3...")
        time.sleep(1)
        print("Exit through 2...")
        time.sleep(1)
        print("Exit through 1...")
        time.sleep(1)
    try:
        ports = int(input("[📥] Enter amount of ports to scan: "))
    except ValueError:
        print("[*] Input only numbers")
        return
    print("[🔍] Scanning ports...")
    print("[⏳] Please wait few seconds...")

    for port in range(1, ports +1):
        thread = threading.Thread(target=scan_port, args=(target, port), name="thr-1")
        thread.start()

    else:
        print(f"[✅] Port scan of {target} was finished")
        print("Exit through 5...")
        time.sleep(1)
        print("Exit through 4...")
        time.sleep(1)
        print("Exit through 3...")
        time.sleep(1)
        print("Exit through 2...")
        time.sleep(1)
        print("Exit through 1...")
        time.sleep(1)

if choice == 1:
    main()
else:
    exit()









