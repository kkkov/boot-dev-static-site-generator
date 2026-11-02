import re

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.IMAGES:
            new_nodes.append(node)
        elif (bool(isinstance(node.text, str) and node.text.strip())):
            raise Exception("Node has no text")


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:


