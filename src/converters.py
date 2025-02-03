import re
from enum import Enum

from src.HTMLNode import HTMLNode
from src.LeafNode import LeafNode
from src.ParentNode import ParentNode
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
    return BlockType.Paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent = ParentNode(tag="div", children=[])
    unordered_list = None
    ordered_list = None

    for i, block in enumerate(blocks):
        block_type = block_to_block_type(block)

        if block_type != BlockType.UnorderedList and unordered_list is not None:
            parent.children.append(unordered_list)
            unordered_list = None

        if block_type != BlockType.OrderedList and ordered_list is not None:
            parent.children.append(ordered_list)
            ordered_list = None

        match block_type:
            case BlockType.Heading:
                level = block.count("#")
                text = block[level:].strip()
                parent.children.append(LeafNode(tag=f"h{level}", value=text))
            case BlockType.Code:
                text = block[3:-3]
                parent.children.append(ParentNode(tag="pre", children=[LeafNode(tag="code", value=text)]))
            case BlockType.Quote:
                text = block[1:].strip()
                parent.children.append(LeafNode(tag="blockquote", value=text))
            case BlockType.UnorderedList:
                if unordered_list is None:
                    unordered_list = ParentNode(tag="ul", children=[])
                text = block[2:].strip()
                unordered_list.children.append(LeafNode(tag="li", value=text))
            case BlockType.OrderedList:
                if ordered_list is None:
                    ordered_list = ParentNode(tag="ol", children=[])
                text = block[2:].strip()
                ordered_list.children.append(LeafNode(tag="li", value=text))
            case BlockType.Paragraph:
                text_nodes = text_to_textnodes(block)
                parent.children.append(ParentNode(tag="p", children=[text_node_to_html_node(node) for node in text_nodes]))
            case _:
                raise ValueError(f"The block type is invalid: {block_type}")

    # Append any remaining lists at the end
    if unordered_list is not None:
        parent.children.append(unordered_list)

    if ordered_list is not None:
        parent.children.append(ordered_list)

    return parent
