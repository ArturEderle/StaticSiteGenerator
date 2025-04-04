from public.src.htmlnode import LeafNode
from public.src.textnode import TextType

def text_node_to_html_node(node):
    match node.text_type:
        case TextType.BOLD:
            return LeafNode("b", node.text)
        case TextType.ITALIC:
            return LeafNode("i", node.text)
        case TextType.CODE:
            return LeafNode("code", node.text)
        case TextType.LINK:
            return LeafNode("a", node.text,{"href": ""})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": "", "alt": ""})
        case TextType.TEXT:
            return LeafNode(None, node.text)
    raise Exception("Unknown TextType")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # implement later
    raise NotImplementedError()
