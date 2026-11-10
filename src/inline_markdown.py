import re
from textnode import TextType, TextNode

def extract_markdown_images(text: str) -> list[tuple]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text: str) -> list[tuple]:
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        elif delimiter not in node.text:
            raise Exception("Specified delimiter not found in the body of text")
        else:
            prep_new = []
            prep_new = node.text.split(delimiter)
            if len(prep_new) % 2 == 0:
                raise Exception("Delimiter is present, yet wrongly used")
            counter = 0
            for i in prep_new:
                counter += 1
                if counter % 2 == 1:
                    if i == "":
                        continue
                    else:
                        new_nodes.append(TextNode(i, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(i, text_type))
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            elements = extract_markdown_images(node.text)
            if elements:
                text_to_process = node.text
                for e in elements:
                    helper = f"![{e[0]}]({e[1]})"
                    tmp = text_to_process.split(helper, 1)
                    if tmp[0] != "":
                        new_nodes.append(TextNode(tmp[0], TextType.TEXT))
                    new_nodes.append(TextNode(e[0], TextType.IMAGES, e[1]))
                    text_to_process = tmp[1]
                if text_to_process != "":
                    new_nodes.append(TextNode(text_to_process, TextType.TEXT))
            else:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            elements = extract_markdown_links(node.text)
            if elements:
                text_to_process = node.text
                for e in elements:
                    helper = f"[{e[0]}]({e[1]})"
                    tmp = text_to_process.split(helper, 1)
                    if tmp[0] != "":
                        new_nodes.append(TextNode(tmp[0], TextType.TEXT))
                    new_nodes.append(TextNode(e[0], TextType.LINKS, e[1]))
                    text_to_process = tmp[1]
                if text_to_process != "":
                    new_nodes.append(TextNode(text_to_process, TextType.TEXT))
            else:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
    return new_nodes


