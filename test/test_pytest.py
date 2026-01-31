import pytest
from src.date_validator import is_valid_date, validate_date_range

def test_is_valid_date():
    assert is_valid_date("2026-01-31")
    assert is_valid_date("31-01-2026", "%d-%m-%Y")
    assert not is_valid_date("2026-02-30")
    assert not is_valid_date("abc")

def test_validate_date_range():
    valid, msg = validate_date_range("2026-01-31", start_date="2026-01-01", end_date="2026-12-31")
    assert valid
    assert msg == ""

    valid, msg = validate_date_range("2025-12-31", start_date="2026-01-01", end_date="2026-12-31")
    assert not valid
    assert "before start date" in msg

    valid, msg = validate_date_range("2027-01-01", start_date="2026-01-01", end_date="2026-12-31")
    assert not valid
    assert "after end date" in msg

    valid, msg = validate_date_range("2026-02-30", start_date="2026-01-01", end_date="2026-12-31")
    assert not valid
    assert "Invalid date format" in msg
