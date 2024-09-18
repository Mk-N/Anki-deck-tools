import re
import os


def process_text(input_path):
    with open(input_path, "r") as file:
        text = file.read()

    # Step 1: Remove trailing whitespace
    text = re.sub(r"\s$", "", text, flags=re.MULTILINE)

    # Step 2: Replace double spaces with single space
    text = re.sub(r"\s\s", " ", text)

    # Step 3: Replace double newlines with single newline
    text = re.sub(r"\n\n", "\n", text)

    # Step 4: Merge subheading number and deck name
    text = re.sub(r"([0-9]+)\n([a-zA-Z].*)", r"\1 \1 - \2", text)

    # Step 5: Remove any newlines at the end of the text
    text = text.rstrip("\n")
    return text


def prepend_text(text, text_to_prepend):
    new_text = ""
    lines = text.split("\n")

    for line in lines:
        new_text += text_to_prepend + line + "\n"
    return new_text.rstrip("\n")  # Remove the trailing newline


def get_unused_filename(directory, base_name, extension):
    i = 1
    while True:
        filename = f"{base_name}{i}.{extension}"
        if not os.path.exists(os.path.join(directory, filename)):
            return filename
        i += 1


def save_cleaned_decks(output_path, text):
    with open(output_path, "w") as file:
        file.write(text)


def output_decks_console(text):
    if "\n" in text:
        print("Here are the decks:")
    else:
        print("Here is the deck")
    print(f"{text}")


# Example usage
if __name__ == "__main__":
    input_path = "input/input.txt"
    output_directory = "output"
    text_to_prepend = "1.2."
    output_to_console = True

    # Text processing
    cleaned_text = process_text(input_path)
    cleaned_text = prepend_text(cleaned_text, text_to_prepend)

    # Get an unused output filename and path
    output_filename = get_unused_filename(output_directory, "output", "txt")
    output_path = os.path.join(output_directory, output_filename)

    # Save the file
    save_cleaned_decks(output_path, cleaned_text)

    # Output to console if required
    if output_to_console == True:
        output_decks_console(cleaned_text)
        print(f"Output path: {output_path}")
