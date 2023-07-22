import json
import pyttsx3
import speech_recognition as sr
import csv
from anytree import Node, RenderTree, search
from anytree.importer import DictImporter
from anytree.exporter import DictExporter


def speak(text):
    # engine = pyttsx3.init()
    # engine.say(text)
    # engine.runAndWait()
    print(text)

def get_user_input():
    # recognizer = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Please speak:")
    #     recognizer.pause_threshold = 1
    #     audio = recognizer.listen(source)

    # try:
    #     user_input = recognizer.recognize_google(audio).lower()
    #     print(f"You said: {user_input}")
    #     return user_input
    # except sr.UnknownValueError:
    #     print("Sorry, I couldn't understand you. Please try again.")
    #     return get_user_input()
    # except sr.RequestError:
    #     print("Sorry, there was an error accessing the Google Speech Recognition service.")
    #     return get_user_input()
    return input()


def build_tree_from_json(json_data):
    importer = DictImporter(nodecls=Node)
    customer_service_root = importer.import_(json_data)
    return customer_service_root

def export_tree_to_json(root_node):
    exporter = DictExporter()
    json_data = exporter.export(root_node)
    return json_data

def w_function():
    speak("Welcome to the customer service")

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
    print(RenderTree(current_node))
    next_node = customer_service_root
    while True:
        globals()[next_node.name + "_function"]()
        print(f"\nCurrent Node: {current_node.name}")
        print("Choose the next node (or 'exit' to quit):")
        print(f"Children of {current_node.name}: {[child.name for child in current_node.children]}")
        next_node_value = input().strip()

        if next_node_value == 'exit':
            break
        temp = search.find_by_attr(current_node, next_node_value)
        # print(f"temp {temp}")
        next_node = temp
        
        if next_node is None:
            print("Node not found. Please try again.")
            continue
        elif next_node.is_leaf:
            print("You have reached the end of the customer service. Thanks for contacting")
            quit()