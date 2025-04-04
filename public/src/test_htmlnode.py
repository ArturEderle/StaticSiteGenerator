import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "<p>",
            "some text",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        node2 = HTMLNode(
            "<p>",
            "some text",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_props_to_html(self):
        node = HTMLNode(
            "<p>",
            "some text",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_value_children(self):
        node = HTMLNode(
            "<p>",
            "some text",
        )
        node2 = HTMLNode(
            "<p>",
            None,
            "some child"
        )

        self.assertEqual(node.children is None, node.value is not None)
        self.assertEqual(node2.children is not None, node2.value is None)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_title(self):
        node = LeafNode("title", "Simple Title")
        self.assertEqual(node.to_html(), "<title>Simple Title</title>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html(self):
        node = LeafNode(None, "Hello, world!")
        node2 = LeafNode("p", None)
        self.assertEqual(node.to_html(), "Hello, world!")
        with self.assertRaises(ValueError) as no_value:
            node2.to_html()
        self.assertEqual(no_value.exception.__str__(), "leaf nodes must have a value")

    def test_parent_node_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()