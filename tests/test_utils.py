import pytest
from app.utils import calculate_discount, get_tax, format_price


def test_calculate_discount():
    """Test that discount is subtracted from price"""
    result = calculate_discount(100, 10)
    assert result == 90, f"Expected 90, got {result}"


def test_get_tax():
    """Test that tax is calculated correctly"""
    result = get_tax(100)
    assert result == 18, f"Expected 18, got {result}"


def test_format_price_returns_int():
    """Test that format_price returns an integer"""
    result = format_price(19.99)
    assert isinstance(result, int), f"Expected int, got {type(result)}"
