import unittest


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("setup method")

    def test_method(self):
        print('test method')

    def tearDown(self):
        print('teardown method')


unittest.main()
