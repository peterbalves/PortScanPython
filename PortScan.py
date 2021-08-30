import os
import socket

portas = [21, 22, 23, 80, 443, 53, 8080]
banner = """
 ______   ______     ______     ______   ______     ______     ______     __   __    
/\  == \ /\  __ \   /\  == \   /\__  _\ /\  ___\   /\  ___\   /\  __ \   /\ "-.\ \   
\ \  _-/ \ \ \/\ \  \ \  __<   \/_/\ \/ \ \___  \  \ \ \____  \ \  __ \  \ \ \-.  \  
 \ \_\    \ \_____\  \ \_\ \_\    \ \_\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_||"\_\ 
  \/_/     \/_____/   \/_/ /_/     \/_/   \/_____/   \/_____/   \/_/\/_/   \/_/ \/_/
"""

os.system("cls")
os.system("color 04")
print(banner)
site = input("Site/IP: ")

for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((site, porta))
    sock.close()
    if result == 0:
        print(porta)