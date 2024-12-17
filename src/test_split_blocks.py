import unittest
from split_blocks import markdown_to_blocks
from split_blocks import block_passing
from split_blocks import markdown_to_html_node

class TestSplitDelimiter(unittest.TestCase):
    def test_normal_markdown_text(self):
        text = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        output = markdown_to_blocks(text)
        self.assertEqual(output, [
        "# This is a heading",
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
        "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ])

    def test_consecutive_blank_lines(self):
        text = """## Block One


        This is block two with consecutive blank lines above.
        """
        output = markdown_to_blocks(text)
        self.assertEqual(output, [
         "## Block One",
        "This is block two with consecutive blank lines above."
        ])
        
    def test_no_blank_lines(self):
        text = """A single block of text without any blank lines separating it.It should all be treated as one block despite the lack of newlines.
        """
        output = markdown_to_blocks(text)
        self.assertEqual(output, [
        "A single block of text without any blank lines separating it.It should all be treated as one block despite the lack of newlines."
        ])

    def test_multiple_empty_lines_between(self):
        text = """### Heading



        Paragraph text.


        - Item 1
        - Item 2
        """
        output = markdown_to_blocks(text)
        self.assertEqual(output, [
        "### Heading",
        "Paragraph text.",
        "- Item 1\n- Item 2"
        ])

class TestBlockTypes(unittest.TestCase):
    def test_heading_code_unorderelist(self):
        test_list = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'paragraph', 'unordered list'])

    def test_heading_code_unorderelistInvalid(self):
        test_list = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        *This is a list item
        * This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'paragraph', 'Invalid markdown'])

    def test_heading_code_unorderelistInvalid1(self):
        test_list = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        - This is a list item
        * This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'paragraph', 'Invalid markdown'])

    def test_heading_code_unorderelistMinus(self):
        test_list = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        - This is the first list item in a list block
        - This is a list item
        - This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'paragraph', 'unordered list'])

    def test_headingInvalid_code_unorderelist(self):
        test_list = """#This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['Invalid markdown', 'paragraph', 'unordered list'])

    def test_headingInvalidHashCount_code_unorderelist(self):
        test_list = """####### This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['Invalid markdown', 'paragraph', 'unordered list'])

    def test_heading_codeTest_unorderelist(self):
        test_list = """# This is a heading

        ```This is a paragraph of text. It has some **bold** and *italic* words inside of it```

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'code', 'unordered list'])

    def test_heading_codeTestInvalid_unorderelist(self):
        test_list = """# This is a heading

        ```This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'Invalid markdown', 'unordered list'])

    def test_heading_codeTestInvalid_unorderelist(self):
        test_list = """# This is a heading

        ```This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'Invalid markdown', 'unordered list'])

    def test_heading_code_orderelist(self):
        test_list = """# This is a heading

        ```This is a paragraph of text. It has some **bold** and *italic* words inside of it```

        1. This is the first list item in a list block
        2. This is a list item
        3. This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'code', 'ordered list'])

    def test_heading_code_orderelistInvalid(self):
        test_list = """# This is a heading

        ```This is a paragraph of text. It has some **bold** and *italic* words inside of it```

        4. This is the first list item in a list block
        2. This is a list item
        3. This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'code', 'Invalid markdown'])

    def test_heading_code_orderelistInvalid1(self):
        test_list = """# This is a heading

        ```This is a paragraph of text. It has some **bold** and *italic* words inside of it```

        1 This is the first list item in a list block
        2. This is a list item
        3. This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'code', 'Invalid markdown'])

    def test_heading_code_orderelistInvalid2(self):
        test_list = """# This is a heading

        ```This is a paragraph of text. It has some **bold** and *italic* words inside of it```

        1.This is the first list item in a list block
        2. This is a list item
        3. This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'code', 'Invalid markdown'])

    def test_heading_code_orderelistInvalid3(self):
        test_list = """# This is a heading

        ```This is a paragraph of text. It has some **bold** and *italic* words inside of it```

        1. This is the first list item in a list block
        1. This is a list item
        3. This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'code', 'Invalid markdown'])

    def test_heading_code_orderelistInvalid4(self):
        test_list = """# This is a heading

        ```This is a paragraph of text. It has some **bold** and *italic* words inside of it```

        1. This is the first list item in a list block
        2.This is a list item
        3. This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'code', 'Invalid markdown'])

    def test_heading_quote_orderelist(self):
        test_list = """# This is a heading

        >This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        1. This is the first list item in a list block
        2. This is a list item
        3. This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['h1', 'quote', 'ordered list'])

    def test_all_paragraph(self):
        test_list = """This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        This is the first list item in a list block
        This is a list item
        This is another list item
        """
        output = markdown_to_blocks(test_list)
        block_types = block_passing(output)
        self.assertEqual(block_types, ['paragraph', 'paragraph', 'paragraph'])

class TestConvertNodes(unittest.TestCase):
    def test_code_markdowns(self):
        md = """
                ```This is another paragraph with *italic* text and `code` here```
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><pre><code>This is another paragraph with *italic* text and `code` here</code></pre></div>" )

    def test_ol_to_html(self):
        md = """
                1. This is an `ordered` list
                2. with items
                3. and more items
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ol><li>This is an  <code>ordered</code>  list</li> <li>with items</li> <li>and more items</li></ol></div>" )

    def test_ul_to_html(self):
        md = """
                - This is an `ordered` list
                - with items
                - and more items
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ul><li>This is an  <code>ordered</code>  list</li> <li>with items</li> <li>and more items</li></ul></div>" )

    def test_blockquote_to_html(self):
        md = """
                >This is an `ordered` list
                >with items
                >and more items
            """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><blockquote>This is an  <code>ordered</code>  list with items and more items</blockquote></div>" )
    
    def test_heading_to_html(self):
        md = """
                # This is a heading

                paragraph

                ## Another h2 heading
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>This is a heading</h1> <p>paragraph</p> <h2>Another h2 heading</h2></div>" )

if __name__ == "__main__":
    unittest.main()
