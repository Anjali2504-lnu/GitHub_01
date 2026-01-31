import unittest
from src.date_validator import is_valid_date, validate_date_range

class TestDateValidator(unittest.TestCase):

    def test_is_valid_date(self):
        self.assertTrue(is_valid_date("2026-01-31"))
        self.assertTrue(is_valid_date("31-01-2026", "%d-%m-%Y"))
        self.assertFalse(is_valid_date("2026-02-30"))
        self.assertFalse(is_valid_date("abc"))

    def test_validate_date_range_valid(self):
        valid, msg = validate_date_range("2026-01-31", start_date="2026-01-01", end_date="2026-12-31")
        self.assertTrue(valid)
        self.assertEqual(msg, "")

    def test_validate_date_range_before(self):
        valid, msg = validate_date_range("2025-12-31", start_date="2026-01-01", end_date="2026-12-31")
        self.assertFalse(valid)
        self.assertIn("before start date", msg)

    def test_validate_date_range_after(self):
        valid, msg = validate_date_range("2027-01-01", start_date="2026-01-01", end_date="2026-12-31")
        self.assertFalse(valid)
        self.assertIn("after end date", msg)

    def test_validate_date_range_invalid(self):
        valid, msg = validate_date_range("2026-02-30", start_date="2026-01-01", end_date="2026-12-31")
        self.assertFalse(valid)
        self.assertIn("Invalid date format", msg)

if __name__ == "__main__":
    unittest.main()
