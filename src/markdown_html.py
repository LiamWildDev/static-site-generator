from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode

md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                node = HTMLNode("P", block)
                return
            case BlockType.HEADING:
                return
            case BlockType.CODE:
                return
            case BlockType.QUOTE:
                return
            case BlockType.UNORDERED_LIST:
                return
            case BlockType.ORDERED_LIST:
                return