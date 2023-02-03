from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


cities = ["Newyork, NY", "Boston, MA", "Arlington, TX", "Chicago, IL", "Miami, FL", "Dallas, TX", "Washington, DC"]

dict_columns = {"City": 1, "Population": 1, "Unemployement Rate": 4, "Median Income": 6, "Median Home Price": 8,
                "Median Age": 10,
                "Comfort Index(Climate)": 12}
rows = list()
for i in cities:

    data = dict()
    driver = webdriver.Chrome("/home/mohit/drivers/chromedriver_linux64/chromedriver")
    driver.get("https://www.bestplaces.net/")
    driver.maximize_window()
    driver.find_element_by_id("txtSearch").send_keys(i)
    driver.find_element_by_name("ctl00$btnSearch").click()
    htmlpage = driver.page_source
    soup = BeautifulSoup(htmlpage, "html.parser")
    mainRow = soup.find("div", class_="card-body container")
    mainRow2 = mainRow.find("div", class_="row")
    blocks = mainRow2.find_all("div", class_="col-md-4 px-1")
    row1 = blocks[0].find_all_next("p")

    for key, value in dict_columns.items():
        if key == "City":
            data.update({key: i})
        else:
            data.update({key: row1[value].text})
    rows.append(data)
    driver.quit()
df = pd.DataFrame(rows)
df.to_csv("City_profile.csv", index=False)
