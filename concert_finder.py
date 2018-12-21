from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime
import calendar
import time

# Get current date
now = datetime.datetime.now()
day = str(now.day)
month = time.strftime("%B")
weekday = time.strftime("%A")
year = str(now.year)
currentDate =  str(weekday + " " + day + " " + month + " " + year)

my_url = "https://www.songkick.com/metro_areas/9179-us-austin"

# Opening connection, grabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# Grabs each concert/location today
event_listings = page_soup.findAll("li", {"title":currentDate})

#creates csv file
filename = "Concerts.csv"
f = open(filename, "w")

headers = "Artist, Location\n"
f.write(headers)

for event in event_listings:

	artist = event.p.strong.text
	try:
		location_container = event.findAll("p", {"class": "location"})
		location = location_container[0].span.a.text.strip()
	except:
		location = "Location not available"

	print("Artist: " + artist)
	print("Location: " + location)

	f.write(artist.replace(",", " ") + "," + location.replace(",", " ") + "\n")
	

f.close()
