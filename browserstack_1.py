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

test_address = input("Address to test: ")
ADDRESS_SPAN_STR = '//span[text()="View {0}\'s Dashboard"]'.format(test_address)

driver.get("https://my.gatherqa.app/admin/")
if not "Gather" in driver.title:
    raise Exception("Unable to load app!")
login_name = driver.find_element_by_xpath('//*[@id="adornment-email"]')
login_name.send_keys(USER)
login_pword = driver.find_element_by_xpath('//*[@id="adornment-password"]')
login_pword.send_keys(PWORD)
login_submit = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[1]/div[2]/form/div[3]/div/button[2]')
login_submit.click()
wait = WebDriverWait(driver, 20)
create_wait = WebDriverWait(driver, 35)
# -- Create New Funeral Home button
create_new_funeral_home = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//span[text()="  create New Funeral Home"]'))).click()
add_new_funeral_home_address = driver.find_element_by_id(
    "downshift-simple-input").send_keys(test_address)
add_new_funeral_home_address_button = driver.find_element_by_xpath(
    '//span[text()="Create Funeral Home"]').click()
print(ADDRESS_SPAN_STR)
complete_create = create_wait.until(EC.element_to_be_clickable(
    (By.XPATH, ADDRESS_SPAN_STR))).click()
# # -- Funeral Homes button
# funeral_homes = wait.until(EC.element_to_be_clickable(By.XPATH, '//span[text()="Funeral Homes"]'))
# # -- Cases button
# funeral_homes=wait.until(EC.element_to_be_clickable(By.XPATH, '//span[text()="Cases"]'))
# # -- Live Stream button
# funeral_homes=wait.until(EC.element_to_be_clickable(By.XPATH, '//span[text()="Live Stream"]'))
# # -- G&S button
# funeral_homes=wait.until(EC.element_to_be_clickable(By.XPATH, '//span[text()="Goods & Services"]'))
# # -- Program Builder button
# funeral_homes=wait.until(EC.element_to_be_clickable(By.XPATH, '//span[text()="Program Builder"]'))
# # -- Designs button
# funeral_homes=wait.until(EC.element_to_be_clickable(By.XPATH, '//span[text()="Designs"]'))
# # -- Content Library button
# funeral_homes=wait.until(EC.element_to_be_clickable(By.XPATH, '//span[text()="Content Library"]'))
# # -- Service Detail button
# funeral_homes=wait.until(EC.element_to_be_clickable(By.XPATH, '//span[text()="Service Detail"]'))
# -- My Team button
# funeral_homes=wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="My Team"]'))).click()
# # -- My Settings button
# funeral_homes=wait.until(EC.element_to_be_clickable(By.XPATH, '//span[text()="My Settings"]'))
# -- Invite new team member
# invite_new_team_member = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, '//span[class()="jss1001"]'))).click()
# elem.send_keys("BrowserStack")
# elem.submit()
print(driver.title)
# driver.quit()


# // * [ @ id = "downshift-simple-input"]
# / html / body / div[10] / div[2] / div / div[2] / div / div / div / div[1] / div[1] / div / div / input
# < input aria - invalid = "false" autocomplete = "off" class = "jss864 jss849 jss2421" id = "downshift-simple-input" name = "off" placeholder = "Start typing to see locations…" required = "" type = "text" value = "" >
# #downshift-simple-input
# document.querySelector("#downshift-simple-input")
# < input aria - invalid = "false" autocomplete = "off" class = "jss864 jss849 jss2421" id = "downshift-simple-input" name = "off"
# placeholder="Start typing to see locations…" required="" type="text" value="">
