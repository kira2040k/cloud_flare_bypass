# cloud_flare_bypass
<p>this tool scan your domain and get the real ip</p>

1. bruteforce real ip 
2. scan subdomains and get ip 

use <a href="https://www.shodan.io/">shodan</a> for check if ip owned by cloudflare

# usage:
-bruteforce ip
    
    example:
    python main.py https://google.com 

-scan subdomains
    
    python main --doamin <domain> --file <wordlist>
    
<img src=img/run.jpg>

