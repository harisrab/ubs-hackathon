from selenium import webdriver
from xvfbwrapper import Xvfb




def run_minesweeper(payload):
    print(payload)
    minesweeper_link = payload[0]

    xf = Xvfb()
    xf.start()

    driver = webdriver.Firefox()

    return None
