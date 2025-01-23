import unittest

from src.LeafNode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_value(self):
        node = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph.</p>')

    def test_to_html_with_attributes(self):
        node = LeafNode(tag="a", value="Click here", attributes={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click here</a>')

    def test_to_html_without_tag(self):
        node = LeafNode(tag=None, value="Just text")
        self.assertEqual(node.to_html(), 'Just text')

    def test_to_html_without_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="p", value=None)
            node.to_html()

if __name__ == "__main__":
    unittest.main()