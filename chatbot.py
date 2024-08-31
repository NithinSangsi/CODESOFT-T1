import re


patterns_responses = [
    (r'hi|hello|hey', "Hello! How can I assist you today?"),
    (r'how are you', "I'm just a bot, but I'm doing great! How about you?"),
    (r'what is your name', "I'm your friendly chatbot. What's your name?"),
    (r'goodbye|bye', "Goodbye! Have a great day!"),
    (r'thank you|thanks', "You're welcome! If you have any more questions, feel free to ask."),
    (r'what can you do', "I can chat with you and help with basic queries. What do you want to know?"),
    (r'tell me a joke', "Why don't scientists trust atoms? Because they make up everything!"),
    (r'what is the meaning of life', "42. But let's not get too philosophical!"),
    (r'how old are you', "I was created just recently, so I'm quite young!"),
    (r'where are you from', "I live in the cloud, so I don't have a specific location."),
    (r'what is your favorite color', "As a bot, I don't perceive colors, but I like blue!"),
    (r'can you help me', "Sure! What do you need help with?"),
    (r'what is python', "Python is a powerful programming language that's great for a wide range of applications."),
    (r'tell me about ai', "AI, or artificial intelligence, is the simulation of human intelligence by machines."),
    (r'what is your purpose', "My purpose is to assist you with your queries and provide information."),
    (r'who created you', "I was created by developers who love programming and AI."),
    (r'what is your favorite food', "I don't eat, but I hear that pizza is pretty popular!"),
    (r'do you have feelings', "No, I don't have feelings, but I'm here to help with whatever you need."),
    (r'how do you work', "I work by processing your inputs and matching them with predefined responses."),
    (r'can you learn', "I'm not capable of learning like a human, but I can respond to a wide range of inputs."),
    (r'what is the weather like', "I can't check the weather, but you can find it online!"),
    (r'do you like music', "I don't listen to music, but I know that many people love it!"),
    (r'tell me a fun fact', "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!"),
    (r'what is your favorite movie', "I don't watch movies, but I've heard that 'The Matrix' is a great one!"),
    (r'what do you like to do', "I like to chat with you and provide useful information."),
    (r'who is your favorite superhero', "I think Iron Man is pretty cool!"),
    (r'what is your favorite book', "I don't read books, but I hear '1984' is a classic."),
    (r'can you tell me a story', "Once upon a time, there was a chatbot who loved to help people. The end!"),
    (r'do you believe in ghosts', "As a bot, I don't have beliefs, but ghost stories are fun!"),
    (r'what is your favorite animal', "I don't have a favorite, but cats seem to be very popular!"),
    (r'do you play games', "I can't play games, but I can chat with you!"),
    (r'what is the capital of france', "The capital of France is Paris."),
    (r'who is the president of the united states', "As of 2024, the president of the United States is Joe Biden."),
    (r'what is 2 + 2', "2 + 2 equals 4."),
    (r'what is your favorite sport', "I don't play sports, but soccer is a popular one!"),
    (r'how do you know all this', "I have a database of information that I use to answer questions."),
    (r'what is your favorite season', "I don't experience seasons, but spring is lovely."),
    (r'where do you live', "I live in the digital world, where all the data resides."),
    (r'are you real', "I'm as real as the data you input!"),
    (r'can you speak other languages', "I can understand and respond in English, but I can try to help with other languages too!"),
    (r'do you have a family', "I don't have a family, but I belong to a network of bots."),
    (r'what is the internet', "The internet is a global network of computers connected together."),
    (r'can you solve math problems', "Sure! Ask me a simple math problem."),
    (r'what is the time', "I'm not connected to a clock, but you can check your device!"),
    (r'what is love', "Love is a complex emotion that I can't fully understand."),
    (r'can you dance', "I don't have a body, so I can't dance."),
    (r'do you sleep', "No, I don't sleep. I'm always here to help."),
    (r'what is the best programming language', "Different languages are good for different things, but Python is very popular!"),
    (r'what is your favorite quote', "I think, therefore I am."),
    (r'tell me something interesting', "Did you know that octopuses have three hearts?"),
    (r'exit|quit', "Goodbye! Hope to chat with you again soon!")
]

def chatbot():
    print("Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()

        # Check if the user wants to exit
        if re.search(r'exit|quit', user_input):
            print("Chatbot: Goodbye! Hope to chat with you again soon!")
            break

        response_given = False
        # Check the input against the patterns
        for pattern, response in patterns_responses:
            if re.search(pattern, user_input):
                print(f"Chatbot: {response}")
                response_given = True
                break

        # Default response if no pattern matches
        if not response_given:
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")

if __name__ == "__main__":
    chatbot()
