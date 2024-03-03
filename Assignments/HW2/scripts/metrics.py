import requests
import time

class ChatbotPerformanceAnalyzer:
    def __init__(self, chatbot_url):
        self.chatbot_url = chatbot_url

    def measure_response_time(self, data, repeat=1):
        total_time = 0
        for _ in range(repeat):
            start_time = time.time()
            response = requests.post(self.chatbot_url, data=data)
            end_time = time.time()
            total_time += (end_time - start_time)
            if repeat == 1:  
                return end_time - start_time
        return total_time / repeat  

    def analyze_performance(self):
        
        # The first request that does not call figlet
        response_time_a = self.measure_response_time("name")
        print(f"Response time for the first request using no figlet call: {response_time_a:.4f} seconds")

        # The second request that does not call figlet
        response_time_b = self.measure_response_time("name")
        print(f"Response time for the second request using no figlet call: {response_time_b:.4f} seconds")

        # Avg over 10 requests that do not call figlet
        average_response_time_c = self.measure_response_time("What is your name?", repeat=10)
        print(f"Average response time over 10 requests using no figlet call: {average_response_time_c:.4f} seconds")

        # The first request that calls figlet
        response_time_d = self.measure_response_time("figlet generate Hello")
        print(f"Response time for the first request using with figlet call: {response_time_d:.4f} seconds")

        # The second request that calls figlet
        response_time_e = self.measure_response_time("figlet generate Hello")
        print(f"Response time for the second request using with figlet call: {response_time_e:.4f} seconds")

        # The second request that calls figlet following the first request that does not call figlet
        
        # Measure the first request with no figlet
        self.measure_response_time("name")
        
        # The second request with figlet
        response_time_f = self.measure_response_time("figlet generate Hello")
        print(f"Response time for the second request using with figlet and after without figlet call: {response_time_f:.4f} seconds")

        # Avg 10 requests that call figlet
        average_response_time_g = self.measure_response_time("figlet generate Hello", repeat=10)
        print(f"Average response time over 10 requests using figlet call: {average_response_time_g:.4f} seconds")

if __name__ == "__main__":
    # chatbot's endpoint
    CHATBOT_URL = "http://10.62.0.1:8080/function/chatbot"
    analyzer = ChatbotPerformanceAnalyzer(CHATBOT_URL)
    analyzer.analyze_performance()

