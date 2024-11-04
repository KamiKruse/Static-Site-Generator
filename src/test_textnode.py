import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        url = "https://www.google.com"
        node3 = TextNode("Sameple", TextType.ITALIC, url)
        self.assertEqual(node3.url, url)

    def test_url_none(self):
        node4 = TextNode("Sample", TextType.ITALIC )
        self.assertIsNone(node4.url)

    def test_type(self):
        # node5 = TextNode("Sample", TextType.CODE)
        # self.assertEqual(node5.text_type, TextType.CODE)
        # self.assertEqual(node5.text_type.value, 'code')
        # self.assertIsInstance(node5.text_type, TextType)
        node = TextNode("Sample", TextType.CODE)
    
    # Test that we get back the exact same enum object
        self.assertEqual(node.text_type, TextType.CODE)
    
    # Test that the enum value is 'code'
        self.assertEqual(node.text_type.value, 'code')
    
    # Test that the enum object is the correct type
        self.assertIsInstance(node.text_type, TextType)




if __name__ == "main":
    unittest.main()
