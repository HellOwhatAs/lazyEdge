***

<center><h1 style="color:red;"><b>WARNING: Works Only On Windows</b></h1></center>

***

# lazyEdge
A warp on ```selenium.webdriver.Edge``` that free you from managing msedgedriver.
# requires
- [bs4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://docs.python-requests.org/en/latest/)
- [selenium](https://github.com/SeleniumHQ/selenium/)==3
# install
```
pip install lazyEdge
```
# usage
```python
from lazyEdge import lazyEdge as Edge
edge=Edge()
edge.get("https://www.bilibili.com/")
```
Just like ```selenium.webdriver.Edge``` since it's a subclass of it.
