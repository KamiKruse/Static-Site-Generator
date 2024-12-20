import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_basic(self):
        node = TextNode("Hello `world` goodbye", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " goodbye")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_multi(self):
        node = TextNode("Hello `world` and `goodbye`", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "goodbye")
        self.assertEqual(nodes[3].text_type, TextType.CODE)
    
    def test_split_nodes_delimiter_no_delimits(self):
        node = TextNode("Hello world", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Hello world")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_missing_pair(self):
        node = TextNode("Hello `world goodbye", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)
    
    def test_split_nodes_delimiter_empty_string(self):
        node = TextNode("", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 1)

    def test_split_nodes_delimiter_non_text_type(self):
        node = TextNode("This is `code` text", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "This is `code` text")
        self.assertEqual(nodes[0].text_type, TextType.BOLD)
    
    def test_delimiter_at_start(self):
        node = TextNode("`code` text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "code")
        self.assertEqual(nodes[0].text_type, TextType.CODE)
        self.assertEqual(nodes[1].text, " text")
        self.assertEqual(nodes[1].text_type, TextType.TEXT)
    
    def test_multiple_delimiter_at_start(self):
        node = TextNode("`code1` regular text `code2`", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "code1")
        self.assertEqual(nodes[0].text_type, TextType.CODE)
        self.assertEqual(nodes[1].text, " regular text ")
        self.assertEqual(nodes[1].text_type, TextType.TEXT)
        self.assertEqual(nodes[2].text, "code2")
        self.assertEqual(nodes[2].text_type, TextType.CODE)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("Hello **world** goodbye", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " goodbye")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("Hello *world* goodbye", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text, " goodbye")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_split_nodes_empty_delimiter(self):
        node = TextNode("Hello world goodbye", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "", TextType.TEXT)
        print(len(nodes))
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Hello world goodbye")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()
