import readlog

f = open("agile-egloos.log", "r")
asd = f.readline()
print(asd.strip())

readlog.isNewpost(asd)
