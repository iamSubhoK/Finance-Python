# Tutorial

### 确认安装

安装完成``Finance-Python``之后，应该可以在例如``ipython``中直接导入：

```python
In [1]: import PyFin

In [2]: PyFin.__version__
Out[2]: '0.4.2'
```

如果获得上述类似的输出，证明``Finance-Python``已经在电脑上正确安装。如果有例如``ImportError``等异常，请回到[README](../../README.md)按照步骤以及依赖重新安装。


### Hello World!

最简单的使用``Finance-Python``的方法是直接使用它对外提供的``api``:

```python
In [3]: from PyFin import api
```

下面的代码获取2016年12月的所有工作日：

```python
In [5]: api.bizDatesList('china.sse', '2016-12-01', '2016-12-31')
Out[5]:
[datetime.date(2016, 12, 1),
 datetime.date(2016, 12, 2),
 datetime.date(2016, 12, 5),
 datetime.date(2016, 12, 6),
 datetime.date(2016, 12, 7),
 datetime.date(2016, 12, 8),
 datetime.date(2016, 12, 9),
 datetime.date(2016, 12, 12),
 datetime.date(2016, 12, 13),
 datetime.date(2016, 12, 14),
 datetime.date(2016, 12, 15),
 datetime.date(2016, 12, 16),
 datetime.date(2016, 12, 19),
 datetime.date(2016, 12, 20),
 datetime.date(2016, 12, 21),
 datetime.date(2016, 12, 22),
 datetime.date(2016, 12, 23),
 datetime.date(2016, 12, 26),
 datetime.date(2016, 12, 27),
 datetime.date(2016, 12, 28),
 datetime.date(2016, 12, 29),
 datetime.date(2016, 12, 30)]

```

