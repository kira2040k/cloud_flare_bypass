import requests
from forcediphttpsadapter.adapters import ForcedIPHTTPSAdapter
import threading
import ipaddress
import time
import sys
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
