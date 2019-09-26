import requests
import smtplib
from bs4 import BeautifulSoup


URL = 'https://www.amazon.com/Akko-Ducky-One-Mechanical-Keyboard/dp/B07MMD7LLD/ref=sr_1_3?keywords=anne+pro&qid=1569506118&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    prettifyed_soup = BeautifulSoup(soup.prettify(), 'html.parser')

    title = prettifyed_soup.find(id="productTitle").get_text()
    price = prettifyed_soup.find(id="priceblock_ourprice").get_text()
    text_price = price
    price = price.replace('$', '')
    price = price.replace(',', '')
    price = price.replace('.', '')
    converted_price = float(price)

    if(converted_price < 13300):
        send_email(text_price)


def send_email(price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pythonmailer.vitor@gmail.com', 'Justamailer123')
    subject = 'Hey! The price fell down to ' + price + '!!!'
    body = 'Check the amazon link! https://www.amazon.com/Akko-Ducky-One-Mechanical-Keyboard/dp/B07MMD7LLD/ref=sr_1_3?keywords=anne+pro&qid=1569506118&sr=8-3'
    msg = f"subject: {subject}\n\n{body}"
    server.sendmail(
        'pythonmailer.vitor@gmail.com',
        'YOUREMAILHERE@CHANGEIT.COM',
        msg
    )
    print("AN EMAIL HAS BEEN SENT!")
    server.quit()


check_price()
