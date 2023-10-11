import datetime
import os.path


def log(fp, s: str):
    curTime = datetime.datetime.now()
    fp.write(f"[{curTime}]: {s}\n")


def openLog(fileName: str):
    if not os.path.exists("./logs"):
        os.makedirs("./logs")
    finalPath = f"./logs/{name}.txt"

    ind = 1
    while os.path.isfile(finalPath):
        finalPath = f"./logs/{name}-{ind}.txt"
        ind += 1
    return open(finalPath, "w")


name = input("Input your name: ")
fp = openLog(name)

log(fp, "bruh")
fp.close()
