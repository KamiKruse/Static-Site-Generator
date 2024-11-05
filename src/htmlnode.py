class HTMLNode:
    def __init__(self, tag = None, value = None, children : list['HTMLNode'] | None = None, props = None):
        self.tag = tag
        self.value = value
        self.children : list['HTMLNode'] = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_list = []
        for key, value in self.props.items():
            props_list.append(f'{key}="{value}"')
        concatted = " ".join(props_list)
        return  " " + concatted
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}{self.value}{self.children}{self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children : list['HTMLNode'] | None = None, props=None):
        all_props = {}
        if props is not None:
            all_props.update(props)
        super().__init__(tag, value, props=all_props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have values")
        if self.tag is None:
            return self.value
        if self.props is not None:
            propped = self.props_to_html()
            return f"<{self.tag}{propped}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, value=None, children: list[HTMLNode] | None = None, props=None):
        super().__init__(tag, value, children, props)
