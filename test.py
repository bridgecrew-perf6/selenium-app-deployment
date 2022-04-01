from socket import timeout
from time import sleep, time
from django.forms import PasswordInput
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By



play_console_link = "https://play.google.com/console/u/1/developers/4962177018327627015/app-list?onboardingflow=signup"
# play_console_link = "https://play.google.com/console/u/0/developers/4962177018327627015/app/4973730883163465011/app-content/summary"
username = "relson@chesslang.com"
password = "vini@0507"
appname = "test"

loading_page_delay = 20

privacy_policy_url = "https://privacypolicychess.com/lotus-chess-academy/"

ans_name = "test user"
ans_usename = "testapp"
ans_password = "kasparov"

email = "relson@chesslang.com"

csv_file_path = "C:\\Users\\Remson\\Desktop\\chesslang\\data_safety_export.csv"

short_description = "Short description"
long_description = "Long desciption"
app_icon_filepath = "C:\\Users\\Remson\\Desktop\\chesslang\\academy-images\\Piper Chess Club\\App Icon.png"
feature_graphic_filepath = "C:\\Users\\Remson\\Desktop\\chesslang\\academy-images\\Piper Chess Club\\Feature Graphic.png"
phone_ss_filepath = "C:\\Users\\Remson\\Desktop\\chesslang\\Screenshots\\Screenshots\\Phone\\"
tablet_ss_filepath = "C:\\Users\\Remson\\Desktop\\chesslang\\Screenshots\\Screenshots\\Tab\\"

aab_file_location = ""
release_name = "First release"
release_notes = " <en-US> <br> First Release <br> </en-US>"

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Remson\\AppData\\Local\\Google\\Chrome\\User Data/profile1")

driver = webdriver.Chrome(executable_path=r"C:\Users\Remson\Desktop\chromedriver_win32\chromedriver.exe", chrome_options=options)
driver.get(play_console_link)

sleep(2)

def login():

    emailID = driver.find_element_by_id("identifierId")
    emailID.send_keys(username, Keys.ARROW_DOWN)

    enter = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
    enter.click()
    sleep(2)

    passwordTxtBox = driver.find_element_by_name("password")
    passwordTxtBox.send_keys(password)

    enter = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
    enter.click()
    sleep(20)

#create app button
def createApp():
    driver.implicitly_wait(5)

    createBtn = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-list-page/console-page-header/div/div/div/console-header/div/div/div[1]/div[2]/div/console-button-set/div/material-button/button')
    createBtn.click()
    driver.implicitly_wait(5)

    try:
        appNameTextField = WebDriverWait(driver, loading_page_delay).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='App name']//div//div//input[@type='text']")))
    except TimeoutException:
        print ("Failed to load page")

        
    appNameTextField.click()
    appNameTextField.send_keys(appname)
    driver.implicitly_wait(1)

    is_app_radiobtn = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/create-new-app-page/console-form/console-form-row[3]/div/div[2]/div[1]/material-radio-group/material-radio[1]')
    is_app_radiobtn.click()
    driver.execute_script("arguments[0].scrollIntoView();", is_app_radiobtn)
    driver.implicitly_wait(1)

    is_free_radiobtn = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/create-new-app-page/console-form/console-form-row[4]/div/div[2]/div[1]/material-radio-group/material-radio[1]')
    is_free_radiobtn.click()

    driver.implicitly_wait(1)

    developer_program_policies_chckbox = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/create-new-app-page/console-form/console-form-row[5]/div/div[2]/div[1]/material-checkbox/div[1]/input').click()
    driver.implicitly_wait(1)

    us_export_laws_chckbox = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/create-new-app-page/console-form/console-form-row[6]/div/div[2]/div[1]/material-checkbox/div[1]/input').click()

    create_app_btn = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/create-new-app-page/form-bottom-bar/bottom-bar-base/div/div/div/div[2]/console-button-set/div/material-button[1]/button')
    create_app_btn.click()


def appContent():
    app_content_btn = driver.find_element_by_xpath("//div[7]//expandable-container[1]//div[1]//div[1]//navigation-subtree[2]//navigation-element[1]//div[1]//material-ripple[1]")
    driver.execute_script("arguments[0].scrollIntoView();", app_content_btn)
    driver.implicitly_wait(1)
    app_content_btn.click()

def dashBoard():
    dashboarod_btn = driver.find_element_by_xpath("//body/div/root/console-chrome[@helpcentercontext='Play Console']/div/material-drawer/navigation-bar/div/div[1]/navigation-subtree[1]/navigation-element[1]/div[1]/material-ripple[1]")
    driver.execute_script("arguments[0].scrollIntoView();", dashboarod_btn)
    driver.implicitly_wait(1)
    dashboarod_btn.click()
    driver.implicitly_wait(2)

def privacyPolicy():

    try:
        privacy_content_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='console-root-021280']/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-summary-page/console-section/div/div/policies-list/div[1]/policy/div/console-block-1-column/div/div/console-button-set/div/material-button/button/div")))       
    except TimeoutException:
        print ("Loading took too much time!")

    # privacy_content_btn = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-summary-page/console-section/div/div/policies-list/div[1]/policy/div/console-block-1-column/div/div/console-button-set/div/material-button/button/div')
    privacy_content_btn.click()
    driver.implicitly_wait(3)

    privacy_content_url_textbox = driver.find_element_by_xpath('/html/body/div[1]/root/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-privacy-policy-page/div/console-block-1-column[2]/div/div/console-form/material-input/label/input')
    privacy_content_url_textbox.click()
    privacy_content_url_textbox.send_keys(privacy_policy_url)

    save_btn = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-privacy-policy-page/div/form-bottom-bar/bottom-bar-base/div/div/div/div[2]/console-button-set/div/material-button[1]/button')
    save_btn.click()
    sleep(3)
