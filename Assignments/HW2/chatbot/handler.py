import requests
import datetime
import random

# Chatbot Handler Function
def handle(req): 
    processedText = req.lower().strip()
    preformat = list(processedText.split())
    
    if "name" in preformat:
        response = get_name()
    elif "time" in preformat:
        response = get_time()
    elif "figlet" in preformat:
        response = get_figlet(req)
    else:
        return "here is a sample questions you can ask.\n\n1. What is your name\n2. what is the current time\n3. figlet generate HI\n"
    return response

# Random name generator for chatbot
def get_name():
    names = ["Assistant", "Alexa", "Siri"]
    return "Hi, I am " + random.choice(names)

# Random format for current date and time generator.
def get_time():
    now = datetime.datetime.now()
    responses = [
        "Current time is {}".format(now.strftime('%I:%M %p')),
        "Current Date is {}".format(now.strftime('%A, %B %d, %Y')),
        "Current Date and Time is {}".format(now.strftime('%A, %B %d, %Y, %I:%M %p')),
    ]
    return random.choice(responses)

# External figlet function calling function.
def get_figlet(req):
    text = req.split("generate", 1)[1].strip()
    url="http://10.62.0.1:8080/function/figlet"
    result = requests.post(url, data=text)
    return result.text


