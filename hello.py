import requests
import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText
import boto3

s3 = boto3.client("s3")

def posli_email(zprava):
        email = "rezacdaniel2@gmail.com"
        heslo = "fpeg mksj wdml obgb"
    
        msg = MIMEText(zprava)
        msg ["Subject"] = "Monitoring problém!"
        msg ["From"] = email
        msg ["To"] = email
    
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email, heslo)
            server.send_message(msg)
            print("Email poslán!")
        


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
        posli_email(f"{url} nefunguje! Čas: {cas}")
        return

weby = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://nexeruno.github.io/hospoda/",
    "https://www.nefungujeto-123.cz"
]
while True:
    for web in weby:
        zkontroluj_web(web)
        s3.upload_file("monitoring_log.txt", "muj-prvni-bucket-dan-123", "monitoring_log.txt")
        time.sleep(5)
    

    


