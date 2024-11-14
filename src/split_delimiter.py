from textnode import TextNode
from textnode import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []
    for node in old_nodes:
        current_text = node.text
        current_type = node.text_type
        if current_text == "":
            return [TextNode("", TextType.TEXT)]
        if current_type == TextType.TEXT: 
            start = 0
            while True:
                open_pos = current_text.find(delimiter, start)
                if open_pos == -1:
                    break
                if open_pos != 0:
                    split_nodes.append(TextNode(current_text[start:open_pos], TextType.TEXT))

                close_pos = current_text.find(delimiter, open_pos + len(delimiter))
                if close_pos == -1:
                    raise Exception("Invalid markdown. No closing delimiter found")
                split_nodes.append(TextNode(current_text[open_pos + len(delimiter):close_pos], text_type))

                start = close_pos + len(delimiter)
            if current_text[start:]:
                split_nodes.append(TextNode(current_text[start:], TextType.TEXT))
        else:
            split_nodes.append(TextNode(current_text, current_type))
    return split_nodes
    
