class HTMLNode:
    def __init__(self, tag: str =None, value: str =None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        
        result=f""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError()
        elif not self.tag:
            return str(self.value)
        else:
            if not self.props:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    


