import unittest
from time import sleep
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner


class YouJiuYe(unittest.TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.get("http://xue.ujiuye.com/foreuser/login/")

    def login(self,username,password):
        username_d1 = self.chrome.find_element_by_id("username_dl")
        password_dl = self.chrome.find_element_by_id("password_dl")
        button = self.chrome.find_element_by_class_name("loginbutton1")
        username_d1.send_keys(username)
        password_dl.send_keys(password)
        button[0].click()
        text = self.chrome.find_element_by_id("J_usernameTip").text
        return text

    def test_login_password(self):
        text = self.login("18203620679","123")
        self.assertEqual("密码应该在6-20位之间！",text,"密码太短提示内容有误！")


    def test_login_username(self):
        text = self.login("12983798379","12345678")
        self.assertEqual("账号不存在",text,"提示内容有误！")

    def tearDown(self):
        sleep(10)
        self.chrome.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(YouJiuYe("test_login_password"))
    suite.addTest(YouJiuYe("test_login_username"))


    with open("report.html","wb") as f:
        runner = HTMLTestRunner(
            stream=f,
            title="测试教学",
            description="就是一个教学测试"
        )
        runner.run(suite)

