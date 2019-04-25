from selenium import webdriver
import os,time
driver = webdriver.Chrome()
file = 'http://www.baidu.com'
driver.get(file)

#inputs = driver.find_elements_by_tag_name()
#<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
#inputs = driver.find_elements_by_id('kw')
print(driver.get_cookies())
element_keyword = driver.find_element_by_id('kw')
element_keyword.send_keys('松勤')
#time.sleep(5)
driver.implicitly_wait(10)
element_search_button = driver.find_element_by_id('su')
element_search_button.click()

#driver.quit() #浏览器和浏览器驱动会同时退出

