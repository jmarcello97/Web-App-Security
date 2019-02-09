
from user_agent import *
from bs4 import BeautifulSoup

def containsDigit(string):
	return any(char.isdigit() for char in string)

def main():
	request_type = "GET"
	file_path = "https://www.rit.edu/programs/computing-security-bs"
	host = "www.rit.edu"
	port = 443
	connection = "close"
	parameters = None

	response = request(request_type,file_path,host,port,connection,parameters)

	#print(response)
	soup = BeautifulSoup(response, 'html.parser')

	#print(soup)

	rows = soup.find_all('td')

	is_course_number = False

	course=""
	#print(rows)
	for r in rows:
		string=r.text.strip().encode('utf-8')
		
		if is_course_number:
			course+=string
			is_course_number=False
			print(course)
			course=""
		if containsDigit(string) and "-" in string:
			course+=string+","
			is_course_number=True

		#print(r.text)

main()
	
