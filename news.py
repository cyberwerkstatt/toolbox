import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time

news = []

url = "https://www.salzburg24.at"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

headlines = soup.find_all("h2", class_="teaser__headline")
for headline in headlines:
    line = headline.get_text()
    news.append(line)
    
for i in tqdm(range(len(news))):
    time.sleep(0.1)
print("\n")
print("#################### SALZBURG24 NEWS ####################")
for lines in news:
    print(lines.strip())
    time.sleep(1)
    







