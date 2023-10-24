import random

# Define a dictionary of predefined rules and responses
rules = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm just a chatbot, but thanks for asking!", "I'm doing well, thanks."],
    "what's your name": ["I'm just a chatbot, I don't have a name.", "You can call me Chatbot."],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm sorry, I don't understand. Please ask another question."]
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    
    for key in rules:
        if key in user_input:
            return random.choice(rules[key])
    
    return random.choice(rules["default"])

# Main chat loop
print("Hello! I'm a simple chatbot. You can start a conversation or type 'goodbye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "goodbye":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)