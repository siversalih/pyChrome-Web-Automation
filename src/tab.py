import logging

class Tab:
    link = ""
    index = 1
    title = ""
    windowHandle = None

    def __init__(self,index, windowHandle,link = 0,title = 0):
        self.link = ""
        if link:
            self.link = link
        self.title = ""
        if title:
            self.title = title
        self.index = index
        self.windowHandle = windowHandle
        return

    def dealloc(self):
        if self.link:
            del self.link
        if self.index:
            self.index = None
        if self.title:
            del self.title
        if self.windowHandle:
            del self.windowHandle

    def printTab(self):
        logging.info("-----Tab Info-------")
        logging.info("Tab: {}".format(self.index))
        logging.info("Title: {}".format(self.title))
        logging.info("Link: {}".format(self.link))
        logging.info("Window Handle: {}".format(self.windowHandle))
        logging.info("--------------------")

