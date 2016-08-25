import sys
import pytest
from unittest.mock import patch

@patch('builtins.input', lambda: '5')
def test_python_text_alignment():
    print('input: {}'.format(input()))
