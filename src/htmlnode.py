class HTMLNode:
    def __init__(self, tag: str =None, value: str =None, children: list[str]=None, props: dict[str,str]=None):
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

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag")
        elif not self.children:
            raise ValueError("Missing children")
        else:
            result = f"<{self.tag}{self.props_to_html()}>"
            for item in self.children:
                result += f"{item.to_html()}"
            result += f"</{self.tag}>"
            return result
