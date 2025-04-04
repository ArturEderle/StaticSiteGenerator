
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        return " " + " ".join(list(map(lambda item: f"{item[0]}=\"{item[1]}\"" , self.props.items())))

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        print(self.children)
        if self.tag is None:
            raise ValueError("ParentNode.tag is None")
        if self.children is None:
            raise ValueError("ParentNode.children is None")
        children_leaf_nodes_string = "".join(list(map(lambda c: c.to_html(), self.children)))
        if self.props is None:
            return f"<{self.tag}>{children_leaf_nodes_string}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{children_leaf_nodes_string}</{self.tag}>"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf nodes must have a value")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

