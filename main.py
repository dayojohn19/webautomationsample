from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# # Firefox options
# options = Options()
# options.headless = False  # set True if you don't want to see the browser

# # Set Tor SOCKS5 proxy
# options.set_preference("network.proxy.type", 1)
# options.set_preference("network.proxy.socks", "127.0.0.1")
# options.set_preference("network.proxy.socks_port", 9050)
# options.set_preference("network.proxy.socks_remote_dns", True)

# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

# driver.get("https://check.torproject.org/")






from selenium.common.exceptions import NoAlertPresentException, WebDriverException

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


# MY IP 20.97.189.103
# service = Service(executable_path="")
# driver = webdriver.Chrome(service=service)
# time.sleep(1)
# driver.get("http://127.0.0.1:8000/")
# time.sleep(1)
# driver.execute_script("createViaje()")
# # Click the Register button
# register_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Register')]")))
# register_button.click()

# # Wait for alert to appear and accept it
# try:
#     alert = WebDriverWait(driver, 5).until(lambda d: d.switch_to.alert)
#     print("Alert text:", alert.text)
#     alert.accept()  # or alert.dismiss()
# except TimeoutException:
#     print("No alert appeared")

# signup_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign-up')]")))
# # signup_button = driver.find_element(By.XPATH, "//button[text()='Sign-up']")
# signup_button.click()

# user_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usernameInput")))
# user_contact = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userContactInput")))
# user_password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "PasswordInput1")))
# user_passwordconfirm = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "PasswordInput2")))

# # Fill in the username
# time.sleep(1)
# user_name.send_keys("my_username1")
# time.sleep(1)
# user_contact.send_keys("user_contact")
# time.sleep(1)
# user_password.send_keys("user_password")
# time.sleep(1)
# user_passwordconfirm.send_keys("user_password")
# time.sleep(1)

# sign_up_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='Sign up']"))
# )

# sign_up_button.click()

# logout_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Log out')]")))
# time.sleep(1)
# logout_button.click()
# time.sleep(10)


# time.sleep(15)


