from src.HTMLNode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, attributes=None):
        super().__init__(tag=tag, children=children, attributes=attributes)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if not self.children:
            raise ValueError("Parent nodes must have children")
        return f'<{self.tag}{self.attributes_to_html()}>{''.join(child.to_html() for child in self.children)}</{self.tag}>'