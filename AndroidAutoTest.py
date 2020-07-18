#  -*- coding:utf-8 -*-
from uiautomator import device as d
import unittest


# d(text="华盛通港股美股").click()

class AutoTest(unittest.TestCase):
    def setUp(self):
        print("--------------onCreate")

    def tearDown(self):
        print("--------------onDestroy")

    def test_launch(self):  # unittest方法名必须test或test_开头
        print("--------------launch app 华盛通港股美股")
        d(text="华盛通港股美股").click()


def test_app():
    test_unit = unittest.TestSuite()
    test_unit.addTest(AutoTest("testLogin"))


if __name__ == '__main__':
    unittest.main()
