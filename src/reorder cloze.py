import re
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

    return formatted_html


# Example usage
html_input = """
{{c4::Social::type}} causes of {{c5::geographic immovability}} are:<br>
<ol>
    <li>{{c8::Family ties}}</li>
    <li>{{c9::Language}} and {{c11::cultural barriers}}</li>
    <li>{{c9::Dislike of change}}&nbsp;</li>
</ol>
"""

formatted_output = renumber_cloze(html_input)
print(formatted_output)
