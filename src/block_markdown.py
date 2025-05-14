import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 0,
    HEADING = 1,
    CODE = 2,
    QUOTE = 3,
    UNORDERED_LIST = 4,
    ORDERED_LIST = 5

def markdown_to_blocks(markdown):
    blocks = [block.strip("\n") for block in markdown.split("\n\n") if block != ""]
    return blocks

def block_to_block_type(block):
    heading_pattern = r"^#{1,6} +\w"
    code_pattern = r"^```.*```$"
    quote_pattern = r"^>.*"
    unordered_pattern = r"^- .*"
    ordered_pattern = r"^\d+."

    if re.match(heading_pattern, block):
        return BlockType.HEADING
    elif re.match(code_pattern, block):
        return BlockType.CODE
    elif re.match(quote_pattern, block):
        return BlockType.QUOTE
    elif re.match(unordered_pattern, block):
        return BlockType.UNORDERED_LIST
    elif re.match(ordered_pattern, block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH