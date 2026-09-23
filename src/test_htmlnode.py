
import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is example text", None,{"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "this is example text", None,{"href": "https://www.google.com"})
        node3 = HTMLNode("h1", "This is another text", None, None)
        node4 = HTMLNode("p", "this is example text", None,{"href": "https://www.google.com"})
        test_props = node.props_to_html()
        test_no_props = node3.props_to_html()
        self.assertEqual(test_props, ' href="https://www.google.com" target="_blank"')
        self.assertEqual(test_no_props, "")
        self.assertEqual(node3.tag, "h1")
        self.assertNotEqual(node3.value, "this is example text")
        self.assertIsNone(node3.children)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node2 = LeafNode('a', "Push the link!", {"href": "https://www.conscious-spending.vercel.app"})
        self.assertEqual(node2.to_html(), '<a href="https://www.conscious-spending.vercel.app">Push the link!</a>')
        
        node3 = LeafNode("a", None,{"href": "https://www.google.com", "target": "_blank"})
        with self.assertRaises(ValueError):
            node3.to_html()
        
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
