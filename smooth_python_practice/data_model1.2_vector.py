from math import hypot

"""自定义二维向量运算的例子"""

'''
内置complex类表示二维向量
abs类返回绝对值，当输入为二维向量时，输出的是模
构建一个有如下功能的vector类：
>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1 + v2
Vector(4, 5)
---------------
>>> v * 3   # 模变长
Vector(9, 12)
>>> abs(v * 3)
15.0

'''


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __repr__与__str__区别：__str__在用print打印对象的时候或者str()才会调用，且更友好

    def __repr__(self):
        """
        一个对象的字符串表示形式，不实现的话，打印对象的时候，默认类似 <Vector object at 0x10e100070>
        __repr__应该是最好的选择，没有__str__的时候，会用__repr__替代
        :return: %r表对象的属性
        """
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)  # 计算的是模的绝对值，平方和再开平方根

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):  # 乘法
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(3, 4)
    v2 = Vector(2, 3)
    print(v1 + v2)  # 因为v1,v2是对象，打印出来的本是内存地址，但是__repr__改变了显示的内容
    v3 = Vector(0, 1)
    print(bool(v3))
