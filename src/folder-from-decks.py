import os
import re
from collections import defaultdict


# Function to validate and extract the number-dot sequence
def is_valid_sequence(sequence):
    return bool(re.match(r"^(\d+\.)*\d+$", sequence))


# Function to remove the number, dash, and space from the start of each line
def clean_folder_name(line):
    # Pattern to match number(s) followed by space, dash, and space
    pattern = r"^\d+(-\d+)*\s-\s"
    match = re.match(pattern, line)
    if match:
        return line[match.end() :].strip()  # Remove matched part and strip extra spaces
    return line.strip()


# Function to extract and split the number-dot sequence from the line
def extract_sequence_and_name(line):
    try:
        sequence, name = line.split(" ", 1)
        if is_valid_sequence(sequence):
            return sequence.split("."), clean_folder_name(name)  # Clean the folder name
    except ValueError:
        return None, None
    return None, None


# Recursive function to build a tree
def add_to_tree(tree, seq_parts, folder_name):
    if len(seq_parts) == 1:  # Base case: we're at the final part of the sequence
        tree[seq_parts[0]] = {"name": folder_name, "children": {}}
    else:
        # Get the current level of the sequence
        current_level = seq_parts[0]
        if current_level not in tree:
            tree[current_level] = {"name": None, "children": {}}
        # Recursively add to the children of the current level
        add_to_tree(tree[current_level]["children"], seq_parts[1:], folder_name)


# Function to print the tree in a human-readable format
def print_tree(tree, indent=0, is_last=True):
    keys = sorted(tree.keys(), key=lambda x: int(x))  # Sort by sequence number
    for index, key in enumerate(keys):
        value = tree[key]
        prefix = "└── " if is_last and index == len(keys) - 1 else "├── "
        print("    " * indent + prefix + value["name"])
        # Recursively print children
        if value["children"]:
            print_tree(value["children"], indent + 1, is_last=(index == len(keys) - 1))


# Function to build the folder tree from the input list
def build_folder_tree(input_list):
    tree = defaultdict(dict)

    for line in input_list:
        seq_parts, folder_name = extract_sequence_and_name(line)
        if seq_parts and folder_name:
            add_to_tree(tree, seq_parts, folder_name)
        else:
            print(f"Skipping invalid line: {line}")

    return tree


# Function to read input from a text file
def read_input_from_file(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


# Recursive function to create directories based on the folder tree
def create_directories(base_path, tree):
    for key, value in sorted(tree.items(), key=lambda x: int(x[0])):
        folder_path = os.path.join(base_path, value["name"])
        if not os.path.exists(folder_path):
            print(f"Creating folder: {folder_path}")
            os.makedirs(folder_path)
        # Recursively create subdirectories
        if value["children"]:
            create_directories(folder_path, value["children"])


if __name__ == "__main__":
    # Example usage
    input_file = "D:\OneDrive - qerdp.co.uk\School work\GCE (General Certificate of Education)\Economics\economics subjects.txt"
    base_directory = (
        "D:\OneDrive - qerdp.co.uk\School work\GCE (General Certificate of Education)"
    )
    safe_mode = True  # Set to True to only print tree without creating directories
    input_list = read_input_from_file(input_file)
    folder_tree = build_folder_tree(input_list)

    # Print the tree
    print_tree(folder_tree)

    if not safe_mode:
        create_directories(base_directory, folder_tree)
    else:
        print("Safe Mode - No directories created.")
