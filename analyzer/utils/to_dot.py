from graphviz import Digraph
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from pyteal.PyTealParser import PyTealParser  
from pyteal.PyTealParserListener import PyTealParserListener
from pyteal.PyTealLexer import PyTealLexer  
import sys


class TreeToDotListener(PyTealParserListener): 
    def __init__(self):
        super().__init__()
        self.dot = Digraph(comment='Parse Tree')

    def enterEveryRule(self, ctx):
        if isinstance(ctx, TerminalNodeImpl):
            token_text = ctx.getText()
            token_type = self.parser.symbolicNames[ctx.symbol.type]
            label = f"{token_type}\n{token_text}"
            self.dot.node(str(id(ctx)), label)
        else:
            self.dot.node(str(id(ctx)), ctx.__class__.__name__)
            if ctx.parentCtx:
                self.dot.edge(str(id(ctx.parentCtx)), str(id(ctx)))

    def get_dot(self):
        return self.dot

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = PyTealLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PyTealParser(stream)
    tree = parser.file_input()
    dot = Digraph(comment='Parse Tree')

    def remove_whitespace_nodes(node):
        if isinstance(node, TerminalNodeImpl):
            token_text = node.symbol.text
            if not token_text.strip():  
                parent = node.parentCtx
                if parent:
                    parent.removeLastChild()  
        else:
            for child in node.children:
                remove_whitespace_nodes(child)

    remove_whitespace_nodes(tree)

    dot = Digraph(comment='Parse Tree')

    def get_terminal_label(node):
        token_text = node.symbol.text
        if token_text == "<EOF>":
            return "EOF"
        elif token_text == "\n":
            return "NEWLINE"
        return token_text

    def traverse_tree(node):
        if isinstance(node, TerminalNodeImpl):
            token_text = node.symbol.text
            if token_text.strip():
                label = get_terminal_label(node)
                dot.node(str(id(node)), label)
        else:
            class_name = node.__class__.__name__
            if "Context" in class_name and class_name != "EOFContext":
                label = class_name.replace("Context", "")
                dot.node(str(id(node)), label)
                for child in node.children:
                    if not isinstance(child, TerminalNodeImpl) or child.symbol.text.strip():
                        dot.edge(str(id(node)), str(id(child)))
                    traverse_tree(child)

    traverse_tree(tree)
    dot.render('parse_tree', format='png', cleanup=True)
    listener = TreeToDotListener()  
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    dot_content = listener.get_dot() 

    with open('parse_tree.dot', 'w') as dot_file:
        dot_file.write(str(dot_content))  

if __name__ == '__main__':
    main(sys.argv)
