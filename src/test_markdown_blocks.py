from block_markdown import BlockType, markdown_to_blocks, block_to_block_type
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


if __name__ == "__main__":
    unittest.main()
