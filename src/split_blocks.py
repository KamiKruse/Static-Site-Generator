from htmlnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    # Split text into lines
    lines = markdown.replace('\r\n', '\n').splitlines()

    # Group lines based on empty line breaks
    groups = []
    current_group = []

    for line in lines:
        line = line.strip('\ufeff').strip('\u200b')
        stripped_line = line.strip()
        if stripped_line:  # If the line is not empty
            current_group.append(stripped_line)
        else:  # If the line is empty, start a new group
            if current_group:
                groups.append("\n".join(current_group))
                current_group = []

    # Add the last group if any
    if current_group:
        groups.append("\n".join(current_group))

    return groups

def block_passing(groups):
    block_types = []
    for block in groups:
        val = block_to_block_type(block)
        block_types.append(val)
    return block_types
    

def block_to_block_type(block):
    if block.startswith('**') or block.startswith('![') or block.startswith('['):
        return "paragraph"
    
    if block[0] == '#':
        count = 0
        first_space = block.find(" ")
        for i in range(0, len(block)):
            if block[i] == '#' and i <=5:
                count += 1
            if block[i] == "#" and i > 5:
                return "Invalid markdown"
        if count == 1 and count == first_space:
            return "h1"
        if count == 2 and count == first_space:
            return "h2"
        if count == 3 and count == first_space:
            return "h3"
        if count == 4 and count == first_space:
            return "h4"
        if count == 5 and count == first_space:
            return "h5"
        if count == 6 and count == first_space:
            return "h6"
        return 'Invalid markdown'
    
    if block[0] == '*':
        if block[1] != " ":
            return "Invalid markdown"
        for i in range(0, len(block)):
            if block[i] == "\n":
                if block[i+1] != "*":
                    return "Invalid markdown"
                elif block[i+2] != " ":
                    return "Invalid markdown"
        return "unordered list"
    
    if block[0] == '-':
        if block[1] != " ":
            return "Invalid markdown"
        for i in range(0, len(block)):
            if block[i] == "\n":
                if block[i+1] != "-":
                    return "Invalid markdown"
                elif block[i+2] != " ":
                    return "Invalid markdown"
        return "unordered list"
    
    if block.startswith("```"):
        if block.count("\n") == 0 and block.endswith("```"):
            return "code"
        lines = block.split("\n")
        if len(lines) >= 2 and lines[-1].strip() == "```":
            return "code"
        return "Invalid markdown"

    if block[0] == ">":
        return "quote"
    
    if  block[0].isdigit():
        if block[0] != '1':
            return "Invalid markdown"
        if block[1] != ".":
            return "Invalid markdown"
        if block[2] != " ":
            return "Invalid markdown"
        val = int(block[0])
        for i in range(0, len(block)):
            if block[i] == "\n":
                val += 1
                try:
                    if int(block[i+1]) != val:
                        return "Invalid markdown"
                except ValueError:
                    return "Invalid markdown"
                if block[i+2] != ".":
                    return "Invalid markdown"
                if block[i+3] != " ":
                    return "Invalid markdown"
        return "ordered list"
                
    return "paragraph"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == "paragraph":
        return paragraph_to_html_node(block)
    if block_type == "code":
        return code_to_html_code(block)
    if block_type == "ordered list":
        return olist_to_html_code(block)
    if block_type == "unordered list":
        return ulist_to_html_code(block)
    if block_type == "quote":
        return quote_to_html_code(block)
    if block_type == "h1" or block_type == "h2" or block_type == "h3" or block_type == "h4" or block_type == "h5" or block_type == "h6":
        return heading_to_html_code(block_type, block)
    if block_type == "Invalid markdown":
        raise ValueError("Invalid block type")
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = TextNode.text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def forCode_text_to_children(text):
    text_nodes = [TextNode(text, TextType.TEXT, None)]
    children = []
    for text_node in text_nodes:
        html_node = TextNode.text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def code_to_html_code(block):
    text = block[3:-3].strip()
    new_text = ' '.join(text.split())
    children = forCode_text_to_children(new_text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def olist_to_html_code(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_code(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_code(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        text = line[1:].strip()
        new_lines.append(text)
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
       

def heading_to_html_code(block_type, block):
    text = block.lstrip("#").strip()
    children = text_to_children(text)
    return ParentNode(f"{block_type}", children)
