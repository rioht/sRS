def cats():
	return "hoolaboola"
def print_this():
	#import csv
	import requests
	r = requests.get("http://www.google.com")
	#with open('SRSresults.csv', 'rb') as csvfile:
		#spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		#for row in spamreader:
			#test_array.append(', '.join(row))
	return r.status_code

def srs_scraper(srs_var):

	def timeconverter(x):
		tc = time.strftime("%Y.%b.%d.%H:%M:%S", time.localtime(x))
		results.append(tc)

	import time, praw, csv
	reddit_ua = "Subreddit Scraper: v0.1 /u/rioht"
	r = praw.Reddit(user_agent = reddit_ua)
	sub = r.get_subreddit(srs_var)
	results = []
	try:

		for loopy in sub.get_new(limit = 25):
			results.append(loopy.id)
			results.append(loopy.author)
			timeconverter(loopy.created_utc)
	
		return results

	except:

		return "The subreddit you queried either doesn't exist or is private.  Try again?"
