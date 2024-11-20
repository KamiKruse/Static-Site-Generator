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


test_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
# test_text1 = "This is *italic* with a **text** word and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
# test_text2 = "This is a [link](https://boot.dev) with an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a **text** word and a *italic*"
# test_text3 = ""
# test_text4 = "This is a [link](https://boot.dev) with an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a **text** word and a *italic*"
print(text_to_textnodes(test_text))
