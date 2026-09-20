
import unittest
from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
