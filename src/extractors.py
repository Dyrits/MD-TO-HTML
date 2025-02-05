import re


def extract_markdown_images(text):
    expression = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(expression, text)

def extract_markdown_links(text):
    expression = r"\[(.*?)\]\((.*?)\)"
    return re.findall(expression, text)

def extract_title(markdown):
    expression = r"^# (.*)"
    match = re.match(expression, markdown)
    if not match:
        raise ValueError("No title was found in the markdown.")
    return match.group(1)