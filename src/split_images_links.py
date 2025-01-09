from textnode import TextNode,TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    split_nodes = []
    for node in old_nodes:
        current_text = node.text
        current_type = node.text_type
        if hasattr(node, 'url'):
           current_url = node.url
        if current_text == "":
            continue  
        if current_type == TextType.TEXT:
            image_split = extract_markdown_images(current_text)
            if len(image_split) == 1:
                start = 0
                image_index = 0
                while image_index < len(image_split):
                    open_pos = current_text.find(image_split[image_index][0], start)
                    if open_pos == -1:
                        break
                    text_to_append = current_text[start:open_pos-2]
                    if open_pos != 0 and text_to_append:
                        split_nodes.append(TextNode(current_text[start:open_pos-2], TextType.TEXT))
                    close_pos = open_pos + len(image_split[image_index][0]) + len(image_split[image_index][1]) + 3
                    split_nodes.append(TextNode(image_split[image_index][0], TextType.IMAGE, url=image_split[image_index][1]))
                    start = close_pos
                    image_index = image_index + 1
                if current_text[start:]:
                    split_nodes.append(TextNode(current_text[start:], TextType.TEXT))
            else:
                split_nodes.append(TextNode(image_split, TextType.TEXT))
        else:
            split_nodes.append(TextNode(current_text, current_type, current_url))
    return split_nodes
                
def split_nodes_links(old_nodes):
    split_nodes = [] 
    for node in old_nodes:
        current_text = node.text
        current_type = node.text_type 
        if hasattr(node, 'url'):
           current_url = node.url
        if current_text == "":
            continue
        if current_type == TextType.TEXT: 
            link_split = extract_markdown_links(current_text)
            if len(link_split) == 1:
                start = 0
                link_index = 0 
                while link_index < len(link_split):
                    open_pos = current_text.find(link_split[link_index][0], start)
                    if open_pos == -1:
                        break
                    text_to_append = current_text[start:open_pos-1]
                    if open_pos != 0 and text_to_append :
                        split_nodes.append(TextNode(current_text[start:open_pos-1], TextType.TEXT))
                    end_pos = open_pos + len(link_split[link_index][0]) + len(link_split[link_index][1]) + 3     
                    split_nodes.append(TextNode(link_split[link_index][0], TextType.LINK, url=link_split[link_index][1]))
                    start = end_pos
                    link_index = link_index + 1
                if current_text[start:]:
                    split_nodes.append(TextNode(current_text[start:], TextType.TEXT))
            else:
                split_nodes.append(TextNode(link_split, TextType.TEXT))
        else:
            split_nodes.append(TextNode(current_text, current_type, current_url))
    return split_nodes
