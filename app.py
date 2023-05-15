from flask import Flask, jsonify, render_template

import requests
from urllib.parse import urlparse
import re
from bs4 import BeautifulSoup
import joblib


app = Flask(__name__)

@app.route('/')
def hello_world():
    return  render_template('index.html')

@app.route('/PhishingAlertAPI/<path:new_url>')
def check_if_phishing(new_url):
    
    #URL length
    url_len = len(new_url)
    URL_Length = -1
    if url_len < 54:
        URL_Length = 1
    elif url_len >= 54 and url_len <=75:
        URL_Length = 0
    
    #Having @ symbol
    having_At_Symbol = -1
    if new_url.find("@")==-1:
        having_At_Symbol = 1

    #Positioning of //

    try:
        position = new_url.index("//")
    except ValueError:
        double_slash_redirecting=-1
    
    if position+1 > 7:
        double_slash_redirecting=-1
    else:
        double_slash_redirecting=1
    
    #Having Hyphen
    HavingHyphen = -1
    if new_url.find("-")==-1:
        HavingHyphen = 1


   #Page rank using api

    headers = {'API-OPR':'c8g4404gswswcok8s0k4404ko4g00oo8w4ks84g4'}
    requested_url = 'https://www.google.com/docs/about/'
    parsed_url = urlparse(requested_url)
    domain = parsed_url.netloc
    url = 'https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D=' + domain
    request = requests.get(url, headers=headers)
    result = request.json()

    page_rank = result['response'][0]['page_rank_decimal']
    if page_rank < 20:
        Page_Rank = -1
    else:
        Page_Rank = 1

    
    #Checking if website is indexed in Google 
    Google_Index = -1

    google = "https://www.google.com/search?q=site:" + domain + "&hl=en"
    response = requests.get(google, cookies={"CONSENT": "YES+1"})
    soup = BeautifulSoup(response.content, "html.parser")
    not_indexed = re.compile("did not match any documents")

    if soup(text=not_indexed):
        Google_Index =-1
    else:
        Google_Index= 1
    
    #Combining all of it 
    X_pred = [URL_Length,having_At_Symbol,double_slash_redirecting,HavingHyphen,Page_Rank,Google_Index] 


    #Getting the model from pickle
    filename = 'model.joblib'
    loaded_model = joblib.load(filename)

    # Use the loaded model for predictions
    result = loaded_model.predict([X_pred])[0]
    if result == 1:
        response = {'url': new_url, 'Result':'Not Phishing', 'Result_binary':1}
    else:
        response = {'url': new_url, 'Result':'Phishing', 'Result_binary':-1}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)