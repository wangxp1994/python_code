
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings('ignore')

html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    
    <p class="story">...</p>
    </html>
"""

sp = BeautifulSoup(html)

# a = sp.prettify()         # 漂亮网页
# a = sp.getText()            # 网页全部文本内容
# a = sp.get_text()

# a = sp.title              # 元素选择
# a = sp.head
# a = sp.a

# a = sp.head.name          # 标签名称
# a = sp.a.string           # 标签内容

# a = sp.a['href']          # 标签内属性
# a = sp.a.attrs['href']

# a = sp.p.contents         # 标签子节点,返回列表

# a = sp.p.children         # 标签子节点,返回代器

# a = sp.a.parent           # 标签父节点

# a = sp.a.parents          # 标签祖先节点,返回迭代器

# a = sp.a.next_siblings    # 以下并列兄弟节点,返回迭代器

# a = sp.a.previous_siblings# 以上并列兄弟节点,返回迭代器

# print(a)


html = """
<div class="panel">
    <div class="panel-heading">
        <h3>hello</h3>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
"""

sp = BeautifulSoup(html)

# 标准选择器 find_all(name, attrs, recursive, text, **kwargs)

# 标签名查找
# b = sp.find_all('ul')
# for ul in b:
#     print(ul.find_all('li'))

# 属性名查找
# b = sp.find_all(attrs={'id':'list-1'})
# b = sp.find_all(id='list-1')
# b = sp.find_all(attrs={'class':'list'})
# b = sp.find_all(class_='list')

# 内容查找
# b = sp.find_all(text='Bar')

# b = sp.find('ul')['class']

# find_parent()
# find_parents()
# find_next_sibling()
# find_next_siblings()
# find_previous_sibling()
# find_previous_siblings()

# print(b)


# CSS选择器 如果选择了class属性，则在css选择器中要以.代替，而id以#代替

# c = sp.select('.panel-body #list-1')

# c = sp.select('ul li')

# print(c)



