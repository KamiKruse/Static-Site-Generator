import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        url = "https://www.google.com"
        node = TextNode("Sample", TextType.ITALIC, url)
        self.assertEqual(node.url, url)

    def test_url_none(self):
        node = TextNode("Sample", TextType.ITALIC )
        self.assertIsNone(node.url)

    def test_type(self):
        node = TextNode("Sample", TextType.CODE)
        self.assertIs(node.text_type, TextType.CODE)
    
    def test_values(self):
        node = TextNode("Sample", TextType.CODE)
        self.assertEqual(node.text_type.value, "code")

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            TextNode("sample", "code")

if __name__ == "main":
    unittest.main()
