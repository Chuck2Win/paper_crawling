from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', DesiredCapabilities.CHROME)
url = 'https://scholar.google.com/scholar?cites=10143779580305681961&as_sdt=2005&sciodt=0,5&hl=ko'
driver.get(url)

data = []
no = 1
while True:
    c = 1
    while True:
        try:
            if no%50 == 0:
                print(no)
            title = driver.find_element(By.CSS_SELECTOR, value = f'#gs_res_ccl_mid > div:nth-child({c}) > div.gs_ri > h3').text
            abstract = driver.find_element(By.CSS_SELECTOR, value = f'#gs_res_ccl_mid > div:nth-child({c}) > div.gs_ri > div.gs_rs').text
            refers = driver.find_element(By.CSS_SELECTOR, value = f'#gs_res_ccl_mid > div:nth-child({c}) > div.gs_ri > div.gs_fl > a:nth-child(3)').text
            c+=1
            no+=1
            data.append(dict(title=title, abstract = abstract, refers = refers))
        except:
            break
    next_link = driver.find_element(By.CSS_SELECTOR, value = '#gs_n > center > table > tbody > tr > td:nth-child(12) > a > b')
    if next_link:
        next_link.click()
        driver.implicitly_wait(5)
    else:
        break    
import pandas as pd 
data = pd.DataFrame(data).to_csv('new_data.csv')
print('done')