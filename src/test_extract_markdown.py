import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_basic_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertEqual(matches[0], ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'))
        self.assertEqual(matches[1], ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg'))

    def test_basic_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertEqual(matches[0], ('to boot dev', 'https://www.boot.dev'))
        self.assertEqual(matches[1], ('to youtube', 'https://www.youtube.com/@bootdotdev'))

    def test_empty_string_images(self):
            text = ""
            matches = extract_markdown_images(text)
            self.assertEqual(matches, "")

    def test_empty_string_links(self):
            text = ""
            matches = extract_markdown_links(text)
            self.assertEqual(matches, "")
    
    def test_no_images(self):
        text = "This is text with a  and "
        matches = extract_markdown_images(text)
        self.assertEqual(matches, "This is text with a  and ")

    def test_no_links(self):
        text = "This is text with a link  and "
        matches = extract_markdown_links(text)
        self.assertEqual(matches, "This is text with a link  and ")
    
    def test_incorrect_images(self):
        text = "This is text with a rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertEqual(matches[0], ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg'))
    
    def test_basic_links(self):
        text = "This is text with a link to boot dev(https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertEqual(matches[0], ('to youtube', 'https://www.youtube.com/@bootdotdev'))


if __name__ == "__main__":
    unittest.main()
