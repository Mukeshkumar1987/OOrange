import time

from pageObjects.LoginPage import Login
from utilities.Logger import LogGenerator
from utilities.Readproperties import Readconfig


class Test_Login:

    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()



    def test_login002(self,setup):
        self.driver = setup
        self.log.info("start execution testcases")
        self.log.info("Opeing Browser")
        self.driver.get(self.url)
        self.lp = Login(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Enter Username" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Enter Password" + self.password)
        self.lp.Click_Login()
        self.log.info("click the login")
        if self.lp.Login_Status()==True:
            self.log.info("test login 002 is passed")
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\FInalOrange\\ScreenShot\\test_login.py-pass.png")
            self.lp.Click_MenuButton()
            self.log.info("Click menu Button")
            self.lp.Click_Logout()
            self.log.info("Enter the logout Button")
            assert True
        else:
            self.log.info("test case login 002 is failed")
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\FInalOrange\\ScreenShot\\test_login.py-fail.png")
            assert False
        self.driver.close()
        self.log.info("test case login002 is completed")