def ads():
    try:
        ads_start_btn = WebDriverWait(driver, loading_page_delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-summary-page/console-section[1]/div/div/policies-list/div[1]/policy/div/console-block-1-column/div/div/console-button-set/div/material-button/button/div')))
    except TimeoutException:
        print ("Failed to load page")

    ads_start_btn.click()
    driver.implicitly_wait(3)

    ads_chkbx = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-ads-declaration-page/div/console-block-1-column[2]/div/div/console-form/console-form-row/div/div[2]/div[1]/material-radio-group/material-radio[2]')
    ads_chkbx.click()

    save_btn = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-ads-declaration-page/div/form-bottom-bar/bottom-bar-base/div/div/div/div[2]/console-button-set/div/material-button[2]/button/div')
    save_btn.click()
    sleep(2)

    app_content_back = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-ads-declaration-page/console-page-header/div/div/div/console-button-set/div/material-button/button/div')
    app_content_back.click()
    driver.implicitly_wait(5)
def appAccess():
    try:
        app_access_start_btn = WebDriverWait(driver, loading_page_delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-summary-page/console-section[1]/div/div/policies-list/div[1]/policy/div/console-block-1-column/div/div/console-button-set/div/material-button/button/div')))
    except TimeoutException:
        print ("Failed to load page")
        
    app_access_start_btn.click()
    driver.implicitly_wait(5)


    restricted_funtion_chckbox = driver.find_element_by_xpath('//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-testing-credentials-page/console-block-1-column/div/div/console-form/console-form-expandable-section[2]/div/div/material-radio/div[2]')
    restricted_funtion_chckbox.click()
    driver.implicitly_wait(5)

    add_new_instruction = driver.find_element_by_xpath("//body//div//console-block-1-column//console-button-set//div//div[1]")
    driver.execute_script("arguments[0].click();", add_new_instruction)
    driver.implicitly_wait(2)
    sleep(1)

    name = driver.find_element_by_xpath('//*[@id="default-acx-overlay-container"]/div[2]/div/focus-trap/div[2]/relative-popup/div/div/div[2]/console-block-1-column/div/div/console-form/console-form-row/div/div[2]/div[1]/material-input/label/input')
    name.click()
    name.send_keys(ans_name)

    username = driver.find_element_by_xpath('//*[@id="default-acx-overlay-container"]/div[2]/div/focus-trap/div[2]/relative-popup/div/div/div[2]/console-block-1-column/div/div/console-form/div/console-form-row[1]/div/div[2]/div[1]/material-input/label/input')
    username.click()
    username.send_keys(ans_usename)

    password = driver.find_element_by_xpath('//*[@id="default-acx-overlay-container"]/div[2]/div/focus-trap/div[2]/relative-popup/div/div/div[2]/console-block-1-column/div/div/console-form/div/console-form-row[2]/div/div[2]/div[1]/material-input/label/input')
    password.click()
    password.send_keys(ans_password)
    driver.implicitly_wait(1)


    apply_btn = driver.find_element_by_xpath("(//div[normalize-space()='Apply'])[1]")
    apply_btn.click()

    driver.implicitly_wait(2)

    save_btn = driver.find_element_by_xpath("(//div[normalize-space()='Save'])[1]")
    save_btn.click()

    sleep(3)

    

def contentRating():
    try:
        contentRating = WebDriverWait(driver, loading_page_delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-summary-page/console-section[1]/div/div/policies-list/div[1]/policy/div/console-block-1-column/div/div/console-button-set/div/material-button/button/div')))
        contentRating.click()
    except TimeoutException:
        print ("Failed to load page")

    
    driver.implicitly_wait(5)

    start_questionaire_btn = driver.find_element_by_xpath("//div[contains(text(),'Start questionnaire')]")
    start_questionaire_btn.click()

    driver.implicitly_wait(5)

    email_txtbox = driver.find_element_by_xpath("//input[@type='email']")
    email_txtbox.send_keys(email)

    category_chckbx = driver.find_element_by_xpath("(//input[@type='radio'])[3]")
    category_chckbx.click()
    driver.implicitly_wait(1)

    next_btn = driver.find_element_by_xpath("//material-button[@debug-id='next-button']")
    next_btn.click()

    driver.implicitly_wait(5)
    sleep(3)

    checkbox1 = driver.find_element_by_xpath("(//input[@type='radio'])[2]").click()
    driver.implicitly_wait(3)

    checkbox1 = driver.find_element_by_xpath("(//input[@type='radio'])[4]").click()
    driver.implicitly_wait(3)

    checkbox2 = driver.find_element_by_xpath("(//input[@type='radio'])[6]")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox2)
    driver.implicitly_wait(1)
    checkbox2.click()
    driver.implicitly_wait(1)

    checkbox3 = driver.find_element_by_xpath("(//input[@type='radio'])[8]")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox3)
    driver.implicitly_wait(1)
    checkbox3.click()
    driver.implicitly_wait(3)
 

    checkbox4 = driver.find_element_by_xpath("(//input[@type='radio'])[10]")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox4)
    driver.implicitly_wait(1)
    driver.execute_script("arguments[0].click();", checkbox4)
    driver.implicitly_wait(3)

    checkbox5 = driver.find_element_by_xpath("(//input[@type='radio'])[12]")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox5)
    driver.implicitly_wait(3)
    checkbox5.click()
    driver.implicitly_wait(1)

    checkbox6 = driver.find_element_by_xpath("(//input[@type='radio'])[14]")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox6)
    driver.implicitly_wait(3)
    checkbox6.click()
    driver.implicitly_wait(1)

    checkbox7 = driver.find_element_by_xpath("(//input[@type='radio'])[15]")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox7)
    driver.implicitly_wait(3)
    checkbox7.click()
    driver.implicitly_wait(1)

    save_btn = driver.find_element_by_xpath("(//div[normalize-space()='Save'])[1]").click()
    net_btn = driver.find_element_by_xpath("(//div[contains(text(),'Next')])[1]").click()
    driver.implicitly_wait(2)
    submit = driver.find_element_by_xpath("(//div[normalize-space()='Submit'])[1]").click()

    sleep(1)

