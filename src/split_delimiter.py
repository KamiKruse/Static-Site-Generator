from textnode import TextNode
from textnode import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []

    for node in old_nodes:
        current_text = node.text
        current_type = node.text_type
        current_url = None
        if hasattr(node, 'url'):
           current_url = node.url
        # if current_text == "":
        #     continue
        if current_type == TextType.TEXT and current_text != "": 
            start = 0
            while True:
                if delimiter:
                    open_pos = current_text.find(delimiter, start)
                else:
                    break
                if open_pos == -1:
                    break
                text_to_append = current_text[start:open_pos]
                if open_pos != 0 and text_to_append:
                    split_nodes.append(TextNode(text_to_append, TextType.TEXT))

                close_pos = current_text.find(delimiter, open_pos + len(delimiter))
                extracted_text_to_append = current_text[open_pos + len(delimiter):close_pos]
                if close_pos == -1:
                    raise Exception("Invalid markdown. No closing delimiter found")
                elif extracted_text_to_append:
                    split_nodes.append(TextNode(extracted_text_to_append, text_type))

                start = close_pos + len(delimiter)
            if current_text[start:]:
                split_nodes.append(TextNode(current_text[start:], TextType.TEXT))
        else:
            split_nodes.append(TextNode(current_text, current_type, current_url))
    return split_nodes
    
