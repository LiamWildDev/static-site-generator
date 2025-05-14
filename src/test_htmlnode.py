import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_tag(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.tag, "p")
    
    def test_value(self):
        node = HTMLNode(value="This is an HTML node")
        self.assertEqual(node.value, "This is an HTML node")

    def test_children(self):
        obj1 = HTMLNode()
        obj2 = HTMLNode()
        obj3 = HTMLNode()
        html_objs = [obj1, obj2, obj3]
        node = HTMLNode(children=html_objs)
        self.assertEqual(node.children, html_objs)

    def test_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props, {"href": "https://www.google.com", "target": "_blank"})
    
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')
    
    def test_default(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_props_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click me!</a>')

    def test_leaf_raw_text_to_html(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_parent_with_children_to_html(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_with_grandchildren_to_html(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )    

    def test_parent_with_no_children_to_html(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError) as assert_error:
            parent_node.to_html()
        self.assertEqual(assert_error.exception.args[0], "children must not be empty")
    
    def test_parent_with_multiple_children_to_html(self):
        child_node1 = LeafNode("p", "This is the first child node")
        child_node2 = LeafNode("b", "This is bold text")
        child_node3 = LeafNode("i", "This is italic text")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><p>This is the first child node</p><b>This is bold text</b><i>This is italic text</i></div>")

    

if __name__ == "__main__":
    unittest.main()