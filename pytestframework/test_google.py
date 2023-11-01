from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_demo():
    Driver=webdriver.Chrome()
    Driver.maximize_window()
    Driver.implicitly_wait(30)
    Driver.get("https://demo.automationtesting.in/Windows.html")
    assert Driver.title=="Frames & windows"
    Driver.quit()
    
    
def test_google():
    Driver=webdriver.Chrome()
    Driver.maximize_window()
    Driver.implicitly_wait(30)
    Driver.get("https://www.google.com/")
    assert Driver.title=="Google"
    Driver.quit()
    
    
def test_facebook():
    Driver=webdriver.Chrome()
    Driver.maximize_window()
    Driver.implicitly_wait(30)
    Driver.get("https://www.facebook.com")
    assert Driver.title=="FaceBook"
    
    
def test_instagram():
    Driver=webdriver.Chrome()
    Driver.maximize_window()
    Driver.implicitly_wait(30)
    Driver.get("https://www.Instagram.com")
    assert Driver.title=="Instagram"
    
    
def test_gmail():
    Driver=webdriver.Chrome()
    Driver.maximize_window()
    Driver.implicitly_wait(30)
    Driver.get("https://www.gmail.com")
    
    
    
    
    



    
    