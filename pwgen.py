import random
from selenium import webdriver
import time
import string
# Create List to hold random words
wordlist = []
obwords = []
# CaMeL CaSe FuNcTiOn
def ccase(s):
	ret = ""
	i = True
	for char in word:
		if i:
			ret += char.upper()
		else:
			ret += char.lower()
		if char != ' ':
			i = not i
	return ret

# URL For pulling words
rwurl = "http://watchout4snakes.com/wo4snakes/Random/RandomWord/"
# Set selenium to run Chrome headless
options = webdriver.ChromeOptions()
options.add_argument('headless')
# Start Chrome and open page
driver = webdriver.Chrome(options=options)
driver.get(rwurl)

#Add result word to list and refresh browser 4x
for x in range(4):
	word = driver.find_element_by_id('result')
	wordlist.append(word.text)
	driver.refresh()
	time.sleep(1)

#close browser
driver.quit()

for word in wordlist:
	word = word.replace('a', '@', 1)
	word = word.replace("l", "1", 1)
	word = word.replace("i", "!", 1)
	word = word.replace("e","3", 1)
	word = word.replace("o","0", 1)
	word = word.replace("s","$", 1)
	word = ccase(word)
	obwords.append(word)
	
print(obwords[0] + obwords[1] + obwords[2] + obwords[3])
