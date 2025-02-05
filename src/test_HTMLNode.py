import unittest

from HTMLNode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_attributes_to_html(self):
        node = HTMLNode(attributes={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.attributes_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_empty_attributes(self):
        node = HTMLNode()
        self.assertEqual(node.attributes_to_html(), '')

    def test_repr(self):
        node = HTMLNode(tag="a", value="Click here", attributes={"href": "https://www.google.com"})
        self.assertEqual(repr(node), 'HTMLNode(tag=a, value=Click here, children=[], attributes={\'href\': \'https://www.google.com\'})')

    def test_no_tag(self):
        node = HTMLNode(value="Just text")
        self.assertEqual(repr(node), 'HTMLNode(tag=None, value=Just text, children=[], attributes={})')

    def test_no_value(self):
        node = HTMLNode(tag="div", children=[HTMLNode(tag="p", value="Child text")])
        self.assertEqual(repr(node), 'HTMLNode(tag=div, value=None, children=[HTMLNode(tag=p, value=Child text, children=[], attributes={})], attributes={})')


if __name__ == "__main__":
    unittest.main()