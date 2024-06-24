# to run you need to cat (wordlist) | apifuzzer.py
# this script will show responses from website along with status code
import requests
import sys

# 200 = valid
# 401 = not authenticated

def loop():
    for word in sys.stdin: # replace loopback with target ip
        res = requests.get(url=f"http://127.0.0.1/{word}")
        if res.status_code == 404:
            loop()
        else:
            data = res.json()
            print(res.status_code)
            print(data)
            print(word)
loop()