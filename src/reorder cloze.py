import re
import pyperclip
import sys
from bs4 import BeautifulSoup


def renumber_cloze(html_text):
    # Find all cloze deletions
    cloze_pattern = re.compile(r"\{\{c(\d+)::(.*?)\}\}")
    matches = cloze_pattern.findall(html_text)

    # Create a mapping from old numbers to new numbers
    mapping = {old: str(new + 1) for new, (old, _) in enumerate(matches)}

    # Replace old numbers with new ones
    def replace_cloze(match):
        old_num, content = match.groups()
        return f"{{{{c{mapping[old_num]}::{content}}}}}"  # Preserve formatting

    updated_html = cloze_pattern.sub(replace_cloze, html_text)

    # Format the HTML
    soup = BeautifulSoup(updated_html, "html.parser")
    formatted_html = soup.prettify()

    # Copy to clipboard
    pyperclip.copy(formatted_html)
    print("Formatted HTML copied to clipboard successfully!")

    return formatted_html


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Read from a file if provided
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            html_input = file.read()
    else:
        # Read from standard input
        html_input = input("Enter HTML text: ")

    formatted_output = renumber_cloze(html_input)
    print(formatted_output)
