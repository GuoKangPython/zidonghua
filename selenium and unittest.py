# import unittest
# from time import sleep
#
# from selenium import webdriver
#
#
# class YouJiuYe(unittest.TestCase):
#
#     def setUp(self):
#         self.chrome = webdriver.Chrome()
#         self.chrome.get("http://xue.ujiuye.com/foreuser/login/")
#
#     def test_login_password(self):
#         username_d1 = self.chrome.find_element_by_id("username_dl")
#         password_dl = self.chrome.find_element_by_id("password_dl")
#         button = self.chrome.find_element_by_class_name("loginbutton1")
#
#
#         username_d1.send_keys("18203620679")
#
#         password_dl.send_keys("1234")
#         button[0].click()
#
#         text =self.chrome.find_element_by_id("J_usernameTip").text
#
#         self.assertEqual("密码应该在6-20位之间！",text,"密码太短提示内容有误")
#
#     def test_login_username(self):
#         username_d1 = self.chrome.find_element_by_id("username_dl")
#         password_dl = self.chrome.find_element_by_id("password_dl")
#         button = self.chrome.find_elements_by_class_name("loginbutton1")
#
#         username_d1.send_keys("13331153361")
#         password_dl.send_keys("123456789")
#         button[0].click()
#
#         text = self.chrome.find_element_by_id("J_usernameTip").text
#         self.assertEqual("账号不存在",text, "提示内容有误")
#
#     def tearDown(self):
#         sleep(5)
#         self.chrome.close()
#
#
# if __name__ == '__main__':
#     unittest.main()

import unittest
from time import sleep
from selenium import webdriver


class YouJiuye(unittest.TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.get("http://xue.ujiuye.com/foreuser/login/")

    def login(self, username, pasword):
        username_d1 = self.chrome.find_element_by_id("username_dl")
        password_dl = self.chrome.find_element_by_id("password_dl")
        button = self.chrome.find_elements_by_class_name("loginbutton1")
        username_d1.send_keys(username)
        password_dl.send_keys(pasword)
        button[0].click()
        text = self.chrome.find_element_by_id("J_usernameTip").text
        return text

    def test_login_password(self):
        text = self.login("18203620679", "112")
        self.assertEqual("密码应该为6-20位之间！", text, "密码太短提示内容有误")

    def test_login_username(self):
        text = self.login("18203620679", "12345678")
        self.assertEqual("账号不存在", text, "提示内容有误")

    def tearDown(self):
        sleep(5)
        self.chrome.close()


if __name__ == '__main__':
    unittest.main()




