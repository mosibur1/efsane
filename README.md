# Efsane Bypass Script  

This script automates the registration process on **EfsaneTR** by solving captchas, sending OTP requests, and submitting registration forms.  

## ⚠ Disclaimer  
This script is developed **for educational purposes only**. Misuse of this script is **strictly prohibited**. Use at your own risk!  

---

## ✨ Features  
✔ **Captcha Bypass** (Cloudflare Turnstile)  
✔ **Automated OTP Request**  
✔ **Proxy Support** (Uses random proxies from `proxies.txt`)  
✔ **User-Agent Randomization**  
✔ **Automated Registration**  

---

## 📜 Requirements  

Make sure you have **Python 3.7+** installed on your system.  

### 🔧 Install Dependencies  

Run the following command to install required Python modules:  

```bash
pip install requests colorama anticaptchaofficial
```

---

## 🚀 How to Use  

1. **Clone the Repository**  

```bash
git clone https://github.com/mosibur1/efsane.git
cd efsane
```

2. **Prepare Proxies**  

- Create a `proxies.txt` file in the same directory as the script.  
- Add HTTP/HTTPS proxies in the format:  
  ```
  http://user:pass@proxy_ip:port
  https://proxy_ip:port
  ```
  
3. **Run the Script**  

```bash
python main.py
```

4. **Follow On-Screen Instructions**  

- Enter your **invite code** (only once).  
- Provide **Country Code** and **Mobile Number**.  
- The script will solve the captcha and send an OTP request.  
- Enter the **OTP received** on your mobile.  
- The script will attempt to complete the registration.  

---

## 🛠 Troubleshooting  

1. **Proxies Not Found?**  
   - Make sure `proxies.txt` exists and contains working proxies.  
   
2. **Captcha Not Solving?**  
   - Ensure your **AntiCaptcha API key** is valid.  
   - If needed, update the API key in the `captcha_bypass()` function.  

3. **Registration Fails?**  
   - Ensure the phone number format is correct.  
   - Verify that the invite code is still active.  

---

## 👨‍💻 Developer Notes  

- The script uses **random user-agents** to mimic real users.  
- The password used is hardcoded as `"Abcdef123@_#"` (you can change it).  
- The script **exits gracefully** on `CTRL+C`.  

---

### 🏴‍☠️ Warning  

Using this script to spam, exploit, or bypass security systems **may violate legal policies**. The author is **not responsible** for any misuse.  

---

### 📜 License  

**MIT License** - Feel free to modify and distribute!
