import csv
# This file gives csv commands for downloading data from a webscrape.
import requests
from BeautifulSoup import BeautifulSoup
# requests.get("https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s").content --this line pulls back a site's html
url = "https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
header = soup.find('tr', attrs={'class':'table-header'})
table = soup.find('tbody', attrs={'class': 'stripe'})

all_data = []


# Getting the header row
header_row = []
for cell in header.findAll('th'):
	header_row.append(cell.text.replace("&nbsp;",""))

all_data.append(header_row)

# Getting all the data from the rows
for row in table.findAll('tr'):
	# Expected: row = all the html for one row at a time
	list_of_cells = []
	for cell in row.findAll('td'):
		# print cell.text
	# Expected: cell = all the html for each td in this particular row
		if cell.text == "&nbsp;Details": 
			link = cell.find('a').get('href')
			list_of_cells.append(link)
		else: 
			list_of_cells.append(cell.text)

	all_data.append(list_of_cells)
file = open("./inmates.csv", "wb")
writer = csv.writer(file)
writer.writerows(all_data)
# print all_data
