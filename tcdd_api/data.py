'''
tcdd_api.data - Prettifies the data fetched from connection and classifies them.
'''
from bs4 import BeautifulSoup as bs
from conn import resp_html

class Parser:
"""
Parses the retrieved data. Shouldn't be used without connection initialization.

:param search: Searches for the specified text in the data.
:type search: str
"""
def __init__ (self, search):
self.search=search

def prettify (self):
"""
Prettifies the data.
"""
soup = BeautifulSoup(resp_html, 'html.parser')
body = soup.find_all('div', attrs={'id': 'travelTable'})
for row in body:
    row_text = [x.text for x in row.find_all('td')]
    print(','.join(row_text))
if search is not None: #incomplete part

#WORK IN PROGRESS 14.01.2022
class Sort:
    def incoming(self):
    """
    Lists and implements defined parameters in incoming trains.
    """
    incomingdata = soup.find_all('tbody', attrs={'id': 'TravelTable_data'})
    for row in incomingdata:
        row_text = [x.text for x in row.find_all('tr')]
        print(','.join(row_text))
    def outgoing(self):
    """
    Lists and implements defined parameters in outgoing trains.
    """
    outgoingdata = soup.find_all('tbody', attrs={'id': 'TravelTable_data'})
    for row in outgoingdata:
        row_text = [x.text for x in row.find_all('tr')]
        print(','.join(row_text))
    def transit(self):
    """
    Lists and implements defined parameters in transit trains.
    """
    transitdata = soup.find_all('tbody', attrs={'id': 'TravelTable_data'})
    if (transitdata==)
    else: 
        for row in transitdata:
            row_text = [x.text for x in row.find_all('tr')]
            print(','.join(row_text))