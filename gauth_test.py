from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#configurations for Gauth and emulator
options = AppiumOptions()
options.set_capability("platformName", "Android")
options.set_capability("platformVersion", "15.0")
options.set_capability("deviceName", "emulator-5554")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("appPackage", "com.education.android.h.intelligence")
options.set_capability("appActivity", "com.ss.android.business.flutter.splash.SplashActivity")

#start testing session
driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723",
    options=options
)
print("Session started successfully!")

#onboarding stage
agree_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.education.android.h.intelligence:id/agreeBtn")))
agree_button.click()

continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.education.android.h.intelligence:id/btn")))
continue_button.click()

continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.education.android.h.intelligence:id/btn")))
continue_button.click()

continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.education.android.h.intelligence:id/btn")))
continue_button.click()

continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.education.android.h.intelligence:id/btn")))
continue_button.click()

time.sleep(3)

exit_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.lynx.tasm.behavior.ui.LynxFlattenUI").instance(1)')
exit_button.click()

#permissions
permission_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
permission_button.click()

permission_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button")))
permission_button.click()

time.sleep(3)

#switch to math image input
math_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Math")')
math_button.click()

#click on image album and provide permissions
input_image_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.education.android.h.intelligence:id/pickAlbum")))
input_image_button.click()

permission_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_all_button")))
permission_button.click()

time.sleep(1)

#pick the image
select_image_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.education.android.h.intelligence:id/photoPreview\").instance(1)")
select_image_button.click()

#submit the image
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.education.android.h.intelligence:id/btnSubmit")))
submit_button.click()

time.sleep(10)

#grab the answer container
answer_container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((AppiumBy.ID, "com.education.android.h.intelligence:id/answerContentContainer"))
)

#place all elements of the answer_container into a text container.
child_elements = answer_container.find_elements(AppiumBy.XPATH, ".//*")
container_text = "".join([child.text for child in child_elements if child.text.strip()])
container_text = container_text.replace(" ", "")
print("Answer Container Text: ", container_text)

#check if text container has expected output
expected_output = "4𝑎+6"
if expected_output in container_text:
    print("Test passed")
else:
    print("Test failed")

#go back home
return_home_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(0)")
return_home_button.click()

time.sleep(5)

driver.quit()