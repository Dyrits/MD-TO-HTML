import unittest

from extractors import extract_markdown_links, extract_markdown_images, extract_title


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is text with a [link to boot dev](https://www.boot.dev) and to [youtube](https://www.youtube.com)"
        expected_links = [("link to boot dev", "https://www.boot.dev"), ("youtube", "https://www.youtube.com")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected_links)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_images = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                           ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected_images)


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_success(self):
        self.title = "# This is a title"
        markdown = self.title
        expected = "This is a title"
        self.assertEqual(extract_title(markdown), expected)

    def test_extract_title_no_title(self):
        markdown = "This is not a title"
        with self.assertRaises(ValueError) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No title was found in the markdown.")


if __name__ == "__main__":
    unittest.main()
