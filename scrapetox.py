#
# coding latin-1

import requests
from bs4 import BeautifulSoup


#myurl = "http://risctox.istas.net/en/dn_risctox_ficha_sustancia.asp?id_sustancia=1024801"
#myurl = "http://risctox.istas.net/en/dn_risctox_ficha_sustancia.asp?id_sustancia=955332"
myurl = "http://risctox.istas.net/en/dn_risctox_ficha_sustancia.asp?id_sustancia=959022"

response = requests.get(myurl)
print (response.text)

soup = BeautifulSoup(response.text, "html.parser")
mytags = soup.findAll('span')

print (myurl)

for mytag in mytags:
    print (mytag) # .replace('<span','\n<span'))

# mytags = soup.findAll('b')
# for mytag in mytags:
#     print (mytag) # .replace('<span','\n<span'))


# <span id="name.label">Chemical name:</span>
# <span id="name.value">[ (phthaloylbis (oxy) ]bis (tributylstannane) </span>
# <span id="identification_numbers.label">Identification numbers:</span>
# <span id="cas_num.label">CAS</span>
# <span id="cas_num.value">4782-29-0</span>
# <span id="ec_einecs_num.label">EC EINECS</span>
# <span id="ec_einecs_num.value">225-327-8</span>
# <span id="groups.label">Groups</span>
# <span id="groups.value">Tributyltin compounds, Organic compounds of Sn, organic esters and their halogenated derivatives, phthalates</span>
# <span id="uses.label">Uses</span>
# <span id="uses.value">additive, antifouling, cleaner, cosmetic additive, denaturing agent, deodorant, dye, fungicide, lacquer, paint, pigment, plasticizer, preservative, scent, solvent, stabilizer, thickener</span>
# <span id="additional_information.label">Additional information</span>
# <span id="rd_num.label">Index No</span>
# <span id="rd_num.value">050-008-00-3</span>
# <span id="molecular_formula.label">Molecular formula</span>
# <span id="molecular_formula.value">C32H58O4Sn2<br/>
# </span>
# <span id="concern_trade_union_reasons.label">This substance is included in the List of Substances of concern for Trade Unions for the following reasons:</span>
# <span id="concern_trade_union_reasons.value">Endocrine disrupter, toxic, persistent and bioaccumulative, may cause long term adverse effects in the aquatic environment
