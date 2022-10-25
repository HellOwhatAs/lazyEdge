# Use selenium 4 Instead
[selenium](https://github.com/SeleniumHQ/Selenium)
```py
from selenium import webdriver

driver = webdriver.Edge()
driver.get('http://www.jwc.sjtu.edu.cn/info/1222/11988.htm')

driver.quit()
```

# ~~lazyEdge~~
~~A warp on ```selenium.webdriver.Edge``` that free you from managing msedgedriver.~~
# ~~requires~~
- ~~[bs4](https://pypi.org/project/beautifulsoup4/)~~
- ~~[requests](https://docs.python-requests.org/en/latest/)~~
- ~~[selenium](https://github.com/SeleniumHQ/selenium/)```==3.141.0```~~
# ~~install~~
```batch
::pip install lazyEdge
```
# ~~usage~~
```python
# from lazyEdge import lazyEdge as Edge
# edge=Edge()
# edge.get("https://www.bilibili.com/")
```
~~Just like ```selenium.webdriver.Edge``` since it's a subclass of it.~~

