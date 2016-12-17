from bs4 import BeautifulSoup


def crawling():
	file = open("grade.html", encoding="utf8")
	soup = BeautifulSoup(file.read(), "html.parser")
	grade = soup.find("td", text="資工一")
	print(grade)