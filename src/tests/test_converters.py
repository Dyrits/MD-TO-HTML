import unittest

from src.TextNode import TextNode, TextType
from src.converters import text_node_to_html_node, text_to_textnodes, markdown_to_blocks, block_to_block_type, BlockType


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


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected_nodes)

    def test_text_to_textnodes_no_formatting(self):
        text = "This is text with no formatting"
        expected_nodes = [TextNode("This is text with no formatting", TextType.NORMAL)]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected_nodes)

    def test_text_to_textnodes_no_formatting_with_link(self):
        text = "This is text with a [link](https://boot.dev)"
        expected_nodes = [TextNode("This is text with a ", TextType.NORMAL), TextNode("link", TextType.LINK, "https://boot.dev")]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected_nodes)

    def test_text_to_textnodes_no_formatting_with_image(self):
        text = "This is text with an ![image](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_nodes = [TextNode("This is text with an ", TextType.NORMAL), TextNode("image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected_nodes)

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = ("# This is a heading" "\n"
                    "This is a paragraph of text. It has some **bold** and *italic* words inside of it." "\n"
                    "* This is the first list item in a list block" "\n"
                    "* This is a list item" "\n"
                    "* This is another list item")

        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block",
            "* This is a list item",
            "* This is another list item"
        ]

        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected_blocks)


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.Heading)

    def test_code_block(self):
        block = "```let x = 5;```"
        self.assertEqual(block_to_block_type(block), BlockType.Code)

    def test_quote_block(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.Quote)

    def test_unordered_list_block(self):
        block = "* This is an unordered list item"
        self.assertEqual(block_to_block_type(block), BlockType.UnorderedList)

    def test_ordered_list_block(self):
        block = "5. This is an ordered list item"
        self.assertEqual(block_to_block_type(block), BlockType.OrderedList)

    def test_paragraph_block(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), "paragraph")

if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()