# PhishingWebsiteDetection

## Introduction
Phishing is a type of cyber attack where attackers uses social engineering techniques to trick the victum into giving their sensitive information, such as login credentials,credit card details, or other personal information.

## How do we detect it ?
We are using Machine Learning to detect whether a particular website is phishing or not, Logistic Regression has been used based on the semantic and network based features of the url. Manual Threshold has been set to optimize the True positive rate.

The notebook can be find here https://www.kaggle.com/code/tenzintsundue/phishing-website-detection.

## About the API
API has been created here that give information about the result prediction. The response will be in json format.

"Result": Whether the website url sent is phishing or not.[Possible Values:"Phishing", "Not Phishing"]

"Result_binary": [Possible Values: -1 (phishing), 1(legitimate)]

"url": sends back the url.
## Steps
../PhishingAlertAPI/mysite :

.. signify current path and 

mysite is website which you want to test if its phishing or not
