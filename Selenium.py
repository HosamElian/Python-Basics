from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
browser.get("https://www.google.com")
browser.find_element(".gLFyf").send_keys("كوره")