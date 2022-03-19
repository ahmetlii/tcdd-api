'''

tcdd_api.conn - Provides the scrapper for fetching data.
'''

import mechanize
class connect:
"""
Connects the scrapper to the official website and fetches the data after sending the form.
:param link: Link for connection. The default is the official website.
:type link: str
"""

def __init__ (self, link="https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf"):
    self.link=link


def fill (self, station, date=datetime.today().strftime('%d.%m.%Y')):
"""
Fill the form with given parameters.
:param station: The station searched for the timetable.
:type station: str
    
:param date: Looks for a specific date for searching services. Default value for the parameter is today's date. Note that the input should be formatted as DD.MM.YY
:type date: str
"""
#TO-DO: Implement a mechanism to check if the station exists in form options, and probably create a way to print it.
br = mechanize.Browser()
br.open(self.link)
br.select_form(name="stationTrainInfoForm")
br.form['neredens'] = station
br.form.find_control("trCalGids_input").readonly = False
br.form['trCalGids_input'] = date
req = br.submit()
resp_url=req.geturl()
if (resp_url==self.link): #TO-DO: Directly check from form options before submitting it.
    raise Exception('The scrapper returned to same page after submitting the form. Did you provide an invalid parameter?')
else: resp_html = req.read()