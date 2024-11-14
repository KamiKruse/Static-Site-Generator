from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGE = "images"

class TextNode:
    def __init__(self, text, text_type: str, url=None): 
        if not isinstance(text_type, TextType):
            raise ValueError("text type must be a TextType enum")
        self.text = text
        self._text_type = text_type
        self.url = url
    
    @property
    def text_type(self):
        return self._text_type

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.name}, {self.url})"
    

    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(tag=None, value=self.text)
            case TextType.BOLD:
                return LeafNode(tag='b', value=self.text)
            case TextType.ITALIC:
                return LeafNode(tag='i', value=self.text)
            case TextType.CODE:
                return LeafNode(tag='code', value=self.text)
            case TextType.LINK:
                return LeafNode(tag='a', value=self.text, props={"href":f"{self.url}"})
            case TextType.IMAGE:
                return LeafNode(tag='img', value=" ", props={
                    "src":f"{self.url}",
                    "alt":f"{self.text}"
                })
            case _:
                raise Exception("TextNode is none of these types")
            
            

   

