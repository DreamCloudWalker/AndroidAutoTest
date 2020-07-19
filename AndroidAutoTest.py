#  -*- coding:utf-8 -*-
from uiautomator import device as d
import unittest
import time


# d(text="华盛通港股美股").click()

class AutoTest(unittest.TestCase):
    def setUp(self):
        print("--------------onCreate a testcase--------------")

    def tearDown(self):
        print("--------------onDestroy a testcase--------------")

    def test_login(self):  # unittest方法名必须test或test_开头
        try:
            print("AutoTest, 1. launch app 华盛通港股美股")
            time.sleep(1)
            d(text="华盛通港股美股").click()

            time.sleep(5)
            print("AutoTest, 2. skip update")
            if d(resourceId="com.huasheng.stock:id/layoutDialog").exists:
                d(resourceId="com.huasheng.stock:id/diaBtnLeft").click()

            time.sleep(1)
            print("AutoTest, 3. click mine")
            if d(text="我的").exists:
                d(text="我的").click()
            else:
                raise Exception("AutoTest, test_mine: can not find 我的")

            time.sleep(1)
            print("AutoTest, 4. click login")
            if d(resourceId="com.huasheng.stock:id/user_layout").exists:
                d(resourceId="com.huasheng.stock:id/user_layout").click()
            else:
                raise Exception("AutoTest, can not find id user_layout")

            time.sleep(1)
            print("AutoTest, 5. switch to input pwd")
            if d(text="手機密碼登錄").exists:
                d(text="手機密碼登錄").click()

            time.sleep(1)
            print("AutoTest, 6. click phone num")
            input_phone_num = d(resourceId="com.huasheng.stock:id/account_num")
            if input_phone_num.exists:
                input_phone_num.click()
            else:
                raise Exception("AutoTest, can not find id account_num")

            time.sleep(1)
            print("AutoTest, 7. input phone num")
            input_phone_num.clear_text()
            input_phone_num.set_text("your_phone_num")

            time.sleep(1)
            print("AutoTest, 8. click and input pwd")
            input_pwd = d(resourceId="com.huasheng.stock:id/pwd")
            if input_pwd.exists:
                input_pwd.click()
            else:
                raise Exception("AutoTest, can not find id input_pwd")
            time.sleep(1)
            input_pwd.clear_text()
            input_pwd.set_text("your_pwd")

            time.sleep(1)
            print("AutoTest, 8. click login")
            if d(resourceId="com.huasheng.stock:id/loginbtn").exists:
                d(resourceId="com.huasheng.stock:id/loginbtn").click()
        except:
            print("AutoTest, test_login encounter exception")


def test_app():
    test_unit = unittest.TestSuite()
    test_unit.addTest(AutoTest("testLogin"))


if __name__ == '__main__':
    unittest.main()
