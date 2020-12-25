from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# BROWSERSTACK_URL = 'https://kevin1659:UydKZsrDxNwtqJDGMssJ@hub-cloud.browserstack.com/wd/hub'

# desired_cap = {

#     'os': 'OS X',
#     'os_version': 'Big Sur',
#     'browser': 'Chrome',
#     'browser_version': '87.0',
#     'name': "kevin1659's First Test"

# }
USER = 'admin+a@gather.app'
PWORD = 'asdfjkl;'

options = Options()
options.add_argument('--enable-javascript')

driver = webdriver.Chrome(options=options)
# driver = webdriver.Remote(
#     command_executor=BROWSERSTACK_URL,
#     desired_capabilities=desired_cap
# )

driver.get("https://my.gatherqa.app/admin/")
if "Google" in driver.title:
    raise Exception("Unable to load google page!")
login_name = driver.find_element_by_xpath('//*[@id="adornment-email"]')
login_name.send_keys(USER)
login_pword = driver.find_element_by_xpath('//*[@id="adornment-password"]')
login_pword.send_keys(PWORD)
login_submit = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[1]/div[2]/form/div[3]/div/button[2]')
login_submit.click()
wait = WebDriverWait(driver, 20)
create_new_funeral_home = wait.until(EC.element_to_be_clickable((By.ID, 'common-drawer')))
    # '//div[@id="common-drawer"]//*[name()="svg"]/*[name()="path"]')
    # '//*[@id="common-drawer"]//*[name()="svg"]//*[name()="d"]')
    # "//div[@id='common-drawer']//*[local-name()='svg']/*[*[local-name()='path']]")))
create_new_funeral_home.click()
# elem.send_keys("BrowserStack")
# elem.submit()
print(driver.title)
# driver.quit()

# < button class = "jss906 jss880 jss882 jss883 jss885 jss886 jss1572" tabindex = "0" type = "button" >
# < span class = "jss881" > < svg class = "jss169 jss1571" focusable = "false" viewBox = "0 0 24 24" aria - hidden = "true" role = "presentation" >
# <path d = "M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z" > </path > </svg > create New Funeral Home < /span > <span class = "jss909" > </span > </button >
#common-drawer > div > div.jss1562.jss1634 > div > button.jss906.jss880.jss882.jss883.jss885.jss886.jss1572
