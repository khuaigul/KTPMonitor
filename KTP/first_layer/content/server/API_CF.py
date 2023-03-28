# import requests
# import pprint
# import hashlib
# import time
# import json
# import os
#
# pref = "https://codeforces.com/api"
# key, secret = (line.strip() for line in open(os.path.abspath(os.path.dirname(__file__)) + "/secret/cf cred.txt", "r"))
#
# def authorized_request(method, params):
#     params.append(("apiKey", key))
#     params.append(("time", str(int(time.time()))))
#     params.sort()
#     partial_request = method + '?' + '&'.join([par + '=' + val for par, val in params])
#     hash_line = "ktpmon/" + partial_request + "#" + secret
#     apiSig = hashlib.sha512(hash_line.encode()).hexdigest()
#     final_request = pref + '/' + partial_request + "&apiSig=ktpmon" + apiSig
#     try:
#         return requests.get(final_request).json()
#     except:
#         return None