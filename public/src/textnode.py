from enum import Enum
from unittest import case

from public.src.htmlnode import LeafNode, HTMLNode


class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "`code`"
    LINK = "link"
    IMAGE = "image"
    TEXT = "text"

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

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
