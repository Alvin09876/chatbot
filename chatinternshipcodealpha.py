import random


responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm doing great, thank you!", "I'm good, how about you?", "I'm just a bot, but I'm doing fine!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["Sorry, I don't understand that.", "Can you please rephrase?", "I'm not sure what you mean."]
}

def chatbot_response(user_input):
    
    user_input = user_input.lower()

    
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    
    return random.choice(responses["default"])

def chat():
    print("Hello! I'm a chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
    
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
