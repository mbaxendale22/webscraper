import requests
from bs4 import BeautifulSoup
import smtplib
from data import data

# get URL
def scrape(url, selector):

    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.select(selector)

    if price is not None:
        for p in price:
            text_price = p.get_text()
            conv_price = float(text_price[1:])
            return conv_price

def send_mail(url, label):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(INSERT LOGIN DETAILS HERE!!!)

    subject = f"Price Reduction for {label}!"
    body = f"check the link: {url}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('mbaxendale21@gmail.com', 'mbaxendale21@gmail.com', msg)

    print("EMAIL SENT")

    server.quit



for item in data:

    curr_price = scrape(item['URL'], item['selector'])

    if curr_price is not None:
        if curr_price < 100.00:
            send_mail(item['URL'], item['label'])
            print('hello')



