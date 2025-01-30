import re
from enum import Enum

from src.LeafNode import LeafNode
from src.TextNode import TextType, TextNode

def text_node_to_html_node(text_node):
    match text_node.type:
        case TextType.NORMAL:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, attributes={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", attributes={"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Invalid TextType")

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

def extract_markdown_images(text):
    expression = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(expression, text)

def extract_markdown_links(text):
    expression = r"\[(.*?)\]\((.*?)\)"
    return re.findall(expression, text)

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


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    # Split nodes by bold (**)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    # Split nodes by italic (*)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    # Split nodes by code (`)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    # Split nodes by images (![...](...))
    nodes = split_nodes_images(nodes)
    # Split nodes by links ([...](...))
    nodes = split_nodes_link(nodes)
    return nodes