import re                                 
from datetime import datetime              
from pathlib import Path              
import time                             

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException


URL="https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L"  
HEADLESS=False                            


def f(d, css):
    try:
        return d.find_element(By.CSS_SELECTOR, css).text.strip()  
    except:
        return ""                        


def price_to_float(t):
    m = re.findall(r"[\d\.,]+", t or "")  
    if not m:
        return None                   
    s = m[0]                            
    s = s.replace(".","").replace(",",".") if (
        s.count(",")==1 and s.count(".")>=1 and s.rfind(",")>s.rfind(".")
    ) else s.replace(",","")           
    try:
        return float(s)               
    except:
        return None                  


def click_continue_shopping_until_open(d, max_wait=8):
    """
    If 'Continue shopping' appears, keep trying to click it (quick retries)
    until the product page is open (productTitle present) or timeout.
    """
    start = time.time()

    xpaths = [
        "//*[@id='continue-shopping']",
        "//a[normalize-space()='Continue shopping']",
        "//button[normalize-space()='Continue shopping']",
        "//input[@type='submit' and (contains(@value,'Continue shopping') or contains(@aria-label,'Continue shopping'))]",
    ]

    while time.time() - start < max_wait:
        # If product page is open, stop
        if d.find_elements(By.ID, "productTitle"):
            return True

        clicked_any = False

        for xp in xpaths:
            els = d.find_elements(By.XPATH, xp) 
            if not els:
                continue

            el = els[0]
            try:
                d.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
                el.click()
            except (ElementClickInterceptedException, Exception):
                d.execute_script("arguments[0].click();", el)

            clicked_any = True
            time.sleep(0.25) 

        time.sleep(0.25 if clicked_any else 0.35)

    return False


o = Options()                          
if HEADLESS:
    o.add_argument("--headless=new")   
o.add_argument("--window-size=1400,900") 
o.add_argument("--disable-blink-features=AutomationControlled") 


d = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=o
)

try:
    d.get(URL)                             

    click_continue_shopping_until_open(d, max_wait=8)

    WebDriverWait(d,20).until(         
        EC.presence_of_element_located((By.ID,"productTitle"))
    )

    title = d.find_element(By.ID,"productTitle").text.strip() 

    p = (
        f(d,"span.a-price span.a-offscreen") or
        f(d,"#corePriceDisplay_desktop_feature_div span.a-price span.a-offscreen")
    )

    if not p:                       
        whole = f(d,"span.a-price-whole") 
        frac  = f(d,"span.a-price-fraction")  
        p = (whole.replace(".","") + ("."+frac if frac else "")) if whole else ""

    val = price_to_float(p)

    Path("data/screenshots").mkdir(parents=True, exist_ok=True)
    d.save_screenshot(
        f"data/screenshots/amazon_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    )

    print(f"Product: {title}\nPrice: {p} ({val})")

finally:

    d.quit()
