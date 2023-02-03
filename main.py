
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("/home/mohit/drivers/chromedriver_linux64/chromedriver")
url = "https://www.redfin.com/city/1826/MA/Boston/filter/sort=lo-price"
cities = ["Boston, MA", "New York, NY", "Dallas, TX", "Los Angeles, Southern California", "Chicago, Illinois",
          "Washington, DC", "San Fransisco, Northern California", "San Diego, California", "Phoenix, Arizona", "Houston, TX",
          "Austin, TX", "Columbus, Ohio"]
column = ["Home Address", "Details", "Price"]
rows = list()
urlTemp = url
for k in range(8):
    driver.maximize_window()
    driver.get(urlTemp)
    htmlContent = driver.page_source
    soup = BeautifulSoup(htmlContent, "html.parser")
    div = soup.find("div", class_="HomeCardsContainer flex flex-wrap")
    cards = div.find_all_next("div",class_="HomeCardContainer defaultSplitMapListView")
    for i in cards:
        row = list()
        div2 = i.find_next("div",class_="bottomV2")
        div3 = div2.find_all("div")
        row.append(div3[len(div3)-1].text)
        row.append(div3[3].text)
        row.append(div2.find("span").text)
        rows.append(row)
    urlTemp = url + "/page-"+str(k+2)
df = pd.DataFrame(rows,columns=column)
driver.quit()
df.to_csv("Boston_homes2.csv", index=False)
print(df)

