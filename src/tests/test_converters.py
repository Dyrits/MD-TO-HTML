import unittest

from src.TextNode import TextNode, TextType
from src.converters import text_node_to_html_node, split_nodes_delimiter, extract_markdown_links, \
    extract_markdown_images, split_nodes_link, split_nodes_images


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


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is text with a [link to boot dev](https://www.boot.dev) and to [youtube](https://www.youtube.com)"
        expected_links = [("link to boot dev", "https://www.boot.dev"), ("youtube", "https://www.youtube.com")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected_links)

    def test_extract_markdown_images(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        expected_images = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected_images)

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        expected_nodes = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        result = split_nodes_link([node])
        self.assertEqual(result, expected_nodes)

    def test_split_nodes_images(self):
        node = TextNode(
            'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)',
            TextType.NORMAL,
        )
        expected_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        result = split_nodes_images([node])
        self.assertEqual(result, expected_nodes)

if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()