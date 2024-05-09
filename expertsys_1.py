# Expert system for Help desk management:
problem_dict = {
 "Printer not working": "Check that it's turned on and connected to the network",
 "Can't log in": "Make sure you're using the correct username and password",
 "Software not installing": "Check that your computer meets the system requirements",
 "Internet connection not working": "Restart your modem or router",
 "Email not sending": "Check that you're using the correct email server settings"
}

# Define a function to handle user requests 
def handle_request(user_input):
    if user_input.lower() == "exit":
        return "Goodbye!"
    elif user_input in problem_dict:
        return problem_dict[user_input]
    else:
        return "I'm sorry, I don't know how to help with that problem."

# Main loop to prompt user for input 
while True:
    user_input = input("What's the problem? Type 'exit' to quit. ")
    response = handle_request(user_input)
    print(response)
    if response == "Goodbye!":
        break

#Stock Market Expert System
import random

class StockMarketExpertSystem:
    def __init__(self, moving_average, rsi):
        self.moving_average = moving_average
        self.rsi = rsi

    def recommend_action(self):
        if self.moving_average == 'crossover' and self.rsi == 'overbought':
            return "Sell"
        elif self.moving_average == 'crossover' and self.rsi == 'oversold':
            return "Buy"
        elif self.moving_average == 'crossover':
            return "Hold"
        elif self.rsi == 'overbought':
            return "Hold"
        elif self.rsi == 'oversold':
            return "Buy"
        else:
            return "No clear recommendation"

def main():
    moving_average = random.choice(['crossover', 'no_crossover'])
    rsi = random.choice(['overbought', 'oversold', 'normal'])
    
    expert_system = StockMarketExpertSystem(moving_average, rsi)
    action = expert_system.recommend_action()

    print("Moving Average:", moving_average)
    print("RSI:", rsi)
    print("Recommendation:", action)

if __name__ == "__main__":
    main()

# Hospital and medical diagnosis system:
problem_dict = {
    "throat pain": "Check for strep throat.",
    "high fever": "Possible infection. Consider seeing a doctor.",
    "pain in lungs": "Possible signs of asthma. Consult a healthcare provider.",
    "continuous headache": "Could be a migraine. If persistent, see a doctor."
}

# Define a function to handle user requests
def handle_request(user_input):
    user_input = user_input.lower().strip()
    if user_input == "exit":
        return "Get well soon!"
    elif user_input in problem_dict:
        return problem_dict[user_input]
    else:
        return "I'm sorry, I don't know how to help with that problem."

# Main loop to prompt user for input
while True:
    user_input = input("What's the problem? Type 'exit' to quit. ")
    response = handle_request(user_input)
    print(response)
    if response == "Get well soon!":
        break
