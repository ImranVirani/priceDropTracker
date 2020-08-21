
start_url = "https://duckgo.com"
driver.get(start_url)
print(driver.page_source.encode("utf-8"))
driver.quit()