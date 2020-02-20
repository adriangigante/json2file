import sys
import urllib2
import json

def run(url):

  contents = urllib2.urlopen(url).read()
  #print(contents)
  data = json.loads(contents)
  #print(data["contents"])
  
  filename = "tmp/" + url.split("//")[2].replace('/','-')
  #print(filename)
  f = open(filename, "w")
  f.write(data["contents"].encode("utf-8"))
  return filename
