import config
import schedule
import time
import json2file

def job():
    print("Creating reports...")
    json2file.run(config.proxyUrl + "/https://swellnet.com/reports/australia/new-south-wales/eastern-beaches")
    json2file.run(config.proxyUrl + "/https://coastalwatch.com/surf-cams-surf-reports/nsw/bondi-beach")
    print("Reports created")

schedule.every(1).seconds.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)