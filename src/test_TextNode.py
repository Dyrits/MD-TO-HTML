import unittest

from TextNode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        first = TextNode("This is a text node", TextType.BOLD)
        second = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(first, second)

    def test_neq_different_text(self):
        first = TextNode("This is a text node", TextType.BOLD)
        second = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(first, second)

    def test_neq_different_type(self):
        first = TextNode("This is a text node", TextType.BOLD)
        second = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(first, second)

    def test_str(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(str(node), "TextNode(This is a text node, TextType.BOLD, None)")

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(str(node), "TextNode(This is a text node, TextType.BOLD, None)")


if __name__ == "__main__":
    unittest.main()