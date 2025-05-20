import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from settings import USERNAMES_FILENAME

def get_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

BASE_URL = "https://www.instagram.com"
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # optional
# chrome_options.add_argument("--headless")       # optional: for headless mode

BROWSER = webdriver.Chrome(options=chrome_options)
BASE_DIR = os.getcwd()
FILE = USERNAMES_FILENAME + ".txt"
FILE_LOCATION = os.path.join(BASE_DIR, FILE)

from selenium import webdriver



