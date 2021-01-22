from selenium import webdriver
import pandas as pd

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path= "/Users/Jordan's Desktop/Desktop/Powerball/chromedriver.exe")
numbers = []

for z in range(1,117):
    print(f"Scanning pages{z}")
    url = f'https://www.usamega.com/powerball/results/{z}'
    browser.get(url)

    num_results = browser.find_elements_by_class_name('results')
    
    for y in range(1,len(num_results)):
        items = []
        for x in range(1,6):
            # Puts item into list
            item = browser.find_elements_by_xpath(f'//*[@id="content"]/main/div[4]/table/tbody/tr[{y}]/td[1]/section/ul/li[{x}]')
            # Puts that item into another list
            items.append(int(item[0].text))

        numbers.append(items)


print(numbers)    

pd.DataFrame(numbers).to_excel('output.xlsx', header=False, index=False)

browser.close()