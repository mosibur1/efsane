import requests
import time
import random
import sys
from anticaptchaofficial.turnstileproxyless import turnstileProxyless
from colorama import Fore, Style, init

init(autoreset=True)  # Enable colors in CLI

# Banner
def print_banner():
    banner = f"""{Fore.CYAN}
   __  ______  ___  _________________ __
  /  |/  / _ \/ _ \/_  __/ __/ ___/ // /
 / /|_/ / , _/ ___/ / / / _// /__/ _  / 
/_/  /_/_/|_/_/    /_/ /___/\___/_//_/  
                                        
{Style.RESET_ALL}
{Fore.YELLOW}[*] Efsanetr Bypass Script By MRPTech - Automated Registration
[*] Developed for educational purposes only!
[*] Use at your own risk.
----------------------------------------------------{Style.RESET_ALL}
"""
    print(banner)

# Global variable for invite code
invite_code = None

# Function to handle exit on CTRL+C
def exit_script():
    print(Fore.RED + "\n[✘] Process interrupted by user. Exiting...")
    sys.exit(1)

# Call the banner at the start of the script
print_banner()

# Captcha Bypass Function
def captcha_bypass():
    print(Fore.YELLOW + "[*] Solving Captcha... Please wait.")
    
    try:
        solver = turnstileProxyless()
        solver.set_verbose(1)
        solver.set_key("296c3d4ba479eeb2c80922baaffd65e0")
        solver.set_website_url("https://efsanetr.com")
        solver.set_website_key("0x4AAAAAAA8edKY9bI4XxjIA")

        token = solver.solve_and_return_solution()

        if token:
            print(Fore.GREEN + "[✔] Captcha solved successfully!")
            return token
        else:
            print(Fore.RED + "[✘] Captcha failed. Error:", solver.error_code)
            return None
    except KeyboardInterrupt:
        exit_script()

# OTP Request Function
def send_code(session, country_code, mobile, captcha_token):
    url = "https://efsanetr.com/api/v2/send/mobileCode"
    payload = {'mobile': mobile, 'countryCode': country_code}
    
    headers = {
        'User-Agent': random_user_agent(),
        'Verification': captcha_token,
        'X-Requested-With': "XMLHttpRequest",
        'Referer': "https://efsanetr.com/en_US/internal/register/",
    }
    
    print(Fore.YELLOW + "[*] Sending OTP request...")
    try:
        response = session.post(url, data=payload, headers=headers).json()
        if response.get("code") == 0:
            print(Fore.GREEN + "[✔] OTP sent successfully!")
            return response
        else:
            print(Fore.RED + f"[✘] OTP failed: {response}")
            return None
    except KeyboardInterrupt:
        exit_script()

# Registration Function
def register(session, mobile, captcha_token, password, country_code, valid_code):
    global invite_code
    url = "https://efsanetr.com/api/v2/register"
    
    payload = {
        'mobile': mobile,
        'inviteCode': invite_code,
        'cf-turnstile-response': captcha_token,
        'passWord': password,
        'confirmPassWord': password,
        'type': "1",
        'countryCode': country_code,
        'validCode': valid_code
    }
    
    headers = {
        'User-Agent': random_user_agent(),
        'Verification': captcha_token,
        'X-Requested-With': "XMLHttpRequest",
        'Referer': "https://efsanetr.com/en_US/internal/register/",
    }
    
    print(Fore.YELLOW + "[*] Submitting registration...")
    try:
        response = session.post(url, data=payload, headers=headers).json()
        print(Fore.CYAN + f"[ℹ] API Response: {response}")
        if response.get("code") == 0:
            print(Fore.GREEN + "[✔] Registration successful!")
        else:
            print(Fore.RED + f"[✘] Registration failed: {response.get('message', 'Unknown Error')}")
    except KeyboardInterrupt:
        exit_script()

# Function for Random User-Agent
def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
    ]
    return random.choice(user_agents)

# Function to Fetch Proxies from File
def get_proxies_from_file(file_path="proxies.txt"):
    try:
        with open(file_path, "r") as file:
            proxies = file.readlines()
        proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
        return proxies
    except FileNotFoundError:
        print(Fore.RED + "[✘] Proxies file not found.")
        exit_script()

# Function to Handle Proxy Input
def get_proxy(proxies):
    if proxies:
        return {"http": random.choice(proxies), "https": random.choice(proxies)}
    return None

# Function to Ask for Invite Code Once
def get_invite_code():
    global invite_code
    if invite_code is None:
        invite_code = input(Fore.YELLOW + "> Enter Invite Code: ").strip()

# Main Execution Loop
try:
    print(Fore.CYAN + "\n=== Welcome to the Efsane Bypass Script ===\n")
    
    get_invite_code()
    
    proxies = get_proxies_from_file()  # Fetch proxies from proxies.txt
    if not proxies:
        print(Fore.RED + "[✘] No proxies found. Exiting...")
        exit_script()

    while True:
        session = requests.Session()
        proxy = get_proxy(proxies)
        if proxy:
            session.proxies.update(proxy)
            print(Fore.GREEN + f"[*] Using proxy: {proxy}")

        country_code = input(Fore.YELLOW + "> Enter Country Code (without +): ").strip()
        mobile = input(Fore.YELLOW + "> Enter Mobile Number (without country code): ").strip()
        password = "Abcdef123@_#"  # You can modify this to be user-defined
        
        # Captcha Bypass
        captcha_token = captcha_bypass()
        if not captcha_token:
            continue  # Retry if captcha fails

        # Send OTP
        otp_response = send_code(session, country_code, mobile, captcha_token)
        if not otp_response:
            continue  # Retry if OTP fails

        otp = input(Fore.YELLOW + "> Enter OTP received on your mobile: ").strip()
        
        # Register User
        register(session, mobile, captcha_token, password, country_code, otp)

except KeyboardInterrupt:
    exit_script()
