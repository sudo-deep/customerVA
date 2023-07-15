from anytree import Node, RenderTree

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

def print_tree(root):
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name}")

# Main program
print("Build a tree using Anytree. Enter node names and their parent nodes.")
tree_root = build_tree()

print("\nTree structure:")
print_tree(tree_root)
