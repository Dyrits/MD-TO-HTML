from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, type, url=None):
        self.text = text
        self.type = type
        self.url = url if type is TextType.LINK or type is TextType.IMAGE else None

    def __str__(self):
        return f"TextNode({self.text}, {self.type}, {self.url})"

    def __eq__(self, other):
        return self.text == other.text and self.type == other.type and self.url == other.url
