from enum import Enum
from constants import *
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def is_block(pattern, markdown_block):
    match = re.match(pattern, markdown_block, re.DOTALL)
    return match

def block_to_block_type(markdown_block):
    if is_block(MD_HEADING_PATTERN, markdown_block):
        return BlockType.HEADING
    if is_block(MD_CODE_PATTERN, markdown_block):
        return BlockType.CODE
    if is_block(MD_QUOTE_PATTERN, markdown_block):
        return BlockType.QUOTE
    if is_block(MD_UNORDERED_LIST_PATTERN, markdown_block):
        return BlockType.UNORDERED_LIST
    if is_block(MD_ORDERED_LIST_PATTERN, markdown_block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

# tried my best here
def markdown_to_blocks(markdown):
    result = []
    blocks_list = list(map(lambda block: block.strip() , markdown.split("\n")))
    # if block_tracker == 1 -> open block and block_tracker == 2 -> block closed
    block_tracker = 0
    # save paragraph
    paragraph = ""
    # parts of paragraph counter
    parts_c = 0
    for paragraph_part in blocks_list:
        if len(paragraph_part) == 0:
            block_tracker += 1
            parts_c = 0
            if block_tracker == 2:
                result.append(paragraph)
                paragraph = ""
                block_tracker = 1
            continue
        if parts_c >= 1:
            paragraph += '\n' + paragraph_part
        else:
            paragraph += paragraph_part
        parts_c += 1
    return result
