from textnode import TextType, TextNode

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




