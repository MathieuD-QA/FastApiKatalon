from selenium import webdriver
from selenium.webdriver.common.by import By



class KatalonDoc:
    def __init__(self):
        # Partie new Version de Katalon Studio

        self.version_filter = None
        self.new_Features_filter = None
        self.enhancements_filter = None
        self.fixes_filter = None

        # Partie Doc Katalon Web UI
        self.title = None
        self.description = None
        self.descriptionText = None
        self.parameters = None
        self.parametersText = None
        self.exemple = None
        self.exempleText = None

        #Optionnel suivant le système d'exploitation
        self.note = None







#DONE

    def WebUIAcceptAlert(self):

        driver = webdriver.Chrome()
        driver.get("https://docs.katalon.com/katalon-studio/docs/webui-accept-alert.html#example")
        self.title = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/section/h1").text
        self.description = driver.find_element(By.XPATH,"//h2[@id='description']").text
        self.descriptionText = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/section/p[1]").text
        self.parameters = driver.find_element(By.XPATH, "//h2[@id='parameters']").text
        self.parametersText = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/section/table").text
        self.exemple = driver.find_element(By.XPATH,"//h2[@id='example']").text
        #self.exempleText = driver.find_element(By.XPATH,"//pre[@scrapping='highlight']").text
        driver.close()




#DONE
    def WebUIBack(self):
        driver = webdriver.Chrome()
        driver.get("https://docs.katalon.com/katalon-studio/docs/webui-back.html")
        self.title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/h1").text
        self.description = driver.find_element(By.XPATH, "//h2[@id='description']").text
        self.descriptionText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/p[1]").text
        self.parameters = driver.find_element(By.XPATH, "//h2[@id='parameters']").text
        self.parametersText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/table").text
        self.exemple = driver.find_element(By.XPATH, "//h2[@id='example']").text
        #self.exempleText = driver.find_element(By.XPATH, "//pre[@scrapping='highlight']").text
        driver.close()

#DONE

    def WebUICheck(self):
        driver = webdriver.Chrome()
        driver.get("https://docs.katalon.com/katalon-studio/docs/webui-check.html")
        self.title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/h1").text
        self.description = driver.find_element(By.XPATH, "//h2[@id='description']").text
        self.descriptionText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/p[1]").text
        self.parameters = driver.find_element(By.XPATH, "//h2[@id='parameters']").text
        self.parametersText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/table").text
        self.exemple = driver.find_element(By.XPATH, "//h2[@id='example']").text
        #self.exempleText = driver.find_element(By.XPATH, "//pre[@scrapping='highlight']").text
        driver.close()


#DONE


    def WebUICheck(self):
        driver = webdriver.Chrome()
        driver.get("https://docs.katalon.com/katalon-studio/docs/webui-click.html")
        self.title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/h1").text
        self.description = driver.find_element(By.XPATH, "//h2[@id='description']").text
        self.descriptionText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/p[1]").text
        self.parameters = driver.find_element(By.XPATH, "//h2[@id='parameters']").text
        self.parametersText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/table").text
        self.exemple = driver.find_element(By.XPATH, "//h2[@id='example']").text
        #self.exempleText = driver.find_element(By.XPATH, "//pre[@scrapping='highlight']").text
        driver.close()


#DONE


    def WebUIClickImage(self):
        driver = webdriver.Chrome()
        driver.get("https://docs.katalon.com/katalon-studio/docs/webui-click-image.html")
        self.title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/h1").text
        self.description = driver.find_element(By.XPATH, "//h2[@id='description']").text
        self.descriptionText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/p[1]").text
        self.parameters = driver.find_element(By.XPATH, "//h2[@id='parameters']").text
        self.parametersText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/table").text
        self.exemple = driver.find_element(By.XPATH, "//h2[@id='example']").text
        #self.exempleText = driver.find_element(By.XPATH, "//pre[@scrapping='highlight']").text
        driver.close()
#DONE


    def WebUIClickOffset(self):
        driver = webdriver.Chrome()
        driver.get("https://docs.katalon.com/katalon-studio/docs/webui-click-offset.html")
        self.title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/h1").text
        self.description = driver.find_element(By.XPATH, "//h2[@id='description']").text
        self.descriptionText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/p[1]").text
        self.parameters = driver.find_element(By.XPATH, "//h2[@id='parameters']").text
        self.parametersText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/table").text
        self.exemple = driver.find_element(By.XPATH, "//h2[@id='example']").text
        #self.exempleText = driver.find_element(By.XPATH, "//pre[@scrapping='highlight']").text
        driver.close()
#DONE
    def WebUICloseBrowser(self):
        driver = webdriver.Chrome()
        driver.get("https://docs.katalon.com/katalon-studio/docs/webui-close-browser.html")
        self.title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/h1").text
        self.description = driver.find_element(By.XPATH, "//h2[@id='description']").text
        self.descriptionText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/p[1]").text
        self.parameters = driver.find_element(By.XPATH, "//h2[@id='parameters']").text
        self.parametersText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/table").text
        self.exemple = driver.find_element(By.XPATH, "//h2[@id='example']").text
        #self.exempleText = driver.find_element(By.XPATH, "//pre[@scrapping='highlight']").text
        driver.close()
#DONE




    def WebUICloseWindowTitle(self):
        driver = webdriver.Chrome()
        driver.get("https://docs.katalon.com/katalon-studio/docs/webui-close-window-title.html")
        self.title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/h1").text
        self.description = driver.find_element(By.XPATH, "//h2[@id='description']").text
        self.descriptionText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/p[1]").text
        self.parameters = driver.find_element(By.XPATH, "//h2[@id='parameters']").text
        self.parametersText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/table").text
        self.exemple = driver.find_element(By.XPATH, "//h2[@id='example']").text
        #self.exempleText = driver.find_element(By.XPATH, "//pre[@scrapping='highlight']").text


    def WebUICloseWindowUrl(self):
        driver = webdriver.Chrome()
        driver.get("https://docs.katalon.com/katalon-studio/docs/webui-close-window-url.html")
        self.title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/h1").text
        self.description = driver.find_element(By.XPATH, "//h2[@id='description']").text
        self.descriptionText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/p[1]").text
        self.parameters = driver.find_element(By.XPATH, "//h2[@id='parameters']").text
        self.parametersText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/table").text
        self.exemple = driver.find_element(By.XPATH, "//h2[@id='example']").text
        #self.exempleText = driver.find_element(By.XPATH, "//pre[@scrapping='highlight']").text

    def WebUIDeleteAllCookies(self):
        driver = webdriver.Chrome()
        driver.get("https://docs.katalon.com/katalon-studio/docs/webui-delete-all-cookies.html")
        self.title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/h1").text
        self.description = driver.find_element(By.XPATH, "//h2[@id='description']").text
        self.descriptionText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/p[1]").text
        self.parameters = driver.find_element(By.XPATH, "//h2[@id='parameters']").text
        self.parametersText = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/section/table").text
        self.exemple = driver.find_element(By.XPATH, "//h2[@id='example']").text
        #self.exempleText = driver.find_element(By.XPATH, "//pre[@scrapping='highlight']").text










