import config
import schedule
import time
#import json2file
#import parse_report
import json
import datetime
import urllib2
import replace_html
import parse_report_inplace

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

#Schedule
schedule.every().day.at("05:00").do(job)
schedule.every().day.at("05:15").do(job)
schedule.every().day.at("05:30").do(job)
schedule.every().day.at("05:45").do(job)
schedule.every().day.at("06:00").do(job)
schedule.every().day.at("08:00").do(job)
schedule.every().day.at("08:30").do(job)
schedule.every().day.at("09:10").do(job)
schedule.every().day.at("09:30").do(job)
schedule.every().day.at("12:00").do(job)
schedule.every().day.at("12:15").do(job)
schedule.every().day.at("12:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


#i.e
#schedule.every(1).seconds.do(job)
#schedule.every().hour.do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)