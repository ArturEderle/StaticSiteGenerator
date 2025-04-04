from htmlnode import LeafNode
from textnode import TextType, TextNode


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
    if len(old_nodes) == 0:
        return []
    result = []
    old_node_split_list = list(map(lambda old_node: old_node.text.split(delimiter),old_nodes))
    for node_string_list in old_node_split_list:
        result.extend(
            [
                TextNode(node_string_list[0], TextType.TEXT),
                TextNode(node_string_list[1], text_type),
                TextNode(node_string_list[2], TextType.TEXT),
            ])
    return result
