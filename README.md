# Static Analyzer for PyTeal Smart Contracts
This tool is developed as part of a Bachelor's thesis research project of "Static Analysis of Algorand Smart Contracts". It is designed to perform static analysis on PyTeal smart contracts and automatically identify potential security vulnerabilities. The tool also provides a report detailing any detected issues, helping developers to improve their PyTeal smart contracts' safety.
### How to run the tool?

```
pip install -r requirements.txt
cd analyzer
python __main__.py --pyteal-file '<path_to_your_pyteal_file>' --generate-ast
```

## Detectors
Our tool supports five types of detectors, including:
| **Detectors**                     | **Contract Type** | **Impact** |
| --------------------------------- | ----------------- | ---------- |
| Unchecked Rekeyto                 | Stateless         | High       |
| Unchecked CloseRemainderto        | Stateless         | High       |
| Unchecked AssetCloseTo            | Stateless         | High       |
| Unprotected Deletable Application | Stateful          | High       |
| Unprotected Updatable Application | Stateful          | High       |

## Report
Our tool provides a vulnerability report with the AST of the code.