def targetAudience():
    try:
        target_audience_start_btn = WebDriverWait(driver, loading_page_delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="console-root-021280"]/console-chrome/div/div/div/div/div[1]/page-router-outlet/page-wrapper/div/app-content-summary-page/console-section[1]/div/div/policies-list/div[1]/policy/div/console-block-1-column/div/div/console-button-set/div/material-button/button/div')))
    except TimeoutException:
        print ("Failed to load page")

    target_audience_start_btn.click()
    driver.implicitly_wait(2)

    checkbox = driver.find_element_by_xpath("(//input[@type='checkbox'])[1]")
    driver.execute_script("arguments[0].scrollIntoView();", checkbox)
    driver.implicitly_wait(2)
    checkbox.click()

    checkbox = driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
    checkbox = driver.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
    checkbox = driver.find_element_by_xpath("(//input[@type='checkbox'])[4]").click()
    checkbox = driver.find_element_by_xpath("(//input[@type='checkbox'])[5]").click()
    checkbox = driver.find_element_by_xpath("(//input[@type='checkbox'])[6]").click()

    driver.implicitly_wait(1)
    next_btn = driver.find_element_by_xpath("(//div[normalize-space()='Next'])[1]").click()
    driver.implicitly_wait(2)
    ok_btn = driver.find_element_by_xpath("(//div[normalize-space()='OK'])[1]").click()

    driver.implicitly_wait(1)

    ##### Part 2 
    personal_indo_radio = driver.find_element_by_xpath("//material-radio[1]//div[1]//input[1]").click()
    legal_chckbx = driver.find_element_by_xpath("(//input[@type='checkbox'])[1]").click()
    next_btn = driver.find_element_by_xpath("(//div[normalize-space()='Next'])[1]").click()
    driver.implicitly_wait(2)
    next_btn = driver.find_element_by_xpath("(//div[normalize-space()='Next'])[1]").click()
    driver.implicitly_wait(2)
    sleep(2)


    #### Part 4
    join_btn1 = driver.find_element_by_xpath("(//input[@type='radio'])[1]")
    driver.execute_script("arguments[0].scrollIntoView();", join_btn1)

    join_btn = driver.find_element_by_xpath("(//input[@type='radio'])[2]").click()
    driver.implicitly_wait(2)
    next_btn = driver.find_element_by_xpath("(//div[normalize-space()='Next'])[1]").click()

    driver.implicitly_wait(2)
    save_btn = driver.find_element_by_xpath("(//div[normalize-space()='Save'])[1]").click()

    back = driver.find_element_by_xpath("(//div)[303]").click()
    sleep(1)

def newsApp():
    driver.implicitly_wait(2)
    try:
        start_btn = WebDriverWait(driver, loading_page_delay).until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Start')])[1]")))
    except TimeoutException:
        print ("Failed to load page")

    start_btn.click()
    driver.implicitly_wait(2)

    is_new_app = driver.find_element_by_xpath("(//input[@type='radio'])[1]").click()
    save_btn = driver.find_element_by_xpath("(//div[normalize-space()='Save'])[1]").click()

    driver.implicitly_wait(2)
    sleep(1)
    back_btn = driver.find_element_by_xpath("//button[@aria-label='Go back to App content']//div").click()
    sleep(1)

def covidApp():
    try:
        start_btn = WebDriverWait(driver, loading_page_delay).until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Start')])[1]")))
    except TimeoutException:
        print ("Failed to load page")

    start_btn.click()
    driver.implicitly_wait(2)

    is_covid_app = driver.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()
    save_btn = driver.find_element_by_xpath("(//div[normalize-space()='Save'])[1]").click()
    sleep(1)
    driver.implicitly_wait(2)

    back_btn = driver.find_element_by_xpath("//button[@aria-label='Go back to App content']//div").click()

def dataSatefy():
    try:
        start_btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Start')])[1]")))
    except TimeoutException:
        print ("Failed to load page")

    start_btn.click()
    driver.implicitly_wait(2)

    import_csv_btn = driver.find_element_by_xpath("(//div[normalize-space()='Import from CSV'])[1]").click()
    sleep(2)
    upload_btn = driver.find_element_by_xpath("(//button[@type='submit'])[15]").click()
    sleep(1)
    pyautogui.write(csv_file_path)
    pyautogui.press('enter')
    # sleep(10)
    
    try:
        import_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//material-button[@debug-id='import-button']//button[@type='submit']")))       
    except TimeoutException:
        print ("Loading took too much time!")

    import_btn.click()
    driver.implicitly_wait(2)
    confirm = driver.find_element_by_xpath("//material-button[@debug-id='yes-button']//button[@type='submit']").click()
    driver.implicitly_wait(2)
    next_btn = driver.find_element_by_xpath("(//div[contains(text(),'Next')])[1]").click()
    driver.implicitly_wait(2)
    next_btn = driver.find_element_by_xpath("(//div[contains(text(),'Next')])[1]").click()
    driver.implicitly_wait(2)
    next_btn = driver.find_element_by_xpath("(//div[contains(text(),'Next')])[1]").click()
    driver.implicitly_wait(2)
    save_btn = driver.find_element_by_xpath("(//div[contains(text(),'Save')])[1]").click()
    sleep(1)

