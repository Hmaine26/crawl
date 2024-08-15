from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome()
driver.get('https://lichngaytot.com/cung-hoang-dao.html')

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div/div/section[2]/div")))

elems = driver.find_elements(By.CSS_SELECTOR, ".title-heading [href]")
title = [elem.text for elem in elems]
print(title)

elems_content = driver.find_elements(By.CSS_SELECTOR, ".block-grid-3")
content = [elem.text for elem in elems_content]
content = [item.replace('\n', '. ') for item in content]
print(content)

df1 = pd.DataFrame(list(zip(title, content)), columns = ["Title", "Content"])
print(df1)

json_data = df1.to_json(orient='records',force_ascii=False, indent=4)
print(json_data)

with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json_data)




