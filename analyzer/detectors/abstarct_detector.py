import abc
from antlr4 import *

from pyteal.PyTealLexer import PyTealLexer
from pyteal.PyTealParser import PyTealParser
from pyteal.PyTealParserListener import PyTealParserListener

from exceptions import PyTealException

from utils.comparable_enum import ComparableEnum


#from tealer: tealer/detectors/abstract_detector.py
class IncorrectDetectorInitialization(Exception):
    """Exception class to represent incorrect detector intialization.

    This exception will be used if any of the necessary attributes of
    the AbstractDetector are not set by the inheriting detector class.
    """


class DetectorType(ComparableEnum):
    STATEFUL = 0
    STATELESS = 1
    UNDEFINED = 255


DETECTOR_TYPE_TXT = {
    DetectorType.STATELESS: "Stateless",
    DetectorType.STATEFUL: "Stateful",
    DetectorType.UNDEFINED: "Undefined",
}


class DetectorClassification(ComparableEnum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2
    INFORMATIONAL = 3
    OPTIMIZATION = 4

    UNIMPLEMENTED = 999

    def __str__(self) -> str:
        return self.name.title()


classification_txt = {
    DetectorClassification.OPTIMIZATION: "Optimization",
    DetectorClassification.INFORMATIONAL: "Informational",
    DetectorClassification.LOW: "Low",
    DetectorClassification.MEDIUM: "Medium",
    DetectorClassification.HIGH: "High",
}

class AbstractDetector(PyTealParserListener, metaclass=abc.ABCMeta):
    NAME = "" 
    DESCRIPTION = ""
    TYPE = DetectorType.UNDEFINED

    IMPACT: DetectorClassification = DetectorClassification.UNIMPLEMENTED
    CONFIDENCE: DetectorClassification = DetectorClassification.UNIMPLEMENTED

    "PyTeal transaction field expr"
    REKEY = PyTealParser.Pyteal_txn_rekey_to_exprContext
    ZEROADDR = PyTealParser.Pyteal_global_zero_address_exprContext
    CLOSEACCOUNT = PyTealParser.Pyteal_txn_close_remainder_to_exprContext
    CLOSEASSET = PyTealParser.Pyteal_txn_asset_close_to_exprContext

    "PyTeal transaction type"
    TYPEENUM = PyTealParser.Pyteal_txn_type_enum_exprContext
    PAYMENT = PyTealParser.Pyteal_txntype_Payment_exprContext
    AXFER = PyTealParser.Pyteal_txntype_AssetTransfer_exprContext

    @abc.abstractmethod
    def _check(self) -> bool:
        """Entry method of detector."""

    def detect(self,pyteal_file):
        try:
                input_stream = InputStream(pyteal_file)
                lexer = PyTealLexer(input_stream)
                tokens = CommonTokenStream(lexer)
                parser = PyTealParser(tokens)

                tree = parser.file_input()
                detector= self
                walker = ParseTreeWalker()
                walker.walk(detector, tree)
                detector= self
                if detector._check():
                    return "-" * 60 + f"\nPotential {self.NAME} vulnerability!\nDescription: {self.DESCRIPTION}\nImpact: {self.IMPACT}"

                return "-" * 60 + f"\nVulnerability {self.NAME} not detected."
        except PyTealException as e:
                return f"An error occurred: {str(e)}"

            
