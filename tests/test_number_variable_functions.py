import ast
from typing import Set

import pytest
from flake8_args_kwargs import Plugin

function_with_two_arguments = """
def foo(a, b):
    pass
"""

function_with_three_arguments = """
def foo(a, b, c):
    pass
"""

function_with_logical_arguments = """
def foo(a, b=True):
    pass
"""


def get_message(string: str) -> Set[str]:
    return {
        '{0}:{1}: {2}'.format(*res) for res in Plugin(ast.parse(string)).run()
    }


@pytest.mark.parametrize(
    'case, expected',
    [
        (
            function_with_two_arguments, set(),
        ),
        (
            function_with_three_arguments,
            {'2:0: AK001 The function has more than 2 arguments.'},
        ),
        (
            function_with_logical_arguments,
            {'2:13: AK002 The function contains a boolean variable'},
        ),
    ],
)
def test_case(case, expected):

    actually = get_message(case)  # act

    assert actually == expected
