import os
from random import seed, randint

f = open("archive_shurain.log", "r")

lines = f.readlines()
cmdList = []

for line in lines:
    split_array = line.split(' ')
    url = split_array[0]
    title = split_array[1]
    title=line.replace(url,"")
    title = title[1:]
    cmdList.append('printf \'\e]8;;' + url + '\e\\' + title + '\e]8;;\e\\\'')

randNum = randint(0, len(cmdList))
os.system(cmdList[randNum])
