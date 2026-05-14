import requests
import time
import os
import boto3
from datetime import datetime
from dotenv import load_dotenv
from prometheus_client import start_http_server, Gauge



load_dotenv()
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
AWS_REGION = os.getenv("AWS_REGION")
s3 = boto3.client("s3", region_name=AWS_REGION)

WEB_STATUS = Gauge("web_status", "Status webu: 1 = funguje, 0 = nefunguje", ["name", "url"])
WEB_RESPONSE_TIME = Gauge("web_response_time_seconds", "Cas odezvy webu v sekundach", ["name", "url"])

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
    name = web["name"]
    url = web["url"]
    cas = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    try:
        odpoved = requests.get(url)
        if odpoved.status_code == 200:
            WEB_STATUS.labels(name=name, url=url).set(1)
            WEB_RESPONSE_TIME.labels(name=name, url=url).set(odpoved.elapsed.total_seconds())
            print(f"{url}- Web funguje! ({odpoved.elapsed.total_seconds()}s)")
            with open("monitoring_log.txt", "a") as f:
                f.write(f"{cas} - {url} funguje\n")
        else:
            WEB_STATUS.labels(name=name, url=url).set(0)
            WEB_RESPONSE_TIME.labels(name=name, url=url).set(odpoved.elapsed.total_seconds())
            print(f"{url}- Web nefunguje! ({odpoved.elapsed.total_seconds()}s)")
            with open("monitoring_log.txt", "a") as f:
                f.write(f"{cas} - {url} nefunguje\n")
            
    except:
        WEB_STATUS.labels(name=name, url=url).set(0)
        WEB_RESPONSE_TIME.labels(name=name, url=url).set(0)
        with open("monitoring_log.txt", "a") as f:
            f.write(f"{cas} - {url} nefunguje\n")
        posli_slack(f"{url} nefunguje! Čas: {cas}")
        return

weby = [
    {"name": "Google", "url": "https://www.google.com"},
    {"name": "Facebook", "url": "https://www.facebook.com"},
    {"name": "Seznam", "url": "https://www.seznam.cz/"},
    {"name": "Dont work", "url":"https://www.dont-work-123.com"}
]

start_http_server(8000)
print("Prometheus metriky bezi na http://localhost:8000/metrics")

while True:
    for web in weby:
        zkontroluj_web(web)
        s3.upload_file("monitoring_log.txt", AWS_BUCKET_NAME, "monitoring_log.txt")
        time.sleep(5)