def storeSetting():
    try:
        contact_details_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//div[@aria-label='Select an app category and provide contact details'])[1]")))       
    except TimeoutException:
        print ("Loading took too much time!")

    driver.execute_script("arguments[0].click();", contact_details_btn)
    sleep(5)

    driver.implicitly_wait(2)

    category_dropdown = driver.find_element_by_xpath("(//div[@role='button'])[9]").click()

    driver.implicitly_wait(1)

    category_option = driver.find_element_by_xpath("//material-select-dropdown-item[9]").click()
    driver.implicitly_wait(2)

    scroll = driver.find_element_by_xpath("(//div[contains(text(),'Manage tags')])[1]")
    driver.execute_script("arguments[0].scrollIntoView();", scroll)

    email_txt = driver.find_element_by_xpath("//div[@aria-label='Email address']//div//div//material-input//label")
    # driver.execute_script("arguments[0].scrollIntoView();", email_txt)
    driver.implicitly_wait(1)
    email_txt.click()
    email_txt.send_keys(email)

    save = driver.find_element_by_xpath("(//div[normalize-space()='Save'])[1]").click()
    sleep(1)

def storeList():
    try:
        setup = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//div[@aria-label='Set up your store listing'])[1]")))
    except TimeoutException:
        print ("Failed to load page")

    driver.execute_script("arguments[0].click();", setup)

    driver.implicitly_wait(2)

    appName = driver.find_element_by_xpath("(//input[@aria-label='Name of the app'])[1]")
    driver.execute_script("arguments[0].scrollIntoView();", appName)

    driver.implicitly_wait(2)


    short_description_txt = driver.find_element_by_xpath("//input[@aria-label='Short description of the app']")
    short_description_txt.click()
    short_description_txt.send_keys(short_description)
    driver.implicitly_wait(2)

    long_description_txt = driver.find_element_by_xpath("//textarea[@aria-label='Full description of the app']")
    long_description_txt.click()
    long_description_txt.send_keys(long_description)

    driver.implicitly_wait(2)



    upload_app_icon = driver.find_element_by_xpath("//app-image-uploader[@debug-id='icon-uploader']//div//material-button[@aria-disabled='false']//div")
    driver.execute_script("arguments[0].click();", upload_app_icon)
    sleep(1)
    pyautogui.write(app_icon_filepath)    
    pyautogui.press('enter')

    sleep(0.5)

    feature_graphic = driver.find_element_by_xpath("//app-image-uploader[@debug-id='feature-graphic-uploader']//div//button[@type='submit']")
    driver.execute_script("arguments[0].click();", feature_graphic)
    sleep(1)
    pyautogui.write(feature_graphic_filepath)    
    pyautogui.press('enter')

    sleep(0.5)


    phone_ss = driver.find_element_by_xpath("//app-screenshots-uploader[@debug-id='phone-screenshot-uploader']//div//material-button[@aria-disabled='false']//div")
    driver.execute_script("arguments[0].click();", phone_ss)
    sleep(1)
    pyautogui.write(phone_ss_filepath) 
    pyautogui.press('enter')
    for x in range(1,9):
        pyautogui.write('\"Huawei P8 Screenshot ' + str(x) + '\" ')    
    pyautogui.press('enter')
    sleep(1)
    driver.implicitly_wait(2)

    sleep(0.5)


    tab10 = driver.find_element_by_xpath("//app-screenshots-uploader[@debug-id='regular-tablet-screenshot-uploader']//div//material-button[@aria-disabled='false']//div")
    driver.execute_script("arguments[0].scrollIntoView(false);", tab10)

    tab7 = driver.find_element_by_xpath("//app-screenshots-uploader[@debug-id='small-tablet-screenshot-uploader']//div//material-button[@aria-disabled='false']//div").click()
    sleep(1)
    pyautogui.write(tablet_ss_filepath) 
    pyautogui.press('enter')
    for x in range(1,9):
        pyautogui.write('\"HTC Nexus 9 Screenshot ' + str(x) + '\" ')    
    pyautogui.press('enter')
    sleep(1)


    tab10 = driver.find_element_by_xpath("//app-screenshots-uploader[@debug-id='regular-tablet-screenshot-uploader']//div//material-button[@aria-disabled='false']//div")
    driver.execute_script("arguments[0].scrollIntoView();", tab10)
    sleep(1)
    tab10.click()
    sleep(1)
    pyautogui.write(tablet_ss_filepath) 
    pyautogui.press('enter')
    for x in range(1,9):
        pyautogui.write('\"HTC Nexus 9 Screenshot ' + str(x) + '\" ')    
    pyautogui.press('enter')

    save_btn = driver.find_element_by_xpath("//material-button[@debug-id='save-button']//button[@type='submit']").click()



    try:
      error_btn = WebDriverWait(driver, 120).until(EC.invisibility_of_element((By.XPATH, "(//icon-text[@debug-id='languages-with-errors-message'])[1]")))       
    except TimeoutException:
        print ("Loading took too much time!")

    save_btn = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "//material-button[@debug-id='save-button']//button[@type='submit']")))       
    save_btn.click()
    
    
    sleep(1)

