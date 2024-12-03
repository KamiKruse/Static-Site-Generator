import unittest
from split_blocks import markdown_to_blocks

class TestSplitDelimiter(unittest.TestCase):
    def normal_markdown_text(self):
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

    def consecutive_blank_lines(self):
        text = """## Block One


        This is block two with consecutive blank lines above.
        """
        output = markdown_to_blocks(text)
        self.assertEqual(output, [
         "## Block One",
        "This is block two with consecutive blank lines above."
        ])
        
    def no_blank_lines(self):
        text = """A single block of text without any blank lines separating it.It should all be treated as one block despite the lack of newlines.
        """
        output = markdown_to_blocks(text)
        self.assertEqual(output, [
        "A single block of text without any blank lines separating it.\nIt should all be treated as one block despite the lack of newlines."
        ])

    def multiple_empty_lines_between(self):
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

if __name__ == "__main__":
    unittest.main()
