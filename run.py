import config
import time
# import json2file
# import parse_report
import parse_report_inplace
import datetime
import urllib2
import json
import replace_html

# def job():

# 	print("cron-log: Running job at ")
# 	print (datetime.datetime.now().time())
# 	report = {"https://www.swellnet.com/reports/australia/new-south-wales/eastern-beaches", "http://www.swellnet.com/reports/australia/new-south-wales/northern-beaches", "https://www.coastalwatch.com/surf-cams-surf-reports/nsw/bondi-beach", "https://www.coastalwatch.com/surf-cams-surf-reports/nsw/manly---nth-steyne"}
    
# 	for url in report:
# 	    print("cron-log: Creating report " + url)
# 	    filename = json2file.run(config.proxyUrl + "/" + url)
# 	    #print(filename)
# 	    report = parse_report.run(filename)
# 	    print("cron-log: Report created at " + report)    

def job():

	print("cron-log: Running job at ")
	print (datetime.datetime.now().time())
	report = {"https://www.swellnet.com/reports/australia/new-south-wales/eastern-beaches", "http://www.swellnet.com/reports/australia/new-south-wales/northern-beaches", "https://www.coastalwatch.com/surf-cams-surf-reports/nsw/bondi-beach", "https://www.coastalwatch.com/surf-cams-surf-reports/nsw/manly---nth-steyne"}
    
	for url in report:
		print("cron-log: Creating report " + url)
		contents = urllib2.urlopen(config.proxyUrl + "/" + url).read()
		# print(contents)
		data = json.loads(contents)
		html = data["contents"].encode("utf-8")
		fullReport = parse_report_inplace.run(url, html)
		# print(fullReport)
		replace_html.run(url,fullReport)

#Run on start
job()
