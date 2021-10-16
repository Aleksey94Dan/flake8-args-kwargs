import ast
import sys
from typing import Any, Generator, List, Tuple, Type

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

AK001 = 'AK001 The function has more than 2 arguments.'
AK002 = 'AK002 The function contains a boolean variable'


class Visitor(ast.NodeVisitor):

    def __init__(self) -> None:
        self.errors: List[Tuple[int, int, str]] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:  # noqa: N802

        if len(node.args.args) > 2:
            self.errors.append((node.lineno, node.col_offset, AK001))

        for default in node.args.defaults:
            if isinstance(default, ast.Constant):
                if isinstance(default.value, bool):
                    self.errors.append(
                        (
                            default.lineno,
                            default.col_offset,
                            AK002,
                        ),
                    )
        self.generic_visit(node)


class Plugin(object):
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.errors:  # noqa: WPS526
            yield line, col, msg, type(self)