# Automation Sign UP 
# Use to Sign Up and create a schedule in Carpooling App
# Make sure the server is running at http://127.0.0.1
# Run the Tor service first
# `brew services start tor`
# `netstat -an | grep 9050`
class WebsiteTester:
    print('\n\nStarting Test')
    def __init__(self, urlsiteserver="http://127.0.0.1:8000/"):
        options = Options()
        options.headless = False  # set True if you don't want to see the browser
        # Set Tor SOCKS5 proxy
        options.set_preference("network.proxy.type", 1)
        options.set_preference("network.proxy.socks", "127.0.0.1")
        options.set_preference("network.proxy.socks_port", 9050)
        options.set_preference("network.proxy.socks_remote_dns", True)
        service = Service(executable_path="")
        self.driver = webdriver.Chrome(service=service)
        # 
        """
        For Tor with Firefox

        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

        Note: not working with alerts
        """
        # 
        self.driver.get(urlsiteserver)
        # driver.execute_script("createViaje()")
        # self.signUp("my_username10", "user_contact", "user_password")
        # self.createSchedule()

    def findElementandClick(self, tofindbuttonoratext):
        # Accepts Button text to find and click
        # foundButton = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, f'//button[contains(text(),"{tofindbuttonoratext}")]')))
        try:
            # Try to find a <button> first
            foundButton = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, f'//button[contains(text(),"{tofindbuttonoratext}")]'))
            )
        except TimeoutException:
            try:
                # If not found, try an <a> tag
                foundButton = WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, f'//a[contains(text(),"{tofindbuttonoratext}")]'))
                )
            except TimeoutException:
                foundButton = None
                print(f'Could not find a button or link with text "{tofindbuttonoratext}"')


        time.sleep(1)
        foundButton.click()
        time.sleep(1)
    def findElementandWrite(self, tofindelementid, text):
        # Accepts Element ID and text to write
        try:
            foundElement = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, tofindelementid)))
        except:
            foundElement = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.NAME, tofindelementid))
            )            
        foundElement.send_keys(text)
    # def handleAlert(self):
    #     try: # Check if alert received
    #         time.sleep(1)
    #         alert = WebDriverWait(self.driver, 5).until(lambda d: d.switch_to.alert)
    #         # alert = self.driver.switch_to.alert
    #         try:
    #             alert_text = alert.text
    #             print("Alert text:", alert_text)
    #         except:
    #             print("Alert present but cannot read text")            
    #         alert.accept()
    #         if len(self.driver.window_handles) > 0:
    #             self.driver.switch_to.window(self.driver.window_handles[0])
    #         else:
    #             print("No window available!")
    #     except TimeoutException:
    #         print("No alert appeared")
    #     print('continued after alert')        

    def handleAlert(self, accept=True):
        """
        Safely handle a JavaScript alert.
        
        :param driver: Selenium WebDriver instance
        :param accept: True to accept, False to dismiss
        """
        try:
            time.sleep(0.5)  # small wait for alert to appear
            alert = self.driver.switch_to.alert
            try:
                alert_text = alert.text
                print("Alert text:", alert_text)
            except WebDriverException:
                print("Alert present but cannot read text")
            if accept:
                alert.accept()
            else:
                alert.dismiss()
            return True  # alert was handled
        except NoAlertPresentException:
            print("No alert present")
            return False  # no alert
        except WebDriverException as e:
            print("Browser became unresponsive while handling alert:", e)
            return False

    def signUp(self, username, contact, password):
        self.driver.execute_script("createViaje()")
        self.findElementandClick('Register')
        print('Clicked Register')
        self.handleAlert()
        self.findElementandClick('Sign-up')
        self.findElementandWrite('usernameInput', username)
        self.findElementandWrite('userContactInput', contact)
        self.findElementandWrite('PasswordInput1', password)
        self.findElementandWrite('PasswordInput2', password)
        print('Filled the form')
        sign_up_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='Sign up']"))
        )
        print('Found Sign up button')
        sign_up_button.click()        
        time.sleep(1)
        # self.findElementandClick('Log out')
    def logOut(self):
        logout_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/userProfile/logoutjson']"))
        )
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", logout_link)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # logout_link.click()        
        self.driver.execute_script("arguments[0].click();", logout_link)
        # self.findElementandClick('Log Out')

    def createSchedule(self,methodplace='imMake', originplace='OriginPlace', destinationplace='DestinationPlace', dateplace='11-22-2025', detailsplace='this is additional details'  ):
    # def createSchedule(self):
        self.findElementandClick('Treep')
        self.driver.execute_script("createViaje()")
        if methodplace == 'create':
            createradiobutton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "imMake")))
        elif methodplace == 'look':
            createradiobutton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "imFind")))
        else:
            createradiobutton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "imFind")))
        createradiobutton.click()
        self.findElementandWrite('meetPlace', originplace)
        self.findElementandWrite('place', destinationplace)
        self.findElementandWrite('meetDate', dateplace)
        self.findElementandWrite('theDetails', detailsplace)
        submitbutton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='Submit']"))
        )        
        submitbutton.click()
        self.handleAlert()
        

        # self.driver.quit()
        pass
    
tester = WebsiteTester()

# tester.signUp("my_username11", "user_contact", "user_password")
tester.signUp("my_username22", "user_contact", "user_password")
tester.createSchedule( methodplace = 'look',originplace='New York', destinationplace='Washington DC', dateplace='11-22-2025', detailsplace='No luggage, just me'  )
time.sleep(5)
tester.logOut()
tester.signUp("my_username23", "user_contact", "user_password")
tester.createSchedule( methodplace = 'look',originplace='New York2', destinationplace='Washington DC', dateplace='11-22-2025', detailsplace='No luggage, just me'  )