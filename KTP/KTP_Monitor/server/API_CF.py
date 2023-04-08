# Тут находится функция, которая делает запрос на CF.

import requests
import pprint
import hashlib
import time
import json
import os


key = "7215c0283517a75de3d6e8f5b9e7cd91d36a08a0"
secret = "f8b4cf3203a5455f89c0ca553b4fe40eef6c674d"
pref = "https://codeforces.com/api"
# key, secret = (line.strip() for line in open(os.path.abspath(os.path.dirname(__file__)) + "/secret/cf cred.txt", "r"))


def authorized_request(method, params):  # Получение информации с CF
    params.append(("apiKey", key))
    params.append(("time", str(int(time.time()))))
    params.sort()
    partial_request = method + '?' + '&'.join([par + '=' + val for par, val in params])
    hash_line = "ktpmon/" + partial_request + "#" + secret
    api_sig = hashlib.sha512(hash_line.encode()).hexdigest()
    final_request = pref + '/' + partial_request + "&apiSig=ktpmon" + api_sig
    try:
        return requests.get(final_request).json()
    except:
        return None
