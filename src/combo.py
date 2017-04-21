import logging
import time
##### Combo #####

class Combo:

    def loginFacebook(self,username,password,ghostmode=0):
        if(self.driver):
            username = username
            password = password

            if ghostmode:
                usernameID = "email"
                passwordID = "pass"
                loginID = "login"
            else:
                usernameID = "email"
                passwordID = "pass"
                loginID = "u_0_q"

            loginURL = "http://www.facebook.com"
            current_url = self.browser.cur_tab.link
            if not current_url is loginURL:
                err = self.browser.open(loginURL)
                if err: return 1
            logging.debug("Using ID {} and Password {} to Login".format(username,password))
            logging.info("\nLog into {}".format(loginURL))

            if ghostmode:
                element = self.findElementByName(usernameID)
                if element:
                    self.sendTextToElement(username, element)
                else:
                    return 1
                element = self.findElementByName(passwordID)
                if element:
                    self.sendTextToElement(password, element)
                else:
                    return 1
                element = self.findElementByName(loginID)
                if element:
                    self.clickElement(element)
                else:
                    return 1
            else:
                element = self.findElementByID(usernameID)
                if element:
                    self.sendTextToElement(username, element)
                else: return 1
                element = self.findElementByID(passwordID)
                if element:
                    self.sendTextToElement(password, element)
                else: return 1
                element = self.findElementByID(loginID)
                if element:
                    self.clickElement(element)
                else:
                    return 1
            return 0
        else:
            logging.error("WebDriver is not present")
            return 1


    def search(self, text):
        if text == 0 or len(text) == 0:
            logging.error("Nothing to search {}".format(text))
            return 1
        logging.info("Preparing to Search...")
        if not self.driver.current_url is "http://www.google.com":
            self.open("http://www.google.com")
        name_str = "q"
        element = self.findElementByName(name_str)
        if element == 0:
            logging.error("Couldn't find any element by its name attribute {}".format(name_str))
            return 1
        self.sendTextToElement(text,element)
        name_str = "btnG"
        element = self.findElementByName(name_str)
        if element == 0:
            logging.error("Couldn't find any element by its name attribute {}".format(name_str))
            return 1
        logging.info("Searching for {}".format(text))
        if self.clickElement(element):
            return 1
        return 0
