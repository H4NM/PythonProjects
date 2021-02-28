from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


CHAT_NAME = "The name of the chat you want to ping someone in..." #e.g. @John Doe, @Melissa etc. It autocompletes with the tab key later on
SEND_MESSAGE = "Testing some more"
#This was the classname of the input field for the text. You probably won't need to change it.
#If it does not work, inspect the input field element and check its class name.
CHATBAR_CLASS_NAME = "_2_1wd copyable-text selectable-text"
NUMBER_OF_PINGS = 20

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")

print("Scan QR Code, And then press Enter")
input()
print("Starting pinging person")

#Checks for the chat with the given chat name through xpath address
elem = driver.find_element_by_xpath("//span[@title="+"'"+CHAT_NAME+"'"+"]")
elem.click()
#Checks for the input field with the given class name, data tabs and contenteditable status through xpath address
elem = driver.find_element_by_xpath("//div[@class="+"'"+CHATBAR_CLASS_NAME+"'"+"][@data-tab='6'][@contenteditable='true']")
elem.click()

#Iterates through the number of pings/tags
for i in range(NUMBER_OF_PINGS):
    #Enters the intended message, autocompletes the tagging with the TAB key, and then send the enter key 
    elem.send_keys(SEND_MESSAGE + Keys.TAB + Keys.RETURN)
    #Waits for 1.5 seconds to make pinging vibrate the targets phone to not make each ping overlap
    time.sleep(1.5)

#Closes the application
driver.quit()

