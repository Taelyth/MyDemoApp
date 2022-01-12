import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

import credentials

ambiente = 'local'

if ambiente == 'local':
    caps = {
        "platformName": "Android",
        "appium:platformVersion": "11.0",
        "appium:automationName": "uiautomator2",
        #"browserName": "",
        "appium:appiumVersion": "1.22.0",
        "appium:deviceName": "emulator5554",
        "appium:deviceOrientation": "portrait",
        "appium:appPackage": "com.saucelabs.mydemoapp.android",
        "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
        #"appium:ensureWebviewsHavePages": True,
        #"appium:nativeWebScreenshot": True, "appium:newCommandTimeout": 3600,
        #"appium:connectHardwareKeyboard": True
        }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
elif ambiente == 'saucelabs':
    caps = {
        "platformName": "Android",
        "appium:platformVersion": "9.0",
        #"browserName": "",
        #"appium:appiumVersion": "1.22.0",
        "appium:deviceName": "Samsung Galaxy S9 FHD GoogleAPI Emulator",
        "appium:deviceOrientation": "portrait",
        "appium:app": "storage:filename=mda-1.0.9-11.apk",
        "appium:appPackage": "com.saucelabs.mydemoapp.android",
        "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
        #"appium:ensureWebviewsHavePages": True,
        #"appium:nativeWebScreenshot": True,
        #"appium:newCommandTimeout": 0,
        #"appium:connectHardwareKeyboard": True
        }
    _credentials = credentials.SAUCE_USERNAME + ':' + credentials.SAUCE_ACCESS_KEY
    _url = 'https://' + _credentials + '@ondemand.us-west-1.saucelabs.com:443/wd/hub'

    driver = webdriver.Remote(_url, caps)


el1 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"Displays selected product\"])[1]")
el1.click()
el2 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/productTV")
el2.click()
el3 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/priceTV")
el3.click()
TouchAction(driver).press(x=956, y=2058).move_to(x=898, y=451).release().perform()

el4 = driver.find_element_by_xpath(
    "//android.widget.FrameLayout[@content-desc=\"Container for fragments\"]/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView")
el4.click()
# time.sleep(5)
# TouchAction(driver).press(x=378, y=1531).move_to(x=276, y=1705).release().perform()

el5 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"Displays color of product\"])[3]")
el5.click()
el6 = driver.find_element_by_accessibility_id("Increases number of products")
el6.click()
el7 = driver.find_element_by_accessibility_id("Tap to add product to cart")
el7.click()
el9 = driver.find_element_by_xpath(
    "//android.widget.RelativeLayout[@content-desc=\"Displays number of items in your cart\"]/android.widget.ImageView")
el9.click()
el10 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/productTV")
el10.click()
el11 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/titleTV")
el11.click()
el12 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/priceTV")
el12.click()
el13 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/itemsTV")
el13.click()
el14 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/totalPriceTV")
el14.click()

driver.quit()
