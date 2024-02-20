import requests
import datetime
import random
import urllib3


def handle(req): 
    #question = json.loads(req)["question"]
    # response = get_figlet(req)
    processed_question = req.lower().strip()
    preformat = list(processed_question.split())
    
    if "name" in preformat:
        response = get_name()
        return response
    elif "time" in preformat:
        response = get_time()
        return response
    elif "figlet" in preformat:
        # text = req.split("for", 1)[1].strip()
        # gateway_url = "http://127.0.0.1:8080/function/figlet"
        # #print(text)
        # response = requests.post(gateway_url, data=str(text))
        # return response.text
        response = get_figlet(req)
        # print(dir(response.text))
        res=response.text.decode('utf-8')
        # print(response)
        # res=response.text.encode('utf-8')
        # plain_text= res.decode('utf-8')
        # print(plain_text)
        # print()
        print(res)
        return res

    # elif "figlet" in processed_question:
    #     response = get_figlet(req)
        
        # if response.status_code == 200:
        #     try:
        #         result = response.json()
        #         return result
        #     except json.JSONDecodeError
        #         return response.text
        # else:
        # return response
    # else:
    #     response = "Sorry, I don't understand your question."
    #     return response
    #return json.dumps({"response": response})
    # return response

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
    headers = {'Content-Type': 'text/plain'}
    gateway_url = "http://127.0.0.1:8080/function/figlet"
    #gateway_url = "http://localhost:8080/function/figlet"
    #print(text)
    response = requests.post(gateway_url, data=text, headers=headers)
    return response

a="figlet for Panya"
b = handle(a)
print(b)