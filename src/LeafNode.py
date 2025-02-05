from HTMLNode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, attributes=None):
        super().__init__(tag, value, attributes=attributes)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.attributes_to_html()}>{self.value}</{self.tag}>" 