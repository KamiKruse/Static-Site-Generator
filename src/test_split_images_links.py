import unittest
from split_images_links import split_nodes_links, split_nodes_image
from textnode import TextNode, TextType

class TestSplitImages(unittest.TestCase):
    # def test_split_nodes_links_basic(self):
    #     node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
    #     nodes = split_nodes_links([node])
    #     self.assertEqual(len(nodes), 4)
    #     self.assertEqual(nodes[0].text, "This is text with a link ")
    #     self.assertEqual(nodes[0].text_type, TextType.TEXT)
    #     self.assertEqual(nodes[1].text, "to boot dev")
    #     self.assertEqual(nodes[1].text_type, TextType.LINK)
    #     self.assertEqual(nodes[1].url, "https://www.boot.dev")
    #     self.assertEqual(nodes[2].text, " and ")
    #     self.assertEqual(nodes[2].text_type, TextType.TEXT)
    #     self.assertEqual(nodes[3].text, "to youtube")
    #     self.assertEqual(nodes[3].text_type, TextType.LINK)

    # def test_split_nodes_images_basic(self):
    #     node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",TextType.TEXT)
    #     nodes = split_nodes_image([node])
    #     self.assertEqual(len(nodes), 4)
    #     self.assertEqual(nodes[0].text, "This is text with a ")
    #     self.assertEqual(nodes[0].text_type, TextType.TEXT)
    #     self.assertEqual(nodes[1].text, "rick roll")
    #     self.assertEqual(nodes[1].text_type, TextType.IMAGE)
    #     self.assertEqual(nodes[1].url, "https://i.imgur.com/aKaOqIh.gif")
    #     self.assertEqual(nodes[2].text, " and ")
    #     self.assertEqual(nodes[2].text_type, TextType.TEXT)
    #     self.assertEqual(nodes[3].text, "obi wan")
    #     self.assertEqual(nodes[3].text_type, TextType.IMAGE)

    def test_split_nodes_images_only(self):
        node = TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif)",TextType.TEXT)
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "rick roll")
        self.assertEqual(nodes[0].text_type, TextType.IMAGE)

    def test_split_nodes_links_only(self):
        node = TextNode("[to boot dev](https://www.boot.dev)",TextType.TEXT)
        nodes = split_nodes_links([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "to boot dev")
        self.assertEqual(nodes[0].text_type, TextType.LINK)

    def test_split_nodes_links_only(self):
        node = TextNode("",TextType.TEXT)
        nodes = split_nodes_links([node])
        self.assertEqual(len(nodes), 0)

    def test_split_nodes_images_only(self):
        node = TextNode("",TextType.TEXT)
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 0)
        

if __name__ == "__main__":
    unittest.main()
