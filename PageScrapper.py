from urllib.request import urlopen
import re
from playsound import playsound


def ScrapeWorkaway(num):

    with open("usa.txt", "a") as textFile:
        textFile.write("Page: " + str(i) + "\n")
        textFile.close()
    
    mainUrl = 'https://www.workaway.info/en/hostlist/northamerica/us?Page=' + str(num)

    with urlopen(mainUrl) as mainpage:
        main = mainpage.read().decode().lower()
        mainpage.close()

    result = re.findall('host/\d+', main)

    pageNumbers = []

    for item in set(result):
        try:
            url = 'https://www.workaway.info/en/host/' + str(item[5:])

            with urlopen(url) as webpage:
                content = webpage.read().decode().lower()

            cleaner = re.compile("<.*?>")

            content = re.sub(cleaner, "", content)

            result = re.search("hours expected.*<a", content)

            result = result.group(0)[14:-2]

            with open("usa.txt", "a") as textFile:
                textFile.write(result + " : " + url + "\n")
                textFile.close()
        except:
            continue



for i in range(2, 55):
    ScrapeWorkaway(i)

playsound("codeFinished.mp3")
