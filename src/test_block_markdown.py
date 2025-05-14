import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class test_markdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_line_markdown_to_blocks(self):
        md = "This is **bolded** line"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** line",
            ],
        )

    def test_no_markdown_to_blocks(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [],
        )

    def test_markdown_to_blocks_newline(self):
        md = """
This is **bolded** paragraph






This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        paragraph_block = "This is a paragraph block"
        heading_block = "### This is a heading block"
        code_block = "```This is a code block```"
        quote_block = ">This is a quote block"
        unordered_block = "- This is an unordered list block"
        ordered_block = """1. this is an ordered list block"""

        testing_paragraph = block_to_block_type(paragraph_block)
        testing_heading = block_to_block_type(heading_block)
        testing_code = block_to_block_type(code_block)
        testing_quote = block_to_block_type(quote_block)
        testing_unordered = block_to_block_type(unordered_block)
        testing_ordered = block_to_block_type(ordered_block)

        self.assertEqual(testing_paragraph, BlockType.PARAGRAPH)
        self.assertEqual(testing_heading, BlockType.HEADING)
        self.assertEqual(testing_code, BlockType.CODE)
        self.assertEqual(testing_quote, BlockType.QUOTE)
        self.assertEqual(testing_unordered, BlockType.UNORDERED_LIST)
        self.assertEqual(testing_ordered, BlockType.ORDERED_LIST)