from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type: str, url=None):
        # try:
        #     self.text = text
        #     self.text_type = TextType(text_type).value
        #     self.url = url
        # except ValueError:
        #     raise ValueError(f"Invalid text type: {text_type}. Must be one of {[t.value for t in TextType]}")
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

