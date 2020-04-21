from random import seed
from random import randint
import os

# read log file
# logFile = open("agile-egloos.log", "r+")

# id를 인자로 받아 파일에 존재하면 true, id 없으면 false, id를 리턴하는 함수
# Parameter:
#   newid: String

def isNewpost(newid):
    
    lines = logFile.readlines()
    hasList = False 
    print(lines)
    for line in lines:
        splited = line.split(' ')
        id = splited[0]
        if newid == id:
            hasList = True
            break;

    return hasList

#def updatePost(newid):

def createLink(blogType, baseUrl):

    logFile = open("logs/shurain.log", "r+")
    lines = logFile.readlines()
    randNum = randint(0, len(lines))
    randEle = lines[randNum]
    splited = randEle.split(' ')
    postId = splited[0]
    title = randEle.replace(postId, '')
    cmd = 'printf \'\e]8;;'+ baseUrl + postId + '\e\\' + title + '\e]8;;\e\\\n\''
    os.system(cmd)
    #postUrl = baseUrl + 

def main():
    #isNewpost(12345)
    url1 = 'http://agile.egloos.com/'
    url2 = 'http://dotd.shurain.net/'

    createLink('agile', url1)
    createLink('shurain', url2)

    logFile.close()


if __name__ == "__main__":
    main()
