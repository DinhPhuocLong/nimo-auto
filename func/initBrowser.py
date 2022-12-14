from selenium import webdriver
import json
from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Browser:
    def __init__(self, url, tabDemand, timeTillNextTab, country):
        self.tabDemand = tabDemand
        self.timeTillNextTab = timeTillNextTab
        self.country = str(country)
        while True:
            # create a Firefox browser instance object Options
            profile = webdriver.FirefoxProfile()
            # disable CSS load
            profile.set_preference('permissions.default.stylesheet', 2)
            # disable images loading
            profile.set_preference('permissions.default.image', 2)
            # disable flash plug
            profile.set_preference('allow_scripts_to_close_windows', True)
            profile.set_preference('dom.allow_scripts_to_close_windows', True)
            profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)
            profile.set_preference("network.http.pipelining", True)
            profile.set_preference("network.http.proxy.pipelining", True)
            profile.set_preference("network.http.pipelining.maxrequests", 8)
            profile.set_preference("content.notify.interval", 500000)
            profile.set_preference("content.notify.ontimer", True)
            profile.set_preference("content.switch.threshold", 250000)
            profile.set_preference("browser.cache.memory.capacity", 65536)  # Increase the cache capacity.
            profile.set_preference("browser.startup.homepage", "about:blank")
            profile.set_preference("reader.parse-on-load.enabled", False)  # Disable reader, we won't need that.
            profile.set_preference("browser.pocket.enabled", False)  # Duck pocket too!
            profile.set_preference("loop.enabled", False)
            profile.set_preference("browser.chrome.toolbar_style", 1)  # Text on Toolbar instead of icons
            profile.set_preference("browser.display.show_image_placeholders",
                                   False)  # Don't show thumbnails on not loaded images.
            profile.set_preference("browser.display.use_document_colors", False)  # Don't show document colors.
            profile.set_preference("browser.display.use_document_fonts", 0)  # Don't load document fonts.
            profile.set_preference("browser.display.use_system_colors", True)  # Use system colors.
            profile.set_preference("browser.formfill.enable", False)  # Autofill on forms disabled.
            profile.set_preference("browser.helperApps.deleteTempFileOnExit", True)  # Delete temprorary files.
            profile.set_preference("browser.shell.checkDefaultBrowser", False)
            profile.set_preference("browser.startup.homepage", "about:blank")
            profile.set_preference("browser.startup.page", 0)  # blank
            profile.set_preference("browser.tabs.forceHide", True)  # Disable tabs, We won't need that.
            profile.set_preference("browser.urlbar.autoFill", False)  # Disable autofill on URL bar.
            profile.set_preference("browser.urlbar.autocomplete.enabled", False)  # Disable autocomplete on URL bar.
            profile.set_preference("browser.urlbar.showPopup", False)  # Disable list of URLs when typing on URL bar.
            profile.set_preference("browser.urlbar.showSearch", False)  # Disable search bar.
            profile.set_preference("extensions.checkCompatibility", False)  # Addon update disabled
            profile.set_preference("extensions.checkUpdateSecurity", False)
            profile.set_preference("extensions.update.autoUpdateEnabled", False)
            profile.set_preference("extensions.update.enabled", False)
            profile.set_preference("general.startup.browser", False)
            profile.set_preference("plugin.default_plugin_disabled", False)
            profile.set_preference("permissions.default.image", 2)  # Image load disabled again
            # Start the Firefox browser with custom settings
            self.driver = webdriver.Firefox(firefox_profile=profile)
            self.driver.get(url)
            self.get_site_info()
            self.loginUsingUsernamePassword()
            self.readLiveUrl()

    def raiseFuckingException(self):
        return True

    def get_site_info(self):
        print('URL:', self.driver.current_url)
        print('Title:', self.driver.title)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print('th???i gian b???t ?????u ch???y: ' + current_time)

    def loginUsingCookies(self):
        self.driver.delete_all_cookies()
        with open('cookies/nimo.json', 'r') as f:
            data = json.load(f)
            for cookie in data["cookies"]:
                cookie.pop('sameSite')
                self.driver.add_cookie(cookie)

    def loginUsingUsernamePassword(self):
        code = ""
        username = ""
        password = ""
        with open("./info.json", 'r') as f:
            data = json.load(f)
            if data["code"] == 66:
                code = "Thailand"
            if data["code"] == 84:
                code = "Vietnam"
            username = data["username"]
            password = data["password"]

        sleep(1)
        loginButton = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/div[2]/button")
        loginButton.click()
        sleep(1)
        dropDown = self.driver.find_element(By.CLASS_NAME, "nimo-area-code")
        dropDown.click()
        sleep(1)
        countryPath = '//div[text()="' + code + '"]'
        countryCode = self.driver.find_element(By.XPATH, countryPath)
        countryCode.click()
        sleep(1)
        userName = self.driver.find_element(By.CLASS_NAME, "phone-number-input")
        userName.click()
        actions = ActionChains(self.driver)
        actions.send_keys(username)
        actions.send_keys(Keys.TAB)
        actions.send_keys(password)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def chooseCountry(self):
        self.driver.maximize_window()
        sleep(3)
        chooseCountryButton = self.driver.find_elements(By.CLASS_NAME, "nimo-header-country-flag")
        chooseCountryButton[0].click()
        script = "let listCountry = document.querySelectorAll('.CountryList__item');" \
                 "let c = '" + self.country + "';"
        script += "listCountry.forEach(country => {" \
                  "attr = country.getAttribute('title');" \
                  "switch (c) {" \
                  "case 'vn':" \
                  "if ((attr === 'Vi???t nam') || (attr === 'Vietnam')) {" \
                  " country.click();" \
                  " };" \
                  "break;" \
                  "case 'gl':" \
                  "if ((attr === 'To??n c???u') || (attr === 'Global')) {" \
                  "country.click();" \
                  " };" \
                  "break;" \
                  "case 'tr':" \
                  "if ((attr === 'Th??? Nh?? K???') || (attr === 'Turkey')) {" \
                  "country.click();" \
                  " };" \
                  "break;" \
                  "case 'mr':" \
                  "if ((attr === 'Ma-r???c') || (attr === 'Morocco')) {" \
                  "country.click();" \
                  " };" \
                  "case 'ind':" \
                  "if ((attr === 'Indonesia') || (attr === 'Indonesia')) {" \
                  "country.click();" \
                  " };" \
                  "break;" \
                  " };" \
                  "" \
                  "});"
        self.driver.execute_script(script)
        sleep(4)

    def readLiveUrl(self):
        sleep(4)
        self.chooseCountry()
        self.scrollToEnd()
        liveUrls = self.driver.find_elements(By.CSS_SELECTOR, ".nimo-rc_meta__info .controlZindex")
        livesTxt = open('data/lives.txt', 'w')

        for url in liveUrls:
            livesTxt.write(url.get_attribute('href') + "\n")

        livesTxt.close()
        self.controlLiveTab()



    def scrollToEnd(self):
        breakPoint = 0
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            if breakPoint == 2:
                break
            breakPoint += 1


    def controlLiveTab(self):
        i = 0
        lives = []
        with open('data/lives.txt') as lives_file:
            for live in lives_file:
                lives.append(live.rstrip())

        while True:
            # print(i, '---------------', len(lives))
            if i != len(lives) - 1:
                if len(self.driver.window_handles) < int(self.tabDemand) + 1:
                    self.switchToOriginalWindow()
                    self.openLiveInNewTab(lives[i])
                    i += 1

            if i == len(lives) - 1 and len(self.driver.window_handles) == 1:
                self.switchToOriginalWindow()
                self.readLiveUrl()


    def openLiveInNewTab(self, url):
        self.driver.switch_to.new_window('tab')
        self.driver.get(url)
        sleep(int(self.timeTillNextTab))
        self.collectEggs()

    def collectEggs(self):
        script = "let button = document.querySelector('.pl-icon_danmu_open');" \
                 "if(button) button.click();" \
                 "collectInterval = setInterval(function(){" \
                 "const boxGift = document.querySelector('.nimo-box-gift__box');" \
                 "const collectBtn = document.querySelector('.nimo-box-gift__box__btn');" \
                 "let isBoxGift = document.querySelector('.nimo-room__chatroom__box-gift-item');" \
                 "if(!boxGift) window.close();" \
                 "if(collectBtn) collectBtn.click();" \
                 "if(window.getComputedStyle(isBoxGift).display == 'none') window.close();" \
                 "}, 1);"

        self.driver.execute_script(script)

    def switchToOriginalWindow(self):
        self.driver.switch_to.window(self.driver.window_handles[0])


