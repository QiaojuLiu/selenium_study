from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os,time
driver = webdriver.Chrome()
file = 'https://kyfw.12306.cn/otn/leftTicket/init'
driver.get(file)

#inputs = driver.find_elements_by_tag_name()
#<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
#inputs = driver.find_elements_by_id('kw')
element_keyword = driver.find_element_by_id('fromStationText')
element_keyword.clear()
element_keyword.send_keys('上海\n')
time.sleep(5)
to_element = driver.find_element_by_id('toStationText')
to_element.clear()
to_element.send_keys('兰州\n')
time.sleep(6)
timeSelect = Select(driver.find_element_by_id('cc_start_time'))
timeSelect.select_by_visible_text('00:00--24:00')
tomrow = driver.find_element_by_css_selector('#date_range li:nth-child(5)')
tomrow.click()
"""xpath = '//#[@id="querLeftTable"]//td[4][@class]/../td[1]//a'
theTrains = driver.find_elements_by_xpath(xpath)
for one in theTrains:
    print(one.text)"""
"""driver.find_element_by_id('train_date').send_keys()
time.sleep(5)
element_search_button = driver.find_element_by_id('su')
element_search_button.click()
#date_range > ul > li:nth-child(5) > span:nth-child(1)
#date_range > ul > li:nth-child(5) > span.hide"""
#<td title="" ifalow_maxlength="1" hbdata="2019-04-28#5l000G197030#SWZ_#" hbid="2019-04-28#AOH#LAJ#5l000G197030#SWZ_#01#上海虹桥#21
##兰州西#T8u34N3R6%2B3zNCTnnyLZj16Z%2Bfs%2BT8gVfrLFl1wK3nujp%2F38QQwtfYtpCYfzm34h1qg6NuIQDqZh%0ARdYFG%2FNE%2B3OOeg6ZeUYIbwa9T%2FlNZJKnxih4OmgTTGMSGof5wftuQR5wyo8YckK6l4A%2FMoRQO5nm%0AxHucn9AN99Y5rFUi8yDu19qu8orFvJfkk83Fb%2FVQuq6c5cDv8xmxt2LoEFv%2BF9FdidAr2o0UJ9bb%0AE7ZxUsTD%2Fg1edID1VwRE5kpQ8isvJE3B2HQfVJcLnQbEAfki53hN7o0wloNOAqKVDVXPgD3nlNQ5%0AVtsGrQ%3D%3D#G1970#" width="46"
#align="center" style="cursor: pointer;" class="t-num" onclick="showTicketPrice(this)"
#id="SWZ_5l000G197030"><div>5</div></td>
#date_range > ul > li:nth-child(3)
##ZE_5l0000G10200
#//*[@id="ZE_5l0000G10200"]
#driver.quit() #浏览器和浏览器驱动会同时退出"""

