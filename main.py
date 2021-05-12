import requests
from forcediphttpsadapter.adapters import ForcedIPHTTPSAdapter
import threading
import ipaddress
import time
import sys
import argparse
import socket

my_parser = argparse.ArgumentParser()

my_parser.add_argument('--domain', action='store', type=str, required=False)
my_parser.add_argument('--file', action='store', type=str, required=False)
args = my_parser.parse_args()

def scan_subdomains_attack(subdomain):
    
        try:
            requests.get(subdomain)
            print(f'[+] {subdomain}  ip: {socket.gethostbyname(subdomain.replace("https://","").replace("http://",""))}')
        except:
            pass
def scan_subdomains(domain):
    print("-"*10,"use shodan for check if ip owned by cloudflare","-"*10) 
    file = open(args.file,"r")
    list = []
    for subdomain in file:
        try:
            subdomain = subdomain.split("\n")[0]
            url = f"https://{subdomain}.{domain}"
            threading.Thread(target=scan_subdomains_attack,args=(url,)).start()
        except:
            list.append(url)
    time.sleep(4)
    for sub in list:
        threading.Thread(target=scan_subdomains_attack,args=(sub,)).start()
        
if(args.domain):
    scan_subdomains(args.domain)
    sys.exit()

if(len(sys.argv) != 2):
    print("usage: main.py <url>")
    sys.exit()
def send_req(domain,ip):    
    
    try:
        session = requests.Session()
        session.mount(domain, ForcedIPHTTPSAdapter(dest_ip=ip)) # type the desired ip
        r = session.get(domain,timeout=5)
        print(f"found on: {ip}")
    except:
        pass
def main(domain):
    list = [] 
    for i in range(16776990,4294967296):
        try:
            ip = ipaddress.ip_address(i)
            if str(ip)[0:3] != "10." or str(ip)[0:4] != "127." or "192.168" not in str(ip):
                threading.Thread(target=send_req,args=(domain,ip,)).start()
        except:
            print("error")
            list.append(ip)
    time.sleep(4)
    for ip in list:
        threading.Thread(target=send_req,args=(domain,ip,)).start()
main(sys.argv[1])