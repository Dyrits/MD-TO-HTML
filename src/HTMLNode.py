# htmlnode.py

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, attributes=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.attributes = attributes if attributes is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")

    def attributes_to_html(self):
        return ''.join(f' {key}="{value}"' for key, value in self.attributes.items())

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.attributes == other.attributes and
            self.children == other.children
        )

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, attributes={self.attributes})"