from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
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
print("\nSession started!\n")

#when all images on current page are processes, scroll to next page.
def swipe_to_next_page():
    touch_action = PointerInput("touch", "touch")
    actions = ActionBuilder(driver, mouse=touch_action)
    
    actions.pointer_action.move_to_location(561, 1782)
    actions.pointer_action.pointer_down()
    actions.pointer_action.move_to_location(561, 438)
    actions.pointer_action.pointer_up()
    actions.perform()

    actions = ActionBuilder(driver, mouse=touch_action)
    actions.pointer_action.move_to_location(594, 1618)
    actions.pointer_action.pointer_down()
    actions.pointer_action.move_to_location(594, 1040)
    actions.pointer_action.pointer_up()
    actions.perform()

    actions = ActionBuilder(driver, mouse=touch_action)
    actions.pointer_action.move_to_location(569, 455)
    actions.pointer_action.pointer_down()
    actions.pointer_action.move_to_location(569, 365)
    actions.pointer_action.pointer_up()
    actions.perform()

passed_tests = 0
failed_tests = 0
expected_outputs = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
    "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
    "30", "31", "32", "33", "34"
]

#onboarding stage
agree_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.education.android.h.intelligence:id/agreeBtn")))
agree_button.click()

for _ in range(4):
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

try:
    #pick the image
    select_image_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("com.education.android.h.intelligence:id/photoPreview").instance({0})')
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

    #check if text container has expected output
    expected_output = expected_outputs[0]
    if expected_output in container_text:
        print("----------------------------")
        print("Test Case 0 Passed\n")
        print("Actual: ", container_text, "\n")
        print("Expected: ", expected_output)
        print("----------------------------\n")
        passed_tests+=1
    else:
        print("----------------------------")
        print("Test Case 0 Failed\n")
        print("Actual: ", container_text, "\n")
        print("Expected: ", expected_output)
        print("----------------------------\n")
        failed_tests+=1
except Exception as e:
    expected_output = expected_outputs[0]
    error_dismiss_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.education.android.h.intelligence:id/container")))
    error_dismiss_button.click()
    print("----------------------------")
    print("Test Case 0 Failed\n")
    print("Actual: Image is blurry or unclear", "\n")
    print("Expected: ", expected_output)
    print("----------------------------\n")
    failed_tests+=1
finally:
    return_home_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(0)")
    return_home_button.click()

#loops through remaining images in album
for i in range(1,35):
    try:
        #click on image album
        input_image_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.education.android.h.intelligence:id/pickAlbum")))
        input_image_button.click()

        if(i >= 18):
            print("Swiping")
            swipe_to_next_page()

        time.sleep(1)

        try:
            #pick the image
            select_image_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.education.android.h.intelligence:id/photoPreview").instance({i % 18}))')
            select_image_button.click()
        except Exception as e:
            print(f'Image instance {i} not found after scrolling: {e}')
            failed_tests+=1
            continue

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

        #check if text container has expected output
        expected_output = expected_outputs[i]
        if expected_output in container_text:
            print("----------------------------")
            print(f'Test case {i} passed\n')
            print("Actual: ", container_text, "\n")
            print("Expected: ", expected_output)
            print("----------------------------\n")
            passed_tests+=1
        else:
            print("----------------------------")
            print(f'Test case {i} failed\n')
            print("Actual: ", container_text, "\n")
            print("Expected: ", expected_output)
            print("----------------------------\n")
            failed_tests+=1
    except Exception as e:
        expected_output = expected_outputs[i]
        error_dismiss_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.education.android.h.intelligence:id/container")))
        error_dismiss_button.click()
        print("----------------------------")
        print(f'Test case {i} failed\n')
        print("Actual: Image is blurry or unclear", "\n")
        print("Expected: ", expected_output)
        print("----------------------------\n")
        failed_tests+=1
    finally:
        return_home_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(0)")
        return_home_button.click()


time.sleep(5)

print(f'Passed tests: {passed_tests}')
print(f'Failed tests: {failed_tests}')
print(f'Pass rate: {passed_tests}/35')
print(f'Pass percentage: {(passed_tests/2) * 100}%')

driver.quit()