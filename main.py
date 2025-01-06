from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import shutil
import os

def bgfdas():
    driver_path = input("where's your chromedriver? (leave empty and i'll try magic): ").strip()
    
    if not driver_path:
        driver_path = shutil.which("chromedriver")
        if not driver_path:
            raise FileNotFoundError("uh-oh, couldn't find chromedriver. help me out here!")
    
    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"yikes, no chromedriver found at '{driver_path}'. try again?")
    
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    print("spinning up the browser... hold tight!")
    return webdriver.Chrome(service=service, options=options)

def klmnpq(driver, url, interval):
    driver.get(url)
    try:
        while True:
            time.sleep(interval)
            driver.refresh()
            print(f"whoosh! refreshed the page after {interval} seconds")
    except KeyboardInterrupt:
        print("okay okay, shutting down the browser... bye bye")
        driver.quit()

if __name__ == "__main__":
    try:
        url = input("what's the url we're visiting today? : ").strip()
        interval = float(input("how many seconds between refreshes? : ").strip())
        
        if interval <= 0:
            raise ValueError("uh-oh, time can't be zero or negative! try again?")
        
        driver = bgfdas()
        klmnpq(driver, url, interval)
    
    except ValueError:
        print("oops, that wasn't a number! try again with a valid interval")
    except FileNotFoundError as e:
        print(f"eep! {e}")
    except Exception as e:
        print(f"hmm, something went wrong: {e}")
