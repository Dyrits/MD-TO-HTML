import re

from src.TextNode import TextNode, TextType
from src.extractors import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for old_node in old_nodes:
        if old_node.type is not TextType.NORMAL:
            nodes.append(old_node)
            continue
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed.")
        for index, part in enumerate(parts):
            if index % 2 == 0:
                nodes.append(TextNode(part, TextType.NORMAL))
            else:
                nodes.append(TextNode(part, text_type))
    return nodes

def split_nodes_by_type(old_nodes, extract_function, text_type):
    nodes = []
    for old_node in old_nodes:
        items = extract_function(old_node.text)
        if not items:
            nodes.append(old_node)
            continue
        parts = re.split({TextType.LINK: r"(\[.*?\]\(.*?\))", TextType.IMAGE: r"(!\[.*?\]\(.*?\))"}[text_type], old_node.text)
        for part in parts:
            if part:  # Ensure part is not empty
                items = extract_function(part)
                if items:
                    for item_text, item_url in items:
                        nodes.append(TextNode(item_text, text_type, item_url))
                else:
                    nodes.append(TextNode(part, TextType.NORMAL))
    return nodes

def split_nodes_images(old_nodes):
    return split_nodes_by_type(old_nodes, extract_markdown_images, TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_nodes_by_type(old_nodes, extract_markdown_links, TextType.LINK)