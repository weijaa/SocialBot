import urllib
import json
import os
import requests
import re
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from flask import make_response, jsonify
import random
def response(keyword):
    url = 'http://news.fcu.edu.tw/wSite/lp?ctNode=31973&mp=101001&idPath='
    view = requests.get(url)
    soup = BeautifulSoup(view.text, 'html.parser')
    report = soup.find_all('a', href = re.compile('http://web.pr.fcu.edu.tw/~pr/fest*'))
    news = []
    link = []

    for i in report:
        if keyword in i.text:
            news.append(i.text)
            link.append(i['href'])
    num = random.randint(0,len(news)-1)
    print(num)
    print(news[num])
    print('link：',link[num])
    msg = news[num]+ 'Link：'+ link[num]
    return msg
# Flask app should start in global layout
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    if req['queryResult']['parameters']['any'] != '':
        keyword = req['queryResult']['parameters']['any']
        print(keyword)
    
    res_message = {"fulfillmentText": response(keyword)}
    print(res_message)
    
    return make_response(jsonify(res_message))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)


