# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9.0"
caps["browserName"] = ""
caps["appium:appiumVersion"] = "1.22.0"
caps["appium:deviceName"] = "Samsung Galaxy S9 FHD GoogleAPI Emulator"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:app"] = "storage:filename=mda-1.0.9-11.apk"
caps["appium:appPackage"] = "com.saucelabs.mydemoapp.android"
caps["appium:appActivity"] = "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 0
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://ondemand.us-west-1.saucelabs.com:80/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("Tap to view menu")
el1.click()
el2 = driver.find_element_by_xpath("//androidx.recyclerview.widget.RecyclerView[@content-desc=\"Recycler view for menu\"]/android.view.ViewGroup[11]/android.widget.TextView")
el2.click()
el3 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/nameET")
el3.click()
el4 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/passwordET")
el4.click()
el5 = driver.find_element_by_accessibility_id("Tap to view menu")
el5.click()
driver.back()
driver.back()
el6 = driver.find_element_by_accessibility_id("Tap to view menu")
el6.click()
el7 = driver.find_element_by_xpath("//androidx.recyclerview.widget.RecyclerView[@content-desc=\"Recycler view for menu\"]/android.view.ViewGroup[11]/android.widget.TextView")
el7.click()
el8 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/passwordET")
el8.click()
driver.back()
el9 = driver.find_element_by_accessibility_id("Tap to login with given credentials")
el9.click()
el10 = driver.find_element_by_accessibility_id("Tap to view menu")
el10.click()
el11 = driver.find_element_by_xpath("//androidx.recyclerview.widget.RecyclerView[@content-desc=\"Recycler view for menu\"]/android.view.ViewGroup[1]/android.widget.TextView[2]")
el11.click()

#
el1 = driver.find_element_by_xpath("//androidx.recyclerview.widget.RecyclerView[@content-desc=\"Displays all products of catalog\"]/android.view.ViewGroup[1]/android.widget.TextView[1]")
el1.click()
el2 = driver.find_element_by_xpath("//androidx.recyclerview.widget.RecyclerView[@content-desc=\"Displays all products of catalog\"]/android.view.ViewGroup[1]/android.widget.TextView[2]")
el2.click()
el3 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/productTV")
el3.click()
#

el12 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"Displays selected product\"])[1]")
el12.click()
el13 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/productTV")
el13.click()
el14 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/priceTV")
el14.click()

el2 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/noTV")
el2.click()
el3 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"Displays color of product\"])[3]")
el3.click()
TouchAction(driver).press(x=531, y=661).move_to(x=531, y=1158).release().perform()

TouchAction(driver).press(x=441, y=1506).move_to(x=437, y=1114).release().perform()

el4 = driver.find_element_by_accessibility_id("Tap to add product to cart")
el4.click()
el4.click()
el5 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/cartIV")
el5.click()
TouchAction(driver).press(x=740, y=691).move_to(x=729, y=1099).release().perform()

el6 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/noTV")
el6.click()
el7 = driver.find_element_by_accessibility_id("Reduces number of products")
el7.click()
el8 = driver.find_element_by_accessibility_id("Confirms products for checkout")
el8.click()
el9 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/nameET")
el9.click()
el9.send_keys("bod@example.com")
el10 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/passwordET")
el10.click()
TouchAction(driver).tap(x=987, y=2093).perform()
TouchAction(driver).tap(x=516, y=1136).perform()
el10.send_keys("10203040")
el11 = driver.find_element_by_accessibility_id("Tap to login with given credentials")
el11.click()
el12 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/fullNameET")
el12.click()
el13 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/address1ET")
el13.click()
el13.click()
TouchAction(driver).press(x=534, y=1192).move_to(x=527, y=919).release().perform()

TouchAction(driver).tap(x=1002, y=2115).perform()
TouchAction(driver).tap(x=1009, y=2268).perform()
TouchAction(driver).tap(x=232, y=2257).perform()
TouchAction(driver).tap(x=232, y=2253).perform()
TouchAction(driver).tap(x=1002, y=2100).perform()
el14 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/cityET")
el14.click()
el15 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/stateET")
el15.click()
TouchAction(driver).press(x=620, y=1229).move_to(x=635, y=897).release().perform()

el16 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/zipET")
el16.click()
el17 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/countryET")
el17.click()
TouchAction(driver).tap(x=1028, y=2119).perform()
el17.click()
el18 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/nameET")
el18.click()
el19 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/cardNumberET")
el19.click()
TouchAction(driver).tap(x=987, y=2078).perform()
el20 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/expirationDateET")
el20.click()
el21 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/securityCodeET")
el21.click()
el22 = driver.find_element_by_accessibility_id("Select if User billing address and shipping address are same")
el22.click()
el23 = driver.find_element_by_accessibility_id("Select if User billing address and shipping address are same")
el23.click()
el24 = driver.find_element_by_accessibility_id("Saves payment info and launches screen to review checkout data")
el24.click()
el25 = driver.find_element_by_xpath(
    "//android.widget.ScrollView[@content-desc=\"Manages scrolling of views in given screen\"]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[1]")
el25.click()
el26 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/titleTV")
el26.click()
el27 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/priceTV")
el27.click()
el27.click()
el28 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/fullNameTV")
el28.click()
el29 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/addressTV")
el29.click()
el30 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/cityTV")
el30.click()
el31 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/countryTV")
el31.click()
el31.click()
el32 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/totalAmountTV")
el32.click()
el33 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/itemNumberTV")
el33.click()
el33.click()
el34 = driver.find_element_by_accessibility_id("Completes the process of checkout")
el34.click()
el35 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/completeTV")
el35.click()
el36 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/thankYouTV")
el36.click()
el37 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/swagTV")
el37.click()
el38 = driver.find_element_by_accessibility_id("Tap to open catalog")
el38.click()
el39 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/productTV")
el39.click()

driver.quit()