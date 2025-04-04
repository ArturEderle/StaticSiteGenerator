import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", None)
        self.assertNotEqual(node.text_type, None)
        self.assertEqual(node2.text_type, None)
        self.assertEqual(isinstance(node.text_type, TextType), True)
        self.assertNotEqual(isinstance(node2.text_type, TextType), True)
        self.assertEqual(node.text_type, TextType.BOLD)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node.url, node2.url)
        self.assertEqual(node.url, None)
        self.assertNotEqual(node2.url, None)
        self.assertEqual(isinstance(node2.url, str), True)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>This is a bold text node</b>")

    def test_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.to_html(), "<i>This is a italic text node</i>")

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.to_html(), "<code>This is a code text node</code>")

    def test_link(self):
        node = TextNode("This is a link text node", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.to_html(), "<a href=\"\">This is a link text node</a>")

    def test_image(self):
        node = TextNode("url_to_image", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.to_html(), "<img src=\"\" alt=\"\"></img>")

if __name__ == "__main__":
    unittest.main()