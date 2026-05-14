import requests
import time
import os
import boto3
from datetime import datetime
from dotenv import load_dotenv



load_dotenv()
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
AWS_REGION = os.getenv("AWS_REGION")
s3 = boto3.client("s3", region_name=AWS_REGION)

def posli_slack(zprava):
    payload = {
        "text": zprava
    }
    odpoved = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
        
    if odpoved.status_code == 200:
        print("Slack poslán!")
    else:
        print(f"Slack chyba: {odpoved.status_code} - {odpoved.text}")

def zkontroluj_web(url):
    cas = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    try:
        odpoved = requests.get(url)
        if odpoved.status_code == 200:
            print(f"{url}- Web funguje! ({odpoved.elapsed.total_seconds()}s)")
            with open("monitoring_log.txt", "a") as f:
                f.write(f"{cas} - {url} funguje\n")
        else:
            print(f"{url}- Web nefunguje! ({odpoved.elapsed.total_seconds()}s)")
            with open("monitoring_log.txt", "a") as f:
                f.write(f"{cas} - {url} nefunguje\n")
            
    except:
        with open("monitoring_log.txt", "a") as f:
            f.write(f"{cas} - {url} nefunguje\n")
        posli_slack(f"{url} nefunguje! Čas: {cas}")
        return

weby = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://nexeruno.github.io/hospoda/",
    "https://www.dont-work-123.com"
]
while True:
    for web in weby:
        zkontroluj_web(web)
        s3.upload_file("monitoring_log.txt", AWS_BUCKET_NAME, "monitoring_log.txt")
        time.sleep(5)
    

    


