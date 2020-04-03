import time
import urllib.request

a = '<html><p>This is a example only </p><strong>$597.50</strong> </html>'
def find_price():
    page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
    text = page.read().decode('utf8')
    text_upper = text.upper()
    price_letter = []
    for letter_index in range(text_upper.find('>$'),len(text_upper)):
        if text_upper[letter_index+2] == '<':
            break
        else:
            price_letter.append(a[letter_index+2])

    return ''.join([letter for letter in price_letter])
price_now = input("Do you want to see the price now (Y/N)?")
if price_now =='Y':
    print(price_now)
else:
    price = 99.99
    while price >4.74:
        time.sleep(300)
        price = find_price()
    print("Buy!")

def send_to_twitter():
    msg = "I am a message that will be sent to Twitter"
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add("Twitter API",
                         "https://twitter.com/statuses",
                         username,
                         password,
                        )
    http_handler = urllib.request.HTTPBasicAuthHandler