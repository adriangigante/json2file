import re
import config

def run(url, fullReport):

    if url.find("swellnet") != -1:
        beginTag = '<!-- BEGIN-SWELLNET !-->'
        endTag = '<!-- END-SWELLNET !-->'
    else:
        beginTag = '<!-- BEGIN-COASTAL !-->'
        endTag = '<!-- END-COASTAL !-->'

    if url.find("eastern") != -1 or url.find("bondi") != -1:
        webpage = "eastern.html"
    else:
        webpage = "northern.html"

    # print(beginTag, endTag, webpage)      

    htmlFile = open(config.webroot + webpage)
    htmlText = htmlFile.read()
    htmlFile.close()

    htmlOut = re.split(beginTag, htmlText)[0] + beginTag + fullReport + endTag + re.split(endTag, htmlText)[1] 
    # print(htmlOut)

    htmlFile = open(config.webroot + webpage, "wt")
    htmlFile.write(htmlOut)
    htmlFile.close()
