

from selenium import webdriver


driver = webdriver.Chrome("C:\\Users\\bobby\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.youtube.com/watch?v=juKRybHPMwE&t=496s")
driver.maximize_window()
driver.implicitly_wait(2)

#if you would like to find a page to log into then change the driver.get (above) to the specific page URL, 
#then target the elements and use your credentials to test!(Below). Start by getting Selenium and changing the
#"driver=" path. 

#driver.find_element_by_id("email").send_keys("email@address")
#driver.find_element_by_name("pass").send_keys("passwordPlaceholder")
#driver.find_element_by_id("loginbutton").click()
