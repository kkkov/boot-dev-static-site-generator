import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestTextNodeDelimiter(unittest.TestCase):
    def test_delimiter(self):
        node = TextNode("This is simply a text node", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

        node2 = TextNode("This is a **bold text** node", TextType.TEXT)
        node2_delimited = split_nodes_delimiter([node2], "**", TextType.BOLD)
        self.assertEqual(
            node2_delimited,
                [
                    TextNode("This is a ", TextType.TEXT),
                    TextNode("bold text", TextType.BOLD),
                    TextNode(" node", TextType.TEXT),
                ],
        )
        node3 = TextNode("This is an _italic text_ node", TextType.TEXT)
        node3_delimited = split_nodes_delimiter([node3], "_", TextType.ITALIC)
        self.assertEqual(
            node3_delimited,
                [
                    TextNode("This is an ", TextType.TEXT),
                    TextNode("italic text", TextType.ITALIC),
                    TextNode(" node", TextType.TEXT),
                ],
        )



