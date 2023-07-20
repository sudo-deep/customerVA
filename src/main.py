'''
File: main.py
Author: Deepansh Goel
Created: 11-07-23
Last Modified: 20-07-23
Python version: 3.8

Description: Main running file for testing purposes currently
'''


from modules.audio_utils import audio_utils
from anytree import Node, RenderTree, RenderTreeGraph

class CustomerServiceNode:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        function_name = self.name.replace(" ", "_") + "_function"
        if function_name in globals() and callable(globals()[function_name]):
            return globals()[function_name]()
        else:
            return "Invalid function."    

def build_tree_from_json(tree_data):
    root = None
    nodes = {}

    def build_node(node_data):
        nonlocal root

        node_name = node_data["name"]

        node = CustomerServiceNode(node_name)
        nodes[node_name] = node

        if root is None:
            root = node
        else:
            parent_name = node_data["parent"]
            parent_node = nodes[parent_name]
            node.parent = parent_node

        for child_data in node_data.get("children", []):
            build_node(child_data)

    build_node(tree_data)
    return root

def print_tree(root):
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")

utils = audio_utils()

def speak(text):
    utils.play_audio(text)

def listen():
    resp = utils.get_speech()
    if resp == -1:
        speak("Service is unavailable, please try again later.")
    return resp


def w_function():
    speak("Welcome to the customer service.")
    speak("To create a ticket, select 1.")
    speak("To view ticket status, select 2.")
    speak("To repeat the options, select 3.")

# def create_function():



def display_menu():
    speak("Welcome to XYZ customer service.")
    speak("To open a ticket, select 1.")
    speak("To view ticket status, select 2.")
    speak("To repeat the options, select 3.")

