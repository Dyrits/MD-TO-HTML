import unittest
from src.ParentNode import ParentNode
from src.LeafNode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child1 = LeafNode(tag="p", value="Paragraph 1")
        child2 = LeafNode(tag="p", value="Paragraph 2")
        parent = ParentNode(tag="div", children=[child1, child2])
        self.assertEqual(parent.to_html(), '<div><p>Paragraph 1</p><p>Paragraph 2</p></div>')

    def test_to_html_with_attributes(self):
        child = LeafNode(tag="p", value="Paragraph")
        parent = ParentNode(tag="div", children=[child], attributes={"class": "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><p>Paragraph</p></div>')

    def test_to_html_without_tag(self):
        child = LeafNode(tag="p", value="Paragraph")
        with self.assertRaises(ValueError):
            parent = ParentNode(tag=None, children=[child])
            parent.to_html()

    def test_to_html_without_children(self):
        with self.assertRaises(ValueError):
            parent = ParentNode(tag="div", children=None)
            parent.to_html()

if __name__ == "__main__":
    unittest.main()