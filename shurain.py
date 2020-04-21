from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import os
from random import seed, randint

baseurl = 'http://dotd.shurain.net/'
req = urllib.request.Request(
        baseurl,
        data=None
        )

f = urlopen(req)
html = f.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

pageNum = 1
postList = []

while(True):
    entries = soup.find_all('a', {'class': 'next'})
    # Last page
    if len(entries) == 0:
        break;

    posts = soup.find_all('div', {'class': 'item'})

    for post in posts:
        postTag = post.find_all('a')
        postList.append(postTag[0])

    pageNum = pageNum + 1
    nextPageurl = baseurl + 'page/' + str(pageNum)
    req = urllib.request.Request(nextPageurl, data=None)
    f = urlopen(req)
    html = f.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

urlList = []
dateList = []
titleList = []
cmdList = []


for post in postList:
    postId = str(post['href'])
    title = post.string
   
    splited = postId.split('/')
    if len(splited) == 3:
        date = splited[1]
    else:
        date = splited[2]
    #print(date, title)
    dateList.append(date)
    titleList.append(title)
    
    postUrl = baseurl + date
    urlList.append(postUrl)
#    print(baseurl+date + ' ' + title)
    cmdList.append('printf \'\e]8;;' + baseurl + date + '\e\\' + title + '\e]8;;\e\\ ' + postUrl + '\n\'')

f = open("blogPost.log", "w+")
for ele in zip(urlList, titleList):
    f.write(ele[0]+" "+ ele[1] + "\n")

f.close()

randNum = randint(0, len(cmdList))


os.system(cmdList[randNum])


