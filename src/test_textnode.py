import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is another text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.BOLD, url=None)
        self.assertEqual(node, node2)

    def test_text(self):
        node5 = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node5)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node6 = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node6)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")


    def test_links(self):
        node7 = TextNode("This is a link node", TextType.LINKS)
        html_node = text_node_to_html_node(node7)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")


    def test_text(self):
        node8 = TextNode("This is a non-existant image node", TextType.IMAGES, "~/Work/boot-dev/static-site-generator/img.jpeg")
        html_node = text_node_to_html_node(node8)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"~/Work/boot-dev/static-site-generator/img.jpeg": "This is a non-existant image node"})

if __name__ == "__main__":
    unittest.main()
