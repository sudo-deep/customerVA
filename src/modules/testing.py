import json
import pyttsx3
import speech_recognition as sr
import csv
from anytree import Node

class CustomerServiceNode(Node):
    def __init__(self, name, parent=None):
        super().__init__(name, parent=parent)

    def __call__(self):
        function_name = self.name.replace(" ", "_").lower() + "_function"
        if function_name in globals() and callable(globals()[function_name]):
            return globals()[function_name]()
        else:
            return "Invalid function."

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_user_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak:")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio).lower()
        print(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you. Please try again.")
        return get_user_input()
    except sr.RequestError:
        print("Sorry, there was an error accessing the Google Speech Recognition service.")
        return get_user_input()

def build_tree_from_json(tree_data, parent=None):
    node_name = tree_data["name"]
    node = CustomerServiceNode(node_name, parent=parent)

    for child_data in tree_data.get("children", []):
        build_tree_from_json(child_data, parent=node)

def create_ticket_function():
    speak("Please provide the ticket ID.")
    user_input = get_user_input()
    ticket_id = parse_ticket_id(user_input)

    if ticket_id:
        with open("tickets.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([ticket_id])
        speak("Ticket created successfully.")
    else:
        speak("Invalid ticket ID format. Please try again.")

def view_ticket_status_function():
    speak("Please provide the ticket ID.")
    user_input = get_user_input()
    ticket_id = parse_ticket_id(user_input)

    if ticket_id:
        with open("tickets.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == ticket_id:
                    speak(f"The status of ticket {ticket_id} is in progress.")
                    break
            else:
                speak(f"Ticket {ticket_id} not found.")
    else:
        speak("Invalid ticket ID format. Please try again.")

def quit_function():
    speak("Goodbye! Thank you for using our customer service.")
    exit()

def parse_ticket_id(user_input):
    # Custom logic to parse ticket ID from user input
    ticket_id = None
    # Add your logic here to extract ticket ID from various forms of user input
    # For simplicity, we assume the user input is the ticket ID itself
    ticket_id = user_input.strip()
    return ticket_id


if __name__ == "__main__":
    # Read the tree data from a JSON file
    with open("tree.json", "r") as file:
        tree_data = json.load(file)

    # Build the tree from JSON data
    customer_service_root = build_tree_from_json(tree_data)

    current_node = customer_service_root
    while True:
        speak(current_node.name)

        if not current_node.children:
            break

        user_input = get_user_input()
        if user_input == "go back":
            if current_node == customer_service_root:
                speak("You are already at the root.")
            else:
                current_node = current_node.parent
        else:
            found_child = None
            for child in current_node.children:
                if child.name.lower() in user_input:
                    found_child = child
                    break

            if found_child:
                current_node = found_child
            else:
                speak("Sorry, I didn't understand. Please try again.")
