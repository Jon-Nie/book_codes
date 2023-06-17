import requests
from bs4 import BeautifulSoup
from html import unescape
import os
import urllib.request

def download_datasets() -> None:
	base_url = "https://faculty.chicagobooth.edu/"
	url = r"https://faculty.chicagobooth.edu/ruey-s-tsay/research/analysis-of-financial-time-series-3rd-edition"
	html = requests.get(url).text
	chapters = ["<h2>" + chapter for chapter in html.split("<h2>")][1:]

	for chapter in chapters:
		chapter = unescape(chapter)
		soup = BeautifulSoup(chapter, "lxml")
		title = soup.find("h2").text.replace(":", "").replace("Chapter", "").lstrip().strip("\n")
		print(title)

		if not os.path.exists(title):
			os.makedirs(f"{title}/datasets")

		for row in soup.find_all("a"):
			name = row.text
			href = row.get("href")
			url = f"{base_url}{href}"
			if "C:/Users" in url:
				continue
			if href == "https://www.chicagobooth.edu/":
				break
			try:
				urllib.request.urlretrieve(url, f"{title}/datasets/{name}")
				print(f"   {url}")
			except urllib.error.HTTPError:
				print(f"   failed: {url}")

if __name__ == "__main__":
	download_datasets()