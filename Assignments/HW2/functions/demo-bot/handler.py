import requests
import datetime
import random

def handle(req):
    processed_text = req.lower().strip()
    preformat = list(processed_text.split())

    if "name" in preformat:
        response = get_name()
        return response
    elif "time" in preformat:
        response = get_time()
        return response
    elif "figlet" in preformat:
        response = get_figlet(req)
        return response
    else:
        response = "Sorry, I don't understand your question."
        return response
        
def get_name():
    names = ["Assistant", "Alexa", "Siri"]
    return "Hi, I am " + random.choice(names)

def get_time():
    now = datetime.datetime.now()
    responses = [
        f" Current time is {now.strftime('%H:%M %p')}",
        f" Current Date is {now.strftime('%A, %B  %d, %Y')}",
        f"Current Date and Time is {now.strftime('%A, %B %d, %Y,%H:%M %p')}",
    ]
    return random.choice(responses)

def get_figlet(question):
    text = question.split("for", 1)[1].strip()
    api_url = "http://127.0.0.1:8080/function/figlet"
    response = requests.post(api_url, data=text)
    return response.text