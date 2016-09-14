try:
    from browser import Browser
except ImportError:
    print "browser.py is missing...Exiting program."
    exit(1)

##### Combo #####

class Combo:
    driver = None
    browser = None

    def __init__(self,driver,browser):
        self.driver = driver
        self.browser = browser

    def dealloc(self):
        if self.browser:
            del self.browser
        if self.driver:
            del self.driver

    def loginFacebook(self,username,password):
        if(self.driver):
            username = username
            password = password
            usernameID = "email"
            passwordID = "pass"
            loginID = "loginbutton"
            loginURL = "http://www.facebook.com"
            current_url = self.driver.current_url
            if not current_url is loginURL:
                err = self.browser.open(loginURL)
                if err: return 1
            print("\nLog into {}".format(loginURL))

            element = self.browser.element.findElementByID(usernameID)
            if element:
                self.browser.interaction.sendTextToElement(username, element)
            else: return 1
            element = self.browser.element.findElementByID(passwordID)
            if element:
                self.browser.interaction.sendTextToElement(password, element)
            else: return 1
            element = self.browser.element.findElementByID(loginID)
            if element:
                self.browser.interaction.clickElement(element)
            else: return 1
            self.browser.tab.link = self.driver.current_url
            self.browser.tab.title = self.driver.title
            return 0
        else:
            return 1