def production():
    try:
        production_btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[3]//expandable-container[1]//div[1]//div[1]//navigation-subtree[2]//navigation-element[1]//div[1]//material-ripple[1]")))
    except TimeoutException:
        print ("Failed to load page")

    production_btn.click()
    driver.implicitly_wait(1)

    try:
        country_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//tab-button[@aria-label='Countries / regions']//material-ripple")))
    except TimeoutException:
        print ("Failed to load page")

    country_tab.click()
    add_country = driver.find_element_by_xpath("//div[normalize-space()='Add countries / regions']").click()
    driver.implicitly_wait(1)

    select_all_county = driver.find_element_by_xpath("//mat-checkbox[@aria-label='Select all rows']").click()
    driver.implicitly_wait(2)

    add_country_btn = driver.find_element_by_xpath("//material-button[@debug-id='overlay-confirm-button']//div[contains(text(),'Add countries / regions')]").click()
    driver.implicitly_wait(1)
    confirm_btn = driver.find_element_by_xpath("(//div[normalize-space()='Add'])[1]").click()
    sleep(2)
    driver.implicitly_wait(2)

    release_dashboard_tab = driver.find_element_by_xpath("(//tab-button[@aria-label='Release dashboard'])[1]").click()
    driver.implicitly_wait(1)

    create_new_release_btn = driver.find_element_by_xpath("(//div[contains(text(),'Create new release')])[2]").click()
    driver.implicitly_wait(5)

    release_name_txt = driver.find_element_by_xpath("//div[@aria-label='Release name']//div//div//material-input")
    driver.execute_script("arguments[0].scrollIntoView(false);", release_name_txt)

    upload_aab_file = driver.find_element_by_xpath("(//button[@type='submit'])[7]").click()
    sleep(1)
    pyautogui.write("C:\\Users\\Remson\\Desktop\\chesslang\\app-release.aab")
    pyautogui.press('enter')
    sleep(3)

    release_name_txt = driver.find_element_by_xpath("//div[@aria-label='Release name']//div//div//material-input")
    driver.execute_script("arguments[0].scrollIntoView();", release_name_txt)

    release_name_txt.send_keys(release_name)

    release_notes_txt = driver.find_element_by_xpath("(//textarea[@aria-label='Release notes'])[1]")
    release_notes_txt.clear()
    release_notes_txt.send_keys(release_name)

createApp()
driver.implicitly_wait(5)

appContent()
privacyPolicy()
driver.implicitly_wait(5)

appContent()
driver.implicitly_wait(3)
ads()
driver.implicitly_wait(5)

appContent()
driver.implicitly_wait(2)
appAccess()
driver.implicitly_wait(2)


appContent()
driver.implicitly_wait(2)
contentRating()
driver.implicitly_wait(2)

appContent()
driver.implicitly_wait(2)
targetAudience()
driver.implicitly_wait(2)

appContent()
driver.implicitly_wait(2)
newsApp()
driver.implicitly_wait(2)

appContent()
driver.implicitly_wait(2)
covidApp()
driver.implicitly_wait(2)

appContent()
driver.implicitly_wait(2)
dataSatefy()
driver.implicitly_wait(2)

dashBoard()
driver.implicitly_wait(2)
storeSetting()
driver.implicitly_wait(2)

dashBoard()
driver.implicitly_wait(2)
storeList()
driver.implicitly_wait(2)

production()



sleep(5)
# driver.close()


