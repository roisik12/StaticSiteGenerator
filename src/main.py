from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    dummy = TextNode("This is some text", TextType.LINK, "https://google.com")
    dummy2 = HTMLNode("h1","text inside a paragraph", [],{
    "href": "https://www.google.com",
    "target": "_blank",
})
    dummy3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(dummy3.to_html())
    print(dummy.__repr__())
    print(dummy2.props_to_html())
if __name__ == "__main__":
    main()