from fuel import convert, gauge
import pytest


def test_empty():
    with pytest.raises(ValueError):
        convert()
