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
        if delimiter not in old_node:
            raise Exception("The markdown is not well formatted.")
        parts = old_node.split(delimiter)
        for index, part in enumerate(parts):
            if index % 2 == 0:
                nodes.append(TextNode(part, TextType.NORMAL))
            else:
                nodes.append(TextNode(part, text_type))
    return nodes