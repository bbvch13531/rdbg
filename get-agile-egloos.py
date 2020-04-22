from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import os 
from random import seed
from random import randint

baseurl = "http://agile.egloos.com/"
requestUrl = baseurl + 'archives/'

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
#req = Request(url, data=None, headers)
req = urllib.request.Request(
    requestUrl,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
f = urlopen(req)
html = f.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
body= soup.body
table = body.table

tbody = table.contents[3]

divs = soup.find_all('div', {'class': 'ARCHIVE_BODY'})

postList = []

for links in divs:
    aline = links.find_all('a', href=True)
    #print(aline)
    for href in aline:
        #print(href)
        monthly = href['href']
        monthlyUrl = baseurl + str(monthly)
        
        req = urllib.request.Request(
                monthlyUrl,
                data=None,
                headers=headers
                )
        f = urlopen(req)
        monthlyHtml = f.read().decode('utf-8')
        soup = BeautifulSoup(monthlyHtml, 'html.parser')
        body = soup.find_all('div', {'class': 'POST_BODY'})
        posts = body[0].find_all('a', href=True)
        for post in posts:
    #        print(post['title'])
            if 'title' not in post.attrs.keys():
                postList.append(post)

linkList = []
titleList = []

for post in postList:
    linkId = post['href']
    link =  str(linkId).replace('/', '')
    linkList.append(link)
    titleList.append(post.string)
    #print(post['href'])


result = zip(linkList, titleList)
result = set(result)

# check this post is new or not
"""
for post in result:
    postId = post[0]
    if readlog.isNewpost(postId):
        readlog.updatePost(postId)
"""


cmdList = []
postUrlList = []

filep = open("archive-agile.log", "w+")

for ele in result:
    filep.write(baseurl + ele[0] + " " + ele[1] + "\n")
    postUrl = baseurl + ele[0]
    postUrlList.append(postUrl)

    cmdList.append('printf \'\e]8;;http://agile.egloos.com/' + ele[0] + '\e\\' + ele[1] + '\e]8;;\e\\' + ' ' + postUrl + '\n\'')

for ele in zip(linkList, titleList):
    link = str(ele[0])
# link = link.replace('/', '')
    #print(link, ele[1])

filep.close()

seed(1)
randNum = randint(0, len(cmdList))

os.system(cmdList[randNum])
"""
#for cmd in cmdList:
#    os.system(cmd)

# read log file

logFile = open('agile-egloos.log', 'w')

logFile.close()
"""
