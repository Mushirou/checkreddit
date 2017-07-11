# Project to start to check new posts on some of my favorites reddits
import urllib.request
import json
import time

url = 'https://www.reddit.com/r/Brasil/new/.json'
isFirst = True
while isFirst:
  try:
    resp = urllib.request.urlopen(url).read()
    parsed = json.loads(resp.decode('utf-8'))
    antItem = parsed['data']['children'][0]
    prevDoc = antItem['data']
    print(prevDoc['title'])
    print(prevDoc['url'])
    print()
    isFirst = False
  except:
    time.sleep(5)

startTimer = True
isFirst = True
i = 0
time.sleep(5)

while True:
  try:
    resp = urllib.request.urlopen(url).read()
    parsed = json.loads(resp.decode('utf-8'))
    atuItem = parsed['data']['children'][0]
    currDoc = atuItem['data']
    titAtu = currDoc['title']
    titAnt = prevDoc['title']
    if not (titAnt == titAtu) :
      prevDoc = currDoc
      print(currDoc['title'])
      print(currDoc['url'])
      print()
      startTimer = False
    else:
      startTimer = True
    if startTimer:
      time.sleep(60)
  except:
    time.sleep(5)