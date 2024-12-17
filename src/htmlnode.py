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
        return " " + concatted
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}{self.value}{self.children}{self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
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
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children:  list['HTMLNode'] | None, props=None):
        if children is None or len(children) == 0:
            raise ValueError("No more children")
        super().__init__(tag, props, children = children)
    
    def to_html(self):
        if self.children is None or len(self.children) == 0:
            raise ValueError("No more children")
        if not self.tag:
            raise ValueError("Parent nodes must have a tag")
        results = " ".join(child.to_html() for child in self.children)
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{results}</{self.tag}>"
        return f"<{self.tag}>{results}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

