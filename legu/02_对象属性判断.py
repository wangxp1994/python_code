
class Book(object):
    def __init__(self,name,author,price):
        self.name = name
        self.author = author
        self.price = price     

sanguo = Book("三国演义", "罗贯中", 25)

print(hasattr(sanguo, "name"))  # 判断是否拥有该属性
print(hasattr(sanguo, "sex"))

print(getattr(sanguo, "name"))  # 获取该属性的值
print(getattr(sanguo, "sex", "保密"))

setattr(sanguo, "price", 36)    # 设置该属性的值
print(sanguo.price)

setattr(sanguo, "sex", "保密")
print(sanguo.sex)



