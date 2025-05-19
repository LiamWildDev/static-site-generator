from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
import re

md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        print(block_type)
        match block_type:
            case BlockType.PARAGRAPH:
                nodes = text_to_textnodes(block)
                leaf_nodes = []
                for node in nodes:
                    leaf_node = text_node_to_html_node(node)
                    leaf_nodes.append(leaf_node)
                html_block_node = ParentNode("p", leaf_nodes, None)
                html_block_nodes.append(html_block_node)
            case BlockType.HEADING:
                nodes = text_to_textnodes(block)
                leaf_nodes = []
                tag = ""
                for node in nodes:
                    # If its the heading inline text node find out what type of heading it is
                    # and create the correct leaf node by deleting the number of '#'
                    heading = re.match(r"^#{1,6}", node.text)
                    if heading:
                        tag = "h" + str(len(heading.group(0)))
                        # I am slicing the text with the num of '#' + 1 because I know there is a space after the markdown heading symbol ('#')
                        node.text = node.text[len(heading.group(0)) + 1:]
                        # Capitalizing the first char
                        node.text = node.text[0].upper() + node.text[1:]
                        leaf_node = text_node_to_html_node(node)
                        leaf_nodes.append(leaf_node)
                        continue
                    #Convert the text_node to an html_node
                    leaf_node = text_node_to_html_node(node)
                    leaf_nodes.append(leaf_node)
                html_block_node = ParentNode(tag, leaf_nodes, None)
                html_block_nodes.append(html_block_node)
            case BlockType.CODE:
                print("code block was entered")
                nodes = text_to_textnodes(block)
                leaf_nodes = []
                for node in nodes:
                    leaf_node = text_node_to_html_node(node)
                    leaf_nodes.append(leaf_node)
                html_block_node = ParentNode("pre><code", leaf_nodes, None)
                html_block_nodes.append(html_block_node)
            case BlockType.QUOTE:
                return
            case BlockType.UNORDERED_LIST:
                return
            case BlockType.ORDERED_LIST:
                return
    body_node = ParentNode("div", html_block_nodes, None)
    print(body_node)
    return body_node
            
markdown_to_html_node(md)