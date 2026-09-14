# -*- coding: utf-8 -*-


import requests
import time

URL = "http://127.0.0.1:5000/login"

username_to_test = "test_user"
passwords_wordlist = [
    "123456",
    "password",
    "admin2026",
    "secret123",
    "kurdish123"
]

print(f"دەستپێکرنا تێستکرنێ بۆ یوزەرێ: {username_to_test}\n" + "="*40)

for index, pwd in enumerate(passwords_wordlist, 1):
    print(f"تاقیکرنا {index}: [{pwd}]")
    
    payload = {'username': username_to_test, 'password': pwd}
    
    try:
        response = requests.post(URL, data=payload)
        res_data = response.json()

        if response.status_code == 200:
            print(f"\n[✓] سەرکەوتووبوو! {res_data['message']}")
            break
        elif response.status_code == 429:
            print(f"\n[!] ڕاوەستیا: {res_data['message']}")
            break
        else:
            print(f"[✗] ئەنجام: {res_data['message']}")

    except Exception as e:
        print(f"[!] ئاریشە د پەیوەندیا سێرڤەری دا هەیە: {e}")
        break

    time.sleep(1)
