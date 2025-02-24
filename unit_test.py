import unittest

from app import app


class TestPlus(unittest.TestCase):
    def test_plus_valid_numbers(self):
        response, status_code = app.plus("3", "5")
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {"result": 8})

    def test_plus_valid_float_numbers(self):
        response, status_code = app.plus("3.5", "2.5")
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {"result": 6.0})

    def test_plus_negative_numbers(self):
        response, status_code = app.plus("-3", "-7")
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {"result": -10})

    def test_plus_mixed_numbers(self):
        response, status_code = app.plus("-3", "5")
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {"result": 2})

    def test_plus_zero(self):
        response, status_code = app.plus("0", "10")
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {"result": 10})

    def test_plus_invalid_inputs(self):
        response, status_code = app.plus("abc", "xyz")
        self.assertEqual(status_code, 400)
        self.assertEqual(response.json, {"error_msg": "Inputs must be valid numbers"})

    def test_plus_invalid_first_input(self):
        response, status_code = app.plus("abc", "10")
        self.assertEqual(status_code, 400)
        self.assertEqual(response.json, {"error_msg": "Inputs must be valid numbers"})

    def test_plus_invalid_second_input(self):
        response, status_code = app.plus("10", "abc")
        self.assertEqual(status_code, 400)
        self.assertEqual(response.json, {"error_msg": "Inputs must be valid numbers"})


class TestIsPrime(unittest.TestCase):
    def test_is_prime_valid_numbers(self):
        response, status_code = app.is_prime("17")
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {"result": True})

    def test_is_prime_valid_numbers(self):
        response, status_code = app.is_prime("36")
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {"result": False})

    def test_is_prime_valid_numbers(self):
        response, status_code = app.is_prime("13219")
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {"result": True})

    def test_is_prime_invalid_input(self):
        response, status_code = app.is_prime("abc")
        self.assertEqual(status_code, 400)
        self.assertEqual(response.json, {"error_msg": "Input must be a valid integer"})


if __name__ == "__main__":
    unittest.main()
