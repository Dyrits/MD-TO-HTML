import unittest

from TextNode import TextNode, TextType
from splitters import split_nodes_delimiter, split_nodes_link, split_nodes_images


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_bold_delimiter(self):
        old_nodes = [TextNode("This is **bold** text", TextType.NORMAL), TextNode("Another **bold** example", TextType.NORMAL)]
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
        old_nodes = [TextNode("This is *italic* text", TextType.NORMAL), TextNode("Another *italic* example", TextType.NORMAL)]
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

    def test_not_closed_delimiter(self):
        old_nodes = [TextNode("This is **bold text", TextType.NORMAL)]
        delimiter = "**"
        text_type = TextType.BOLD
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertTrue("Invalid markdown, formatted section not closed." in str(context.exception))

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