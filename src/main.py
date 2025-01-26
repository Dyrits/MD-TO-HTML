from src.LeafNode import LeafNode
from src.TextNode import TextNode, TextType
from src.converters import text_node_to_html_node


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(text_node_to_html_node(node))

if __name__ == "__main__":
    main()