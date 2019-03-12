from bs4 import BeautifulSoup
# Python 3.x
from urllib.request import urlopen, urlretrieve, quote
from urllib.parse import urljoin
import os




######## Prepare --------------------------------------------------------

year = "平成28年度DPC導入の影響評価に係る調査「退院患者調査」の結果報告について"
url = 'https://www.mhlw.go.jp/stf/shingi2/0000196043.html'



######## Make soup ------------------------------------------------------

u = urlopen(url)
try:
    html = u.read().decode('utf-8')
finally:
    u.close()

soup = BeautifulSoup(html, "html.parser")


# check
"""
soup.select('a[href^="/file"]')[30]
soup.select('a[href^="/file"]')[30].get('href')
soup.select('a[href^="/file"]')[30].get_text().split("（E")[0]
soup.select('a[href^="/file"]')[0].get('href').rsplit('/', 1)[-1]
temp = "test.csv"
any(temp.endswith(x) for x in [".xls", ".xlsx"])
"""


######## Retrieve files ------------------------------------------------------

# Select all A elements with href attributes containing URLs starting with http://
os.chdir("./data/")
for link in soup.select('a[href^="/file"]'):
    href = "https://www.mhlw.go.jp" + link.get('href')
    txt = link.get_text()
    
    # Make sure it has one of the correct name expressions
    if txt.startswith("（９）疾患別手術有無別処置1有無別集計_MDC"):
        # Make sure it has one of the correct extensions
        if any(href.endswith(x) for x in ['.csv','.xls','.xlsx']):
            #filename = href.rsplit('/', 1)[-1]
            filename = txt.split("（E")[0] + "_" + year[:6] + ".xls"
            print("Downloading %s to %s..." % (href, filename))
            urlretrieve(href, filename)
            print("Done.")

            
            
            

            
            
            
            
            
"""
reference: https://stackoverflow.com/questions/34632838/download-xls-files-from-a-webpage-using-python-and-beautifulsoup
"""