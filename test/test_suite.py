# Shivam Janda and Jade Bedlington
# test_suite.py
# November 5th, 2022
# Description: this is the main test file, that includes all other tests files and user's menu options.

import unittest
from test_Lab3_Jade_Shivam import TestCircle
from test_Lab3_Jade_Shivam import TestTrapezium
from test_Lab3_Jade_Shivam import TestEllipse
from test_Lab3_Jade_Shivam import TestRhombus

testcase1 = unittest.TestLoader().loadTestsFromTestCase(TestCircle)
testcase2 = unittest.TestLoader().loadTestsFromTestCase(TestTrapezium)
testcase3 = unittest.TestLoader().loadTestsFromTestCase(TestEllipse)
testcase4 = unittest.TestLoader().loadTestsFromTestCase(TestRhombus)

display = ''' Please enter one of the following options:
            - 'c' for testing area of circle
            - 't' for testing area of trapezium
            - 'e' for testing area of ellipse
            - 'r' for testing area of rhombus
            - 'q' to quit 
            What would you like to do? '''

while (option := input(display).lower()) != "q":
    if option == "c":
        unittest.TextTestRunner().run(testcase1)
    elif option == "t":
        unittest.TextTestRunner().run(testcase2)
    elif option == "e":
        unittest.TextTestRunner().run(testcase3)
    elif option == "r":
        unittest.TextTestRunner().run(testcase4)
    else:
        print("Unknown Command")

if __name__ == "__main__":
    unittest.main(verbosity=2)
