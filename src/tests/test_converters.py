import unittest

from src.TextNode import TextNode, TextType
from src.converters import text_node_to_html_node, split_nodes_delimiter


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_normal_text(self):
        text_node = TextNode("Normal text", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Normal text")

    def test_bold_text(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_italic_text(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_code_text(self):
        text_node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")

    def test_link_text(self):
        text_node = TextNode("Link text", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.example.com">Link text</a>')

    def test_image_text(self):
        text_node = TextNode("Image text", TextType.IMAGE, "https://www.example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.example.com/image.png" alt="Image text"></img>')

    def test_invalid_text_type(self):
        text_node = TextNode("Invalid text", "INVALID")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_bold_delimiter(self):
        old_nodes = ["This is **bold** text", "Another **bold** example"]
        delimiter = "**"
        text_type = TextType.BOLD
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL),
            TextNode("Another ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" example", TextType.NORMAL)
        ]
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(result, expected_nodes)

    def test_split_nodes_italic_delimiter(self):
        old_nodes = ["This is *italic* text", "Another *italic* example"]
        delimiter = "*"
        text_type = TextType.ITALIC
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.NORMAL),
            TextNode("Another ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" example", TextType.NORMAL)
        ]
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(result, expected_nodes)

    def test_no_delimiter(self):
        old_nodes = ["This is normal text"]
        delimiter = "**"
        text_type = TextType.BOLD
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertTrue("The markdown is not well formatted." in str(context.exception))

if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()