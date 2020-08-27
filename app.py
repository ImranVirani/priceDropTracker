from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from time import sleep
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)
bestPrice = 0
productUrl = input("Please enter the URL of the product you which to price track: ")
while True:
    
    driver.get(productUrl)
    sleep(1)

    search1 = driver.find_element_by_class_name("price_FHDfG")
    output = search1.text
    output = output.replace("$", "")
    output = float(output)
    output = output / 100
    if bestPrice > output:
        print("Price drop detected")
        # Insert code to send an email that says that there is a price drop
    print(str(output))
    sleep(20)
# driver must not be quit each time
driver.quit()