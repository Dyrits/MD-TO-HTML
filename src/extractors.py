import re


def extract_markdown_images(text):
    expression = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(expression, text)

def extract_markdown_links(text):
    expression = r"\[(.*?)\]\((.*?)\)"
    return re.findall(expression, text)