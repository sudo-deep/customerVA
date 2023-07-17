'''
File: tree_builder.py
Author: Deepansh Goel
Created: 15-07-23
Last Modified: 17-07-23
Python version: 3.8

Description: Building a tree data structure for the application.
'''


import json
from anytree import Node, RenderTree
from anytree.exporter import DictExporter


FILE_PATH = "/home/deepansh/Documents/Python Personal/customerVA/data/tree_main.json"

def build_tree():
    root_name = input("Enter the name of the root node: ")
    root = Node(root_name)

    nodes = {root_name: root}  # Dictionary to store nodes by name for easy access

    while True:
        parent_name = input("Enter the name of the parent node (or 'q' to quit): ")
        if parent_name == 'q':
            break

        if parent_name not in nodes:
            print("Parent node not found. Please enter an existing node name.")
            continue

        child_name = input("Enter the name of the child node: ")
        if child_name in nodes:
            print("Node name already exists. Please enter a unique node name.")
            continue

        parent_node = nodes[parent_name]
        child_node = Node(child_name, parent=parent_node)
        nodes[child_name] = child_node

    return root

def export_tree(root):
    exporter = DictExporter()
    tree_dict = exporter.export(root)
    return tree_dict

def save_tree_to_file(tree_dict, filename):
    # filename = input("Enter the filename to save the tree (e.g., tree.json): ")
    with open(filename, 'w') as file:
        json.dump(tree_dict, file)
    print(f"Tree saved to {filename}.")

def print_tree(root):
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")

# Main program
print("Build a tree using Anytree. Enter node names and their parent nodes.")
tree_root = build_tree()

print("\nTree structure:")
print_tree(tree_root)

# Export and save the tree to a file
tree_dict = export_tree(tree_root)
save_tree_to_file(tree_dict, FILE_PATH)
