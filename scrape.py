import requests
from BeautifulSoup import BeautifulSoup
# requests.get("https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s").content --this line pulls back a site's html
url = "https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs= {'class': 'stripe'})


# for row in table.findAll('tr'):
# 	# Expected: row = all the html for one row at a time
# 	# for cell in row.findAll('td'):
# 	# 	print cell.text
# 	# # Expected: cell = all the html for each td in this particular row
# 	# if cell.text == "&nbsp;Details": 
# 	# 	print cell.find('a').get('href')
# 	# else: 
# 	# 	print cell.text
# 	# Expected: cell.find('a').get('href') = return links on this page. else: print cell.text = return everything but the links. Remember that the indentation matters. "if" and "else" commands are on same line, as are "print" commands.

# # for row in table.findAll('tr'):
# 	# Expected: row = all the html for one row at a time
# 	list_of_cells = []
# 	for cell in row.findAll('td'):
# 		print cell.text
# 	# Expected: cell = all the html for each td in this particular row
# 	if cell.text == "&nbsp;Details": 
# 		link = cell.find('a').get('href')
# 		list_of_cells.append(link)
# 	else: 
# 		list_of_cells.append(cell.text)
# print list_of_cells


# for row in table.findAll('tr'):
	# Expected: row = all the html for one row at a time
	# for cell in row.findAll('td'):
	# 	print cell.text
	# # Expected: cell = all the html for each td in this particular row
	# if cell.text == "&nbsp;Details": 
	# 	print cell.find('a').get('href')
	# else: 
	# 	print cell.text
	# Expected: cell.find('a').get('href') = return links on this page. else: print cell.text = return everything but the links. Remember that the indentation matters. "if" and "else" commands are on same line, as are "print" commands.

all_data = []
for row in table.findAll('tr'):
	# Expected: row = all the html for one row at a time
	list_of_cells = []
	for cell in row.findAll('td'):
		print cell.text
	# Expected: cell = all the html for each td in this particular row
		if cell.text == "&nbsp;Details": 
			link = cell.find('a').get('href')
			list_of_cells.append(link)
		else: 
			list_of_cells.append(cell.text)

	all_data.append(list_of_cells)
print all_data