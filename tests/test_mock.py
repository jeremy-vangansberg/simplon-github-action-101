# test_my_module.py
import pytest
from unittest.mock import patch
from source import mock_demo

def test_f2_with_fixed_f1():
    with patch('source.mock_demo.f1', return_value=52) as mock_f1:
        # f1 est mockée pour retourner 5, donc f2 devrait retourner 5 * 10 = 50
        assert mock_demo.f2() == 50
        mock_f1.assert_called_once()
