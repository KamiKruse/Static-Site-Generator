import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_one(self):
        node = HTMLNode('a', {"href":"www.google.com"})
        self.assertIsInstance(node.props, dict)
    
    def test_none(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})
    
    def test_values(self):
        node = HTMLNode(tag="a", props = {"href":"www.google.com"} )
        self.assertEqual(node.props["href"], "www.google.com")
    
    def test_props_to_html(self):
        node = HTMLNode(tag='a', props= {"href":"www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="www.google.com"')

    def test_multi_props(self):
         node = HTMLNode(tag='button', props={
             "for": "password", 
             "id": "password"
             })
         result_parts = set(node.props_to_html().strip().split())
         expected_parts = set(['for="password"', 'id="password"'])
         self.assertEqual(result_parts, expected_parts)

class TestLeafNode(unittest.TestCase):  
    def test_to_html(self):
        val = "Click me!"
        node = LeafNode(tag='button',value = val, props = { 
            "for": "password", 
            "id": "password"
            })
        expected_html = '<button for="password" id="password">Click me!</button>'
        self.assertEqual(set(node.to_html().split()), set(expected_html.split()))
    
    def test_leaf_node_no_value_provided(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag='a', value=None)
            node.to_html()

    def test_leaf_node_empty_string_values(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag='a', value='')
            node.to_html()
    
    def test_leaf_node_text_only(self):
        node = LeafNode(tag=None, value='This is supposed to be a link')
        self.assertEqual(node.to_html(), "This is supposed to be a link")

    def test_leaf_node_with_special_characters(self):
        node = LeafNode(tag=None, value='This is supposed to be a link')
        self.assertEqual(node.to_html(), "This is supposed to be a link")
   
class TestParentNode(unittest.TestCase):
    def test_one(self):
        node = ParentNode('p', [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ])
        assert node.to_html() == "<p><b>Bold text</b> Normal text <i>italic text</i> Normal text</p>"
    
    def test_nested_parent_node(self):
        parent = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "Paragraph text")
                    ],
                )
            ],
        )
        assert parent.to_html() == "<div><p>Paragraph text</p></div>"
    
    def test_parent_node_no_tag(self):
        with self.assertRaises(ValueError) as e:
            parent = ParentNode(None, [LeafNode("b", "Bold text")])
            parent.to_html()
        self.assertEqual(str(e.exception), "Parent nodes must have a tag")

    def test_parent_node_no_children(self):
        with self.assertRaises(ValueError) as e:
            parent = ParentNode("p", [])
            parent.to_html()
        self.assertEqual(str(e.exception), "No more children")
        
if __name__ == "main":
    unittest.main()
