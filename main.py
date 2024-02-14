import json
import random

with open('json/data.json', 'r') as file:
    responses = json.load(file)

def get_response(message):
    message = message.lower()
    
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def main():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
