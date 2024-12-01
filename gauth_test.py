from appium import webdriver
from appium.options.common import AppiumOptions

options = AppiumOptions()
options.set_capability("platformName", "Android")
options.set_capability("platformVersion", "15.0")
options.set_capability("deviceName", "emulator-5554")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("appPackage", "com.education.android.h.intelligence")
options.set_capability("appActivity", "com.ss.android.business.flutter.splash.SplashActivity")

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723",
    options=options
)

print("Session started successfully!")
print(driver.page_source)

driver.quit()
