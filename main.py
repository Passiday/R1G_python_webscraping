import requests
from bs4 import BeautifulSoup

# TODO: get the date from CLI param
url = 'https://ltv.lsm.lv/lv/programma?date=2023-11-08'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

def get_ltv1_contents():
  section_headers = soup.find_all("div", class_=["guide-table-header"])
  for div in section_headers:
    for txt in div.stripped_strings:
      if txt == "ltv1":
        items = []
        li_elements = div.parent.find_all("li")
        for li in li_elements:
          time = li.find("div", class_=["item-time"]).get_text()
          title = li.find("span", class_=["title"]).get_text()
          link = li.find("a", class_=["item-title"])
          if link:
            link = link["href"]
          #print(time, title, link)
          items.append([time, title, link])
        return items

ltv1 = get_ltv1_contents()
print(len(ltv1))
print(ltv1[1])
