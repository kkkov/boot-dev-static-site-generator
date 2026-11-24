from block_markdown import BlockType, markdown_to_blocks, block_to_block_type, markdown_to_html_node
import unittest

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_types(self):
        md2 = """
### Heading

> Quotations are great

```
SELECT * FROM orders;
```

- This is a line.
- Also a line.
- Third line in the block.

1. This
2. is
3. an ordered
4. list

And, finally, a normal paragraph.
"""
        blocks = markdown_to_blocks(md2)
        expected = [
            BlockType.HEADING,
            BlockType.QUOTE,
            BlockType.CODE,
            BlockType.UNORDERED_LIST,
            BlockType.ORDERED_LIST,
        ]
        for block, exp in zip(blocks, expected):
            self.assertEqual(block_to_block_type(block), exp)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()
