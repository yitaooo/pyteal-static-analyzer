import argparse
from antlr4 import *
from antlr4.tree.Trees import Trees
from pyteal.PyTealLexer import PyTealLexer
from pyteal.PyTealParser import PyTealParser
from utils.mode import Mode
from detectors.abstarct_detector import DetectorType
from detectors.all_detectors import (
    UncheckedRekeyto,
    UncheckedDeletableApplication,
    UncheckedUpdatableApplication,
    CanCloseAccount,
    CanCloseAsset
    
)


def read_pyteal_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def choose_detector(detector_type):

    all_detectors = [
        UncheckedUpdatableApplication(),
        UncheckedDeletableApplication(),
        UncheckedRekeyto(),
        CanCloseAccount(),
        CanCloseAsset()
]
    
    selected_detectors = []

    selected_detectors = all_detectors

    if detector_type == "Stateful":
        selected_detectors = [detector for detector in selected_detectors if detector.TYPE == DetectorType.STATEFUL]
    elif detector_type == "Stateless":
        selected_detectors = [detector for detector in selected_detectors if detector.TYPE == DetectorType.STATELESS]

    return selected_detectors

def visitChildren(self, node):
        result = None
        for child in node.getChildren():
            child_result = child.accept(self)
            if child_result == "Mode.Signature":
                result = child_result
                break  
        return result

def run_detectors(detector_type, pyteal_file):

    results = []

    selected_detectors = choose_detector(detector_type)
    
    detector = selected_detectors
            

    for detector in selected_detectors:
        input_stream = FileStream(pyteal_file)
        lexer = PyTealLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PyTealParser(stream)
        tree = parser.file_input()
        walker = ParseTreeWalker()
        walker.walk(detector, tree)
            
        result = detector.detect(pyteal_file)
        results.append(result)
  
    return results


def main():
    parser = argparse.ArgumentParser(description="Static Analyzer for PyTeal")


    parser.add_argument("--pyteal-file", type=str, help="Path to PyTeal file")
    parser.add_argument("--generate-ast", action="store_true", help="Generate AST")

    args = parser.parse_args()
   

    pyteal_file = args.pyteal_file

    if pyteal_file is None:
        print("Please provide the path to the PyTeal file: --pyteal-file <file path>")
    else:
        if args.generate_ast:
            try:
                input_stream = FileStream(pyteal_file)
                lexer = PyTealLexer(input_stream)
                stream = CommonTokenStream(lexer)
                parser = PyTealParser(stream)
                tree = parser.file_input()
                print("PyTeal code successfully parsed!\n" + "-" * 60)
                tree_str = Trees.toStringTree(tree, None, parser)
                print(f"Here is the AST of your PyTeal contract: \n '{tree_str}'\n" + "-" * 60)
                mode_checker = Mode()
                walker = ParseTreeWalker()
                walker.walk(mode_checker, tree)
                detector_type = mode_checker.get_mode()
            except FileNotFoundError:
                print(f"File '{pyteal_file}' not found.")
                return None
            
        if pyteal_file is not None:
            
            results = run_detectors(detector_type, pyteal_file)

            for result in results:
                print(result)
        

if __name__ == "__main__":
    main()