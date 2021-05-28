#!/bin/python
import requests
import re
import argparse

parser = argparse.ArgumentParser(description='Converts Facebook Profile URLs into Facebook Profile IDs')
parser.add_argument("url", help="Facebook Profile URL. Should look something like this: https://www.facebook.com/{username}")
args = parser.parse_args()

url = args.url

def urlToID(url):
    if "https://facebook.com/" in url or "https://www.facebook.com/" in url:
        pass   
    else:
        print("[-] Please input a valid Facebook Profile URL (ex: https://www.facebook.com/{username})")
        raise Exception("Invalid Facebook Profile URL")

    r = requests.get(url)
    if r.ok:
        html_response = r.text
        fb_id = re.search(r'"fb://profile/(.*?)"', html_response).group(1)
        return fb_id
    else:
        print("[-] Error while sending request to Facebook: Got response code {}".format(r.status_code))
        exit()

fb_id = urlToID(url)
print(f"[+] ID: {fb_id}")
print(f"[+] Static Profile URL: https://www.facebook.com/profile.php?id={fb_id}")
