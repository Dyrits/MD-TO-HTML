import unittest

from src.HTMLNode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(attributes={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_empty_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode(tag="a", value="Click here", attributes={"href": "https://www.google.com"})
        self.assertEqual(repr(node), 'HTMLNode(tag=a, value=Click here, children=[], attributes={\'href\': \'https://www.google.com\'})')

if __name__ == "__main__":
    unittest.main()