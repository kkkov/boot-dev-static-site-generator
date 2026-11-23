from enum import Enum
from inline_markdown import text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node
import re

from htmlnode import HTMLNode

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        block = block.strip()
        if block != "":
            new_blocks.append(block)
    return new_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block: str) -> BlockType:
    lines = markdown_block.split("\n")
    if re.match("(^#{1,6} )", markdown_block):
        return BlockType.HEADING
    elif markdown_block.startswith("```\n") and markdown_block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{i}. ") for i,line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def block_type_to_html_node(block, block_type) -> HTMLNode:
    lines = block.split("\n")
    if block_type == BlockType.HEADING:
        level = len(block) - len(block.lstrip('#'))
        return HTMLNode(f"h{level}", text_to_children(block[level+1:])
    elif block_type == BlockType.CODE:
        code = [HTMLNode("code", block[4:-3] + "\n")]
        return HTMLNode("pre", code)
    elif block_type == BlockType.QUOTE:
        cleaned = [line.lstrip(">").strip() for line in lines]
        return HTMLNode("blockquote", " ".join(cleaned))
    elif block_type == BlockType.UNORDERED_LIST:
        li = [HTMLNode("li", line[2:]) for line in lines]
        return HTMLNode("ul", None, li)
    elif block_type == BlockType.ORDERED_LIST:
        li = [HTMLNode("li", line.split(". ", 1)[1]) for line in lines]
        return HTMLNode("ol", None, li)
    elif block_type == BlockType.PARAGRAPH:
        cleaned = block.replace("\n", " ")
        return HTMLNode("p", cleaned)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_nodes.append(block_type_to_html_node(block, block_type))
    
