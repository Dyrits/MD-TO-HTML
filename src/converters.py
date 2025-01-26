from src.LeafNode import LeafNode
from src.TextNode import TextType


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