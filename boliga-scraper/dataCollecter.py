from pageScraper import scrapePage
import csv

pageNumReq = int(raw_input("How many pages should be scraped? --> "))

output = []
header = "ID, ADRESSE, POSTNR, RUM, PRIS, KR/m2, BOLIG, GRUND, OPFORT, LIGGETID \n"
output.append(header)



loopNum = 1
while loopNum <= pageNumReq:
    baseURL = "http://www.boliga.dk/soeg/resultater/edf85890-eeb3-48c3-b550-608888d85ed3?page={0}".format(loopNum)
    tempList = scrapePage(baseURL)
    output.extend(tempList)
    loopNum += 1

with open('output.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    for row in output:
        if row == header: #Don't encode the header
            outfile.write(row)

        else:
            row = [s.encode('utf-8') for s in row] #Encode it in utf-8
            writer.writerows([row])
