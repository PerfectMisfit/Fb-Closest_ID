# -*- coding: utf-8 -*-
import sys
import requests
import json
from bs4 import BeautifulSoup

profile_id = raw_input("Enter your Facebook Profile ID: ")

# Ask for number of neighbours user will like to see
num = int(raw_input("How many neighbours would you like to find out? (Max 20) "))
if num > 20:
    print "Your desires are too high! Sorry!"
else:
    # Initialization of counter variable(count)
    count = 0
    # Store the profile ID in a temp variable which will be set(incremented) again and again
    temp = int(profile_id)
    while count < num:
        temp += 1
        fb_url = "https://www.facebook.com/profile.php?id=" + str(temp)
        # Make HTTP call with every value of profile ID(temp)
        r = requests.get(fb_url)
        html = r.content
        soup = BeautifulSoup(html,"lxml")
        # Get name from title of the page(the easiest method to get name from the page)
        name = soup.title.string.split(" | ")
        name = name[0]
        # Error handling
        if name != "Profile Unavailable" and name != "Content Not Found" and name.encode('utf-8') != "सामग्री नहीं मिली":
            print name.encode('utf-8'), "https://www.facebook.com/profile.php?id="+str(temp)
            count += 1 # Increment counter variable(count)
