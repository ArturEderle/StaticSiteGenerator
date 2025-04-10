from htmlnode import LeafNode
from textnode import TextType, TextNode
import re

def text_node_to_html_node(node):
    match node.text_type:
        case TextType.BOLD:
            return LeafNode("b", node.text)
        case TextType.ITALIC:
            return LeafNode("i", node.text)
        case TextType.CODE:
            return LeafNode("code", node.text)
        case TextType.LINK:
            props = "" if node.url is None else node.url
            return LeafNode("a", node.text,{"href": props})
        case TextType.IMAGE:
            url = "" if node.url is None else node.url
            props = "" if node.text is None else node.text
            return LeafNode("img", "", {"src": url, "alt": props})
        case TextType.TEXT:
            return LeafNode(None, node.text)
    raise Exception("Unknown TextType")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    #matches = re.findall(r"!\[(.*?)]\((.*?)\)", text)
    matches = re.findall(r"!\[([^\[\]]*)]\(([^()]*)\)", text)
    return matches

def extract_markdown_links(text):
    #matches = re.findall(r"\[(.*?)]\((.*?)\)", text)
    matches = re.findall(r"(?<!!)\[([^\[\]]*)]\(([^()]*)\)", text)
    return matches

def text_to_textnodes(text):
    text_nodes_with_types = []
    text_node = [TextNode(text, TextType.TEXT)]
    filtered_bold = split_nodes_delimiter(text_node, '**', TextType.BOLD)
    filtered_italic = split_nodes_delimiter(filtered_bold, '_', TextType.ITALIC)
    filtered_code = split_nodes_delimiter(filtered_italic, '`', TextType.CODE)
    filtered_image = split_nodes_image(filtered_code)
    filtered_link = split_nodes_link(filtered_image)
    text_nodes_with_types.extend(filtered_link)
    return text_nodes_with_types

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        old_node_text = old_node.text
        image_url_tuples_list = extract_markdown_images(old_node_text)
        if len(image_url_tuples_list) == 0:
            new_nodes.append(old_node)
            continue
        for img_url_tuple in image_url_tuples_list:
            parts = old_node_text.split(f"![{img_url_tuple[0]}]({img_url_tuple[1]})", 1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, formatted image not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(img_url_tuple[0], TextType.IMAGE, img_url_tuple[1]))
            old_node_text = parts[1]
        if old_node_text != "":
            new_nodes.append(TextNode(old_node_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        old_node_text = old_node.text
        alt_link_tuples_list = extract_markdown_links(old_node_text)
        if len(alt_link_tuples_list) == 0:
            new_nodes.append(old_node)
            continue
        for alt_link_tuple in alt_link_tuples_list:
            parts = old_node_text.split(f"[{alt_link_tuple[0]}]({alt_link_tuple[1]})", 1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, formatted link not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_link_tuple[0], TextType.LINK, alt_link_tuple[1]))
            old_node_text = parts[1]
        if old_node_text != "":
            new_nodes.append(TextNode(old_node_text, TextType.TEXT))
    return new_nodes
