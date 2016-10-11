import os
import sys

cur_dir = os.getcwd()
par_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
if(not os.path.exists(par_dir)):
    print("Path {} does not exist".format(par_dir))
    exit(1)
os.chdir(par_dir)
sys.path.insert(0, par_dir)

try:
    from pyChrome import PyChrome
except ImportError:
    print "pyChrome.py is missing from {}\nTry copy {} to pyChrome.py directory and run it from there.".format(os.getcwd(),os.path.basename(__file__))
    exit(1)

print "\n"
print "***** Welcome to pyChrome Demo *****"
print "\nThis demo shows how you can leverage Selenium WebDriver (or pyChrome) for Web Testing and Autofill 'Any' Forms.\n" \


browser = PyChrome()
os.chdir(cur_dir)
sys.path.insert(0, cur_dir)

link = "https://login.yahoo.com/account/create?specId=yidReg&lang=en-US&src=ym&done=https%3A%2F%2Fmail.yahoo.com&display=login&intl=us"
select_link = 0

select_link = "1"
while select_link != '8':
    print "\nSelect a form\n" \
        "1. Regitster to Vote 1\n" \
        "2. Regitster to Vote 2\n" \
        "3. Create Yahoo Account\n" \
        "4. Create Gmail Account\n" \
        "5. Create Live Account\n" \
        "6. Apply Texas Form\n" \
        "7. Fill out Common App Form\n" \
        "8. Exit the Demo\n"

    select_link = raw_input("Select a form to demo Autofill (1-8)\n > ")
    try:
        select_link = int(select_link)
    except ValueError:
        print "Value Error"
        continue
    if select_link < 1 or select_link > 8:
        continue
    else:
        if select_link == 1:
            link = "https://registertovote.sos.ga.gov/GAOLVR/welcome.do#no-back-button"
            #break
        elif select_link == 2:
            link = "http://registertovote.ca.gov/?ref=voteusa"
            #break
        elif select_link == 3:
            link = "https://login.yahoo.com/account/create?specId=yidReg&lang=en-US&src=ym&done=https%3A%2F%2Fmail.yahoo.com&display=login&intl=us"
            #break
        elif select_link == 4:
            link = "https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en"
            #break
        elif select_link == 5:
            link = "https://signup.live.com"
            #break
        elif select_link == 6:
            link = "https://www.applytexas.org/adappc/gen/profile.WBX"
            #break
        elif select_link == 7:
            link = "https://apply.commonapp.org/createaccount"
            #break
        elif select_link == 8:
            browser.quit()
            exit(0)
        else:
            continue

    print "\nSelected Link: {}\n".format(link)
    browser.open(link)

    char = 's'
    items = []
    last_item = None
    while char != 'q':
        char = raw_input("\nPress Enter to Record\n"
                         "Enter 'P' to Playback\n"
                         "Enter 'D' to Delete last entry\n"
                         "Enter 'S' to Save all the records\n"
                         "Enter 'L' to Load all the records\n"
                         "Enter 'C' to Clear all the records\n"
                         "Enter 'Q' to Quit the current form\n > ")
        try:
            char = str(char)
            char.lower()
        except ValueError:
            print "Value Error"
            continue
        if char == '\n' or char == '':
            browser.record()
            items = browser.getRecordedElements()
            last_item = items[len(items)-1]
            print "Element Recorded: {}".format(last_item.output())
        elif char == 'd':
            if last_item:
                print "Element Deleted: {}".format(last_item.output())
            err = browser.deleteRecord()
            if err:
                print "Failed to delete or no element is captured to delete"
        elif char == 'p':
            err = browser.playback()
            if err:
                print "Playback completed with Error"
            else:
                print "Playback completed"
        elif char == 's':
            filename = raw_input("Enter the name of the file to save it\n > ")
            if filename and len(filename):
                err = browser.storeRecorder(filename,directory=cur_dir)
            else: err = browser.storeRecorder()
            if err:
                print "Failed to store the file"
            else:
                print "File {}.json stored at {}".format(filename,cur_dir)
        elif char == 'l':
            filename = raw_input("Enter the name of the file to load it\n > ")
            if filename and len(filename):
                err = browser.loadRecorder(filename,directory=cur_dir)
            else: err = browser.loadRecorder()
            if err:
                print "Failed to load the file"
            else:
                del items[:]
                del last_item
                items = browser.getRecordedElements()
                last_item = items[len(items)-1]
                print "File {}.json loaded from {}".format(filename,cur_dir)
        elif char == 'c':
            if items and len(items):
                print "Clearing out all the recorded items"
                browser.clearRecorder()
                del items[:]
                if last_item:
                    last_item = None
            else:
                print "Recorded elements is empty"
        elif char == 'q':
            del items[:]
            del last_item
        else:
            continue
