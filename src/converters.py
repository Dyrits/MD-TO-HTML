import re
from enum import Enum

from src.LeafNode import LeafNode
from src.TextNode import TextType, TextNode
from src.splitters import split_nodes_delimiter, split_nodes_images, split_nodes_link


class BlockType(Enum):
    Paragraph = "paragraph"
    Heading = "heading"
    Code = "code"
    Quote = "quote"
    UnorderedList = "unordered_list"
    OrderedList = "ordered_list"


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

def markdown_to_blocks(markdown):
    return [line for line in markdown.split("\n") if len(line) != 0]

def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.Heading
    if block.startswith("```") and block.endswith("```"):
        return BlockType.Code
    if block.startswith(">"):
        return BlockType.Quote
    if block.startswith("- ") or block.startswith("* "):
        return BlockType.UnorderedList
    if re.match(r"^\d+\.", block):
        return BlockType.OrderedList
    return "paragraph"