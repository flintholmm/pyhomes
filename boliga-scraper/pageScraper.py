import urllib2
from bs4 import BeautifulSoup

def scrapePage(urlReq):
    #specify url
    website = urlReq

    #Query the url and return it to the variable 'page'
    page = urllib2.urlopen(website)

    #Parse the html in the page variable and store it in a BeautifulSoup format
    soup = BeautifulSoup(page, "lxml")

    #Identify the correct rows
    right_rows = soup.find_all("tr", class_="pRow")

    iterator = 1 #Iterator for creating unique IDs
    output = [] #Output list (will be the rows of csv file)


    for row in right_rows: #Iterator over the correct table rows
        cells = row.find_all("td") #Getting all values
        links = row.find_all("a") #Getting the address
        tmplist = [] #List containing all data points
        tmpAddress = [] #List containing <a> values ([0] will always be the address)
        outTemp = [] #Row temp of output

        for cell in cells: #Get all data points
            cellString = cell.get_text()
            tmplist.append(cellString)

        for link in links: #Get <a> tags (for isolating address)
            address = link.get_text()
            clean_add = address.replace(",", ";")
            tmpAddress.append(clean_add)

        outTemp = ["%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
        iterator,
        tmpAddress[0].strip(),
        tmplist[8],
        tmplist[1],
        tmplist[2],
        tmplist[7],
        tmplist[4],
        tmplist[5],
        tmplist[6],
        tmplist[9])]

        output.append(outTemp)
        iterator += 1

    print "Scraped page!"
    return output
