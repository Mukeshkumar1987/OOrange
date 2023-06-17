import time

from pageObjects.LoginPage import Login
from utilities.Logger import LogGenerator
from utilities.Readproperties import Readconfig


class Test_Login_Params:

    url = Readconfig.geturl()
    # username = Readconfig.getusername()
    # password = Readconfig.getpassword()
    log = LogGenerator.loggen()



    def test_login_params_003(self,setup,getDataForLogin):
        self.log.info("Opeing Browser")
        self.driver = setup
        self.driver.get(self.url)
        self.log.info("Going to url")
        self.lp = Login(self.driver)
        self.lp.Enter_UserName(getDataForLogin[0])
        self.log.info("Enter username-->" + getDataForLogin[0])
        self.lp.Enter_Password(getDataForLogin[1])
        self.log.info("Enter password-->"+ getDataForLogin[1])
        self.lp.Click_Login()
        self.log.info("click the login")
        login_status=[]
        if self.lp.Login_Status()==True:
            if getDataForLogin[2]=="Pass":
                login_status.append("Pass")
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\FInalOrange\\ScreenShot\\test_login-params.py-pass.png")
                self.lp.Click_MenuButton()
                self.log.info("click Menu Button")
                self.lp.Click_Logout()
                self.log.info("Click logout Button")
            elif getDataForLogin[2]=="Fail":
                login_status.append("Fail")
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\FInalOrange\\ScreenShot\\test_login-params.py-fail.png")
                self.lp.Click_MenuButton()
                self.log.info("CLick menu botton")
                self.lp.Click_Logout()
                self.log.info("click logout")
        else:
            if getDataForLogin[2]=="Fail":
                login_status.append("Pass")
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\FInalOrange\\ScreenShot\\test_login-params.py-fail.png")
            elif getDataForLogin[2] =="Pass":
                login_status.append("Fail")
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\FInalOrange\\ScreenShot\\test_login-params.py-fail.png")
        print(login_status)

        if "Fail" not in login_status:
            self.log.info("test_login_params_003 is passed")
            assert True
        else:
            self.log.info("test_login_params is failed")
        self.driver.close()




































