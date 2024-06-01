import sys

def create_anki_decks(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    deck_hierarchy = []
    current_path = []

    for index, line in enumerate(lines):
        # Split the line by tab and ensure there are at least two parts
        parts = line.strip().split('\t')
        if len(parts) < 2:
            raise ValueError(f"Error on line {index + 1}: does not have a tab to split into 2 parts.")

        level = parts[0].count('.')
        name = parts[1].strip()  # Removing quotes is no longer necessary

        # Adjust the current path based on the level
        if level < len(current_path):
            current_path = current_path[:level]

        current_path.append(name)
        deck_hierarchy.append('::'.join(current_path))

    return deck_hierarchy

if __name__ == "__main__":
    # run code in powershell in same directory as script in the most simple implementationas: python "Deck generator.py"
    # Default file paths
    input_file_path = 'raw deck names.txt'
    output_file_path = 'anki decks and subdeck names.txt'

    # Update file paths from command-line arguments if provided
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_file_path = sys.argv[2]

    try:
        decks = create_anki_decks(input_file_path)
        with open(output_file_path, 'w') as output_file:
            # Write each deck, adding a newline only if it's not the last deck
            for i, deck in enumerate(decks):
                if i < len(decks) - 1:
                    output_file.write(deck + '\n')
                else:
                    output_file.write(deck)
        print(f"Decks and subdecks have been successfully written to '{output_file_path}'")
    except ValueError as e:
        print(e)