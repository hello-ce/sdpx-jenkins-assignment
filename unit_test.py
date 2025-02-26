import unittest

from app import app


# class TestPlus(unittest.TestCase):

#     def test_plus_negative_numbers(self):
#         response, status_code = app.plus("-3", "-7")
#         self.assertEqual(status_code, 200)
#         self.assertEqual(response.json, {"result": -10})

#     def test_plus_mixed_numbers(self):
#         response, status_code = app.plus("-3", "5")
#         self.assertEqual(status_code, 200)
#         self.assertEqual(response.json, {"result": 2})

#     def test_plus_zero(self):
#         response, status_code = app.plus("0", "10")
#         self.assertEqual(status_code, 200)
#         self.assertEqual(response.json, {"result": 10})

#     def test_plus_invalid_inputs(self):
#         response, status_code = app.plus("abc", "xyz")
#         self.assertEqual(status_code, 400)
#         self.assertEqual(response.json, {"error_msg": "Inputs must be valid numbers"})

#     def test_plus_invalid_first_input(self):
#         response, status_code = app.plus("abc", "10")
#         self.assertEqual(status_code, 400)
#         self.assertEqual(response.json, {"error_msg": "Inputs must be valid numbers"})

#     def test_plus_invalid_second_input(self):
#         response, status_code = app.plus("10", "abc")
#         self.assertEqual(status_code, 400)
#         self.assertEqual(response.json, {"error_msg": "Inputs must be valid numbers"})


# class TestIsPrime(unittest.TestCase):
#     def test_true_when_x_is_13219(self):
#         response, status_code = app.is_prime("13219")
#         self.assertEqual(status_code, 200)
#         self.assertEqual(response.json, {"result": True})

#     def test_true_when_x_is_36(self):
#         response, status_code = app.is_prime("36")
#         self.assertEqual(status_code, 200)
#         self.assertEqual(response.json, {"result": False})

#     def test_true_when_x_is_17(self):
#         response, status_code = app.is_prime("17")
#         self.assertEqual(status_code, 200)
#         self.assertEqual(response.json, {"result": True})

#     def test_is_prime_invalid_input(self):
#         response, status_code = app.is_prime("abc")
#         self.assertEqual(status_code, 400)
#         self.assertEqual(response.json, {"error_msg": "Input must be a valid integer"})


class TestIsCircleSurface(unittest.TestCase):
    def test_x_is_1(self):
        response, status_code = app.cir_sur("1")
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {"result": 12.56})

    def test_x_is_1dot5(self):
        response, status_code = app.cir_sur("1.5")
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {"result": 28.26})

    def test_x_is_ne0(self):
        response, status_code = app.cir_sur("-1")
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {"result": 0.00})



if __name__ == "__main__":
    unittest.main()
