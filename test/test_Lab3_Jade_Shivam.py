# Shivam Janda and Jade Bedlington
# test_Lab3_Jade_Shivam.py
# November 5th, 2022
# Description: This file imports lab3_Jade_Shivam.py and test the fixtures within.

import unittest
from app.Lab3_Jade_Shivam import circle_area
from app.Lab3_Jade_Shivam import ellipse_area
from app.Lab3_Jade_Shivam import rhombus_area
from app.Lab3_Jade_Shivam import trapezium_area


class TestCircle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')

    def test_circle_area(self):
        self.assertEqual(circle_area(2), 12.566370614359172)
        self.assertEqual(circle_area(1), 3.141592653589793)
        print("End of test: Test areas when radius circle >= 0")

    def test_circle_int(self):
        self.assertRaises(ValueError, circle_area, 'r')
        print(
            "End of test: Exception raised areas when radius of circle is imaginary number or boolean value or a text")

    def test_circle_value(self):
        self.assertRaises(ValueError, circle_area, -2)
        print("End of test: Exception raised areas when radius of circle < 0")


class TestTrapezium(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')

    def test_trapezium_int(self):
        self.assertEqual(trapezium_area(2, 3, 6), 15)
        self.assertEqual(trapezium_area(1, 1, 1), 1)
        print("End of test: Test areas when b1, b2, b3 of trapezium >= 0")

    def test_trapezium_int_b1(self):
        self.assertRaises(ValueError, trapezium_area, 'b1', 2, 3)
        print("End of test: Exception raised areas when b1 of trapezium is imaginary number or boolean value or a text")

    def test_trapezium_int_b2(self):
        self.assertRaises(ValueError, trapezium_area, 1, 'b2', 3)
        print("End of test: Exception raised areas when b2 of trapezium is imaginary number or boolean value or a text")

    def test_trapezium_int_h(self):
        self.assertRaises(ValueError, trapezium_area, 1, 2, 'h')
        print("End of test: Exception raised areas when h of trapezium is imaginary number or boolean value or a text")

    def test_trapezium_value_b1(self):
        self.assertRaises(ValueError, trapezium_area, -2, 3, 4)
        print("End of test: Exception raised areas when b1 of trapezium < 0")

    def test_trapezium_value_b2(self):
        self.assertRaises(ValueError, trapezium_area, 2, -3, 4)
        print("End of test: Exception raised areas when b2 of trapezium < 0")

    def test_trapezium_value_h(self):
        self.assertRaises(ValueError, trapezium_area, 2, 3, -4)
        print("End of test: Exception raised areas when h of trapezium < 0")


class TestEllipse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')

    def test_ellipse_area(self):
        self.assertEqual(ellipse_area(3, 2), 18.849555921538759430775860299677017305183016396251)
        self.assertEqual(ellipse_area(1, 1), 3.1415926535897932384626433832795028841971693993751)
        print("End of test: Test areas when a and b of circle >= 0")

    def test_ellipse_value_a(self):
        self.assertRaises(ValueError, ellipse_area, -1, 2)
        print("End of test: Exception raised areas when a of ellipse < 0")

    def test_ellipse_value_b(self):
        self.assertRaises(ValueError, ellipse_area, 1, -2)
        print("End of test: Exception raised areas when b of ellipse < 0")

    def test_ellipse_int_a(self):
        self.assertRaises(ValueError, ellipse_area, 'a', 1)
        print("End of test: Exception raised areas when a of ellipse is imaginary number or boolean value or a text")

    def test_ellipse_int_b(self):
        self.assertRaises(ValueError, ellipse_area, 1, 'b')
        print("End of test: Exception raised areas when b of ellipse is imaginary number or boolean value or a text")


class TestRhombus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')

    def test_rhombus_area(self):
        self.assertEqual(rhombus_area(3, 2), 3)
        self.assertEqual(rhombus_area(1, 1), 0.5)
        print("End of test: Test areas when d1 and d2 of rhombus >= 0")

    def test_rhombus_int_d1(self):
        self.assertRaises(ValueError, ellipse_area, 'd1', 1)
        print("End of test: Exception raised areas when d1 of rhombus is imaginary number or boolean value or a text")

    def test_rhombus_int_d2(self):
        self.assertRaises(ValueError, ellipse_area, 1, 'd2')
        print("End of test: Exception raised areas when d2 of rhombus is imaginary number or boolean value or a text")

    def test_rhombus_value_d1(self):
        self.assertRaises(ValueError, ellipse_area, -1, 2)
        print("End of test: Exception raised areas when d1 of rhombus < 0")

    def test_rhombus_value_d2(self):
        self.assertRaises(ValueError, ellipse_area, 1, -2)
        print("End of test: Exception raised areas when d2 of rhombus < 0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
