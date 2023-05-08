from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
def chrome_setup():
    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-gpu') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    chrome_options.add_argument('--proxy-server=http://192.168.181.1:7890') 
    chrome_options.add_argument('--disable-infobars')

    # disable download popup window
    chrome_options.add_experimental_option('prefs', {
    "download.default_directory": "/home/cc/chrome/paper/usenix", #Change default directory for downloads
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True, #It will not show PDF directly in chrome
    })
    
    driver = webdriver.Chrome(options=chrome_options)
    
    return driver


websites = [
    #"https://www.ndss-symposium.org/ndss2021/accepted-papers/",
    "https://dblp1.uni-trier.de/db/conf/uss/uss2018.html",
]
for website in websites:
    driver = chrome_setup()
    driver.get(website)
    all_paper_link = list()
    second_level = 2
    first_level = 1
    blank_elem = driver.find_element(By.XPATH, "/html/body/div[2]/ul[1]/li[1]/nav/ul/li[1]/div[1]/a/img")
    flag_pass_tacle = False
    for i in range(1,200):
        try:
            tmp = driver.find_element(By.XPATH, f"/html/body/div[2]/ul[{second_level}]/li[{first_level}]/nav/ul/li[1]/div[1]/a/img")
            first_level += 1
        except:
            second_level += 1
            first_level = 1
            continue
        all_paper_link.append(tmp)
    print(len(all_paper_link))
    all_paper_link = all_paper_link[75:]
    for paper_link in all_paper_link:
        # popup a new tab
        ActionChains(driver).key_down(Keys.CONTROL).click(paper_link).key_up(Keys.CONTROL).perform()
        
        # change the window
        handles = driver.window_handles
        driver.switch_to.window(handles[1])

        driver.find_element(By.CLASS_NAME, "file").click()
        time.sleep(4)
        driver.close()
        time.sleep(5)
        driver.switch_to.window(handles[0])
        try:
            driver.find_element("class name", "cky-btn-accept").click()
        except:
            pass
        if flag_pass_tacle == False:
            ActionChains(driver).move_to_element(blank_elem).key_down(Keys.CONTROL).click(blank_elem).key_up(Keys.CONTROL).perform()
            handles = driver.window_handles
            driver.switch_to.window(handles[1])
    
            driver.close()

            driver.switch_to.window(handles[0])

    driver.close()
    
        
