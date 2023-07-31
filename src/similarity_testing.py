from modules import sen_similarity as ss
from modules import audio_utils

utils = audio_utils.audio_utils()

def speak(text):
    utils.play_audio(text)

def get_user_input():
    return utils.get_speech()

def get_response(question):
    responses = {
        "hello": "Hello! How can I assist you today?",
        "how are you": "I'm a computer program, but thanks for asking! How can I help?",
        "help": "Sure, I'm here to help. What do you need assistance with?",
        "bye": "Goodbye! Have a great day!",
    }
    promptlist = [i for i in responses]
    # print(ss.closest_attr(question, promptlist)[0])
    return responses.get(ss.closest_attr(question, promptlist)[1], "I'm sorry, I don't understand. Can you please rephrase your question?")


def main():
    speak("Welcome to the Customer Service Chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = get_user_input()
        response = get_response(user_input)
        if "Goodbye" in response:
            speak("goodbye")
            break
        
        
        speak(response)


if __name__ == "__main__":
    main()