# lazyEdge
A warp on selenium.webdriver.Edge that free you from managing msedgedriver.
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
Just like selenium.webdriver.Edge since it's a subclass of ```selenium.webdriver.Edge```.
