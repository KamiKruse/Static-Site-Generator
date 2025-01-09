from split_delimiter import split_nodes_delimiter
from split_images_links import split_nodes_image, split_nodes_links
from textnode import TextNode, TextType

def text_to_textnodes(text):
    raw_text = text
    text_type = TextType.TEXT 
    node = [TextNode(raw_text, text_type, None)]
    link_split =split_nodes_links(split_nodes_image(node))
    bold_split = split_nodes_delimiter(link_split, "**", TextType.BOLD)
    italic_split = split_nodes_delimiter(bold_split, "*", TextType.ITALIC)
    final_split = split_nodes_delimiter(italic_split, "`", TextType.CODE)
    return final_split


