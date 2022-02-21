from io import BytesIO
from bs4 import BeautifulSoup
from selenium.webdriver import Edge
import os,requests,zipfile
_fp=os.path.dirname(os.path.abspath(__file__))
def _getmsedgedriver():
    resp=requests.get("https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")
    soup=BeautifulSoup(resp.content,"lxml")
    url=soup.select_one(".driver-download__meta").select_one("a")["href"]
    resp=requests.get(url)
    with zipfile.ZipFile(BytesIO(resp.content),"r")as z:
        with open(os.path.join(_fp,"msedgedriver.py"),"wb") as f:
            f.write(z.read("msedgedriver.exe"))
class lazyEdge(Edge):
    def __init__(self,headless=False):
        capabilities={"ms:edgeOptions":{'extensions': [],'args': ['--headless','--disable-gpu',]}} if headless else None
        try:
            super(lazyEdge,self).__init__(os.path.join(_fp,"msedgedriver.py"),capabilities=capabilities)
        except:
            _getmsedgedriver()
            super(lazyEdge,self).__init__(os.path.join(_fp,"msedgedriver.py"),capabilities=capabilities)
    def __del__(self):
        self.quit()

if __name__=="__main__":
    a=lazyEdge()
    a.get("https://www.bilibili.com/")