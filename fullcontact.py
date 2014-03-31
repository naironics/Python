""" Python program that uses Full Contact API to 
	find out social profile usernames, twitter handles, gravatar photos and 
	all possible social details associated with an email.
	This could be from Facebook, Twitter, LinkedIn, Gravatar etc...
"""


import urllib2
import json

def fullContactCollect(email):
    api_key = 'YOUR API KEY FOR FULL CONTACT'
    email = email
    fullURL = 'https://api.fullcontact.com/v2/person.json?apiKey=' + api_key + '&email=' + email
    loadUrl = urllib2.urlopen(fullURL)
    jsonData = json.load(loadUrl)
	
    print jsonData
    
    # To get photos url :
    photos = jsonData['photos']
	 
    for item in photos:
	print item['url']	
	


fullContactCollect('YOUR EMAIL ADDRESS TO CHECK')
