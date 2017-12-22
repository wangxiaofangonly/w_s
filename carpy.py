# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
#
# def is_element_visible(self, element):
#     driver = self.driver
#     try:
#         the_element = EC.visibility_of_element_located(element)
#         assert the_element(driver)
#         flag = True
#     except:
#         flag = False
#     return flag
import time


driver = webdriver.Chrome(r"D:\webderive\chromedriver_win32\chromedriver")
# .setProperty(“webdriver.firefox.bin”, “D:\Program Files (x86)\Mozilla Firefox\firefox.exe”);
# driver = webdriver.Firefox(r"D:\tools\selenium\webdriver\geckodriver_win64\geckodriver.exe")
driver.get("https://mchexian.youbaoplus.com/static/mobilePage/baseInformation/index.html?value=YWdlbnRDb2RlPVcwMjQwMDY1MiZzcHNvdXJjZT1QMDUtQURXQlBaWUwtTS14czE2NSZuZXRjYW1wYWlnbm5vPUhEMjAxMzAzMjI0NTYmYWNjb3VudFR5cGU9MiZhY2NvdW50Tm89UFozNDM0MTUmdGVybWluYWxUeXBlPXVuQXBwNSZwYXlUeXBlPTMmdXJsQ2l0eU5hbWU9JTI1RTUlMjU4QyUyNTk3JTI1RTQlMjVCQSUyNUFDXyUyNUU1JTI1OEMlMjU5NyUyNUU0JTI1QkElMjVBQyUyNUU1JTI1QjglMjU4MiZjcFN3aXRjaD0xJm1vYmlsZT0xODIxMDMyODI4Ng==")
driver.set_window_size(414,736)
# driver.get("http://h5cartest.youbaoplus.com/static/mobilePage/baseInformation/index.html?value=YWdlbnRDb2RlPVcwMjQwMDY1MiZhY2NvdW50Tm89SkUxNzg3NzA1Jm1vYmlsZT0xODIxMDA3NjIyOA==")

#基本信息ye
cityMame = driver.find_element_by_id("cityMame")

cityMame.click()
proviceValue = driver.find_element_by_link_text("福建")

proviceValue.click()

cityValue = driver.find_element_by_link_text("福州市")

cityValue.click()

licenseNo = driver.find_element_by_id("licenseNo")
linkman = driver.find_element_by_id("linkman")
linkman.send_keys(u'你好')
ownerMobile = driver.find_element_by_id('ownerMobile')
ownerMobile.send_keys(u'13898934934')
nextButton = driver.find_element_by_id(u'nextButton')
nextButton.click()
time.sleep(3)


#车辆信息页面

vehicleFrameNo = driver.find_element_by_id('vehicleFrameNo')
vehicleFrameNo.send_keys('LVS77887873646373')

choiceType = driver.find_element_by_id('choiceType')
choiceType.send_keys(u'捷达')

searchIconicon = driver.find_element_by_css_selector("i.searchIcon")
time.sleep(1)
searchIconicon.click()

time.sleep(1)

typeList = driver.find_element_by_id('typeList')

driver.find_element_by_xpath("//div[@id='typeList']/ul/li").click()

driver.find_element_by_id('engineNo').send_keys('287834')
firstRegisterDate = driver.find_element_by_id('firstRegisterDate')

firstRegisterDate.click()

time.sleep(1)
firstRegisterDateconfirm = driver.find_element_by_class_name("dwb-c")
time.sleep(1)
firstRegisterDateconfirm.click()

# driver.find_element_by_xpath("//div[@class='android-ics']/div/div[@class='dw']/div[@class='dwwr']/div[@class='dwbc']/span[@class='dwbw']/span").click()

driver.find_element_by_name('ownerIdNo').send_keys('130431198309162115')

# driver.find_element_by_xpath("//body[@id='baseheight']/input[@id='nextButton']").click()
nextButton2 = driver.find_element_by_id('nextButton')
nextButton2.click()
time.sleep(12)

#算价

submitButton = driver.find_element_by_id(u"submitButton")
time.sleep(3)
submitButton.click()
time.sleep(10)

#核保

ActionChains(driver).click(driver.find_element_by_id('Adress')).perform()


addresseeDetailsOption = driver.find_element_by_id(u"dwb1")
time.sleep(1)
addresseeDetailsOption.click()

driver.find_element_by_id('addresseeDetails').send_keys(u'北京市通州区金融街')

driver.find_element_by_name('policyEmail').send_keys('89812391')
driver.find_element_by_id('mailList_MenuItem_@163.com').click()

driver.find_element_by_id(u"insuredIdAddress").send_keys(u"北京市通州区金融街")

asPeisongAddress= driver.find_element_by_id(u'asPeisongAddress')
time.sleep(2)
asPeisongAddress.click()
driver.find_element_by_id('hasRead').click()

nextButton3 = driver.find_element_by_id('nextButton')
nextButton3.click()

# time.sleep(1)

# driver.quit()
#driver.close()
