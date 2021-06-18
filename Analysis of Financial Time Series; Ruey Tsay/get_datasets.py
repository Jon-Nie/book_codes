import requests
from bs4 import BeautifulSoup
import html
import os
import urllib.request

base_url = 'https://faculty.chicagobooth.edu/'
url = r'https://faculty.chicagobooth.edu/ruey-s-tsay/research/analysis-of-financial-time-series-3rd-edition'
string = requests.get(url).text

delimiter_h2 = '<h2>'
string = [delimiter_h2 + sub_string for sub_string in string.split(delimiter_h2)][1:]

delimiter_p = '</a>'
for chapter in string:
	chapter = html.unescape(chapter)
	soup = BeautifulSoup(chapter, "lxml")
	chapter_title = soup.find('h2').text.replace(':', '').replace('Chapter', '').lstrip().strip('\n')
	print("\n", chapter_title,"\n")
	if not os.path.exists(chapter_title):
		os.makedirs(f"{chapter_title}/datasets")
	rows = soup.find_all('a')
	for row in rows:
		name = row.text
		href = row.get('href')
		file_link = base_url + href
		if 'C:/Users' in file_link:
			continue
		if href == "https://www.chicagobooth.edu/":
			break
		print("\t", file_link)
		urllib.request.urlretrieve(file_link, f"{chapter_title}/datasets/{name}")
