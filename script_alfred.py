#!/usr/bin/env python3
# coding: utf-8
# vi: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from os import times
import sys
import requests
import threading
import json
import random
import time
import concurrent.futures as cf
from datetime import datetime as dt
from requests_toolbelt.multipart.encoder import MultipartEncoder as Form
import os.path
from collections import defaultdict, Counter


URL = 'http://votingappg2-testchargeg2.westus.cloudapp.azure.com'
jsonFile = "./data.json"

if os.path.exists(jsonFile) == False:
    dictionary = {
}
    json_object = json.dumps(dictionary, indent=4)

    with open(jsonFile, "x") as outfile:
        outfile.write(json_object)

def make_form(value):
    f = Form({'vote': value})
    return f.content_type, f.to_string()


f_cats_ct, f_cats = make_form('Cats')
f_dogs_ct, f_dogs = make_form('Dogs')
f_reset_ct, f_reset = make_form('Reset')


quit = threading.Event()

jsonData = defaultdict(Counter)


def send_votes(thread_id: int, quit: threading.Event):
    j = 0
    while not quit.is_set():
        f, ct = random.choice(((f_cats, f_cats_ct), (f_dogs, f_dogs_ct)))
        r = requests.post(URL, data=f, headers={'Content-Type': ct})
        j += 1
        if not r.ok:
            print(f"[{dt.now()}] thread {thread_id}, request {j}: Error {r.status_code}")
            continue

        print(f"[{dt.now()}] thread {thread_id}, request {j}: {r.headers['X-HANDLED-BY']}")

        """
        { 
            "<instance>": {
                "<timestamp>": <nb_req>
            }
        }
        """
        xhandled = r.headers['X-HANDLED-BY']
        timestamp = str(int(dt.now().timestamp()))
        jsonData[xhandled][timestamp] += 1

        """
        if xhandled not in jsonData:
            jsonData[xhandled] = {}
        
        if timestamp not in jsonData[xhandled]:
            jsonData[xhandled][timestamp] = 0
        
        jsonData[xhandled][timestamp] += 1
        """

    return jsonData


def main():
    print(f"[{time.mktime(dt.now().timetuple())}]  DÃ©but du test")

    quits = []
    with cf.ThreadPoolExecutor(10) as exc:
        try:
            for i in range(1, 10, 2):
                q = threading.Event()
                quits.append(q)
                exc.submit(send_votes, i, q)
                exc.submit(send_votes, i + 1, q)
                time.sleep(300)

            for q in quits:
                q.set()
                time.sleep(300)
        except KeyboardInterrupt:
            pass

        for q in quits:
            q.set()
    
    print(jsonData)
    with open (jsonFile,"w") as outfile:
        json.dump(jsonData, outfile, indent=4)


    print(f"[{dt.now()}] Fin du test")
    return


if __name__ == '__main__':
    sys.exit(main())