from textnode import TextNode, TextType
from copy_files import prep_dest, copy_files
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def main():
    src_path = "static"
    dest_path = "public"
    prep_dest(dest_path)
    copy_files(src_path, dest_path)

main()
