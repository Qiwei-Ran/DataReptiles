# ***字符串与字节***
print(bytes([102, 111, 111]))
print(list(b'foo bar'))  # b是字节，只能用字节作为序列值，即 0 <= x <256 范围内的整数
print(list('foo bar'))  # python3默认不加前缀，都是str类型的,包括' " '''引起来的
# 转换为list等其他类型时就显示出原来面目
print(tuple(b'foo bar'))  # python要是表str，就必须加u前缀
print(type("some string"))
'''
# 如果 Unicode 字符串没有被编码为二进制数据的话，是无法保存在磁盘中或通过网络发送，要存储str到磁盘或发送网络，需要将unicode编码为序列字节
# bytes本是不可变的， bytearray可以像列表一样变化和操作。字符串也是不可变的，每次操作都会生成新的字符串实例
'''
# 字符串拼接，使用s="".join(substrings)替代a+=substring,性能更好。jion对大型列表性能快
# 还可以用于插入分割符号
a = ','.join(['some', 'comma', 'separated', 'values'])
print(a)
# 用str.format或者%拼接的话可读性比jion要好，但是性能会变差

# ***集合类型***
"""列表与元祖"""
# 列表是动态的，其大小可以改变；而元组是不可变的（因此就是可hash的），一旦创建就不能修改
'''
list.insert方法在任意位置插入一个元素 — 复杂度为O(n)
list.delete 或 del 删除一个元素 — 复杂度为 O(n)。
lis是数组，真正的链表可以使用双端队列deque
'''
'''
1.列表推导性能高于for遍历列表,然后采用append的方式。少了append操作
2.解释器在对列表推导进行求值的过程中并不知道最终
结果容器的大小，也就无法为它预先分配数组的最终大
小。因此，内部数组的重新分配方式与 for 循环中完
全相同。但在许多情况下，与普通循环相比，使用列表
推导创建列表要更加整洁、更加快速。
'''
print([i for i in range(10) if i % 2 == 0])

# 使用枚举的优化方法
for i, element in enumerate(['one', 'two', 'three']):
    print(i, element)
'''
输出:
0 one
1 two
2 three
'''

# zip库的使用，对俩个大小一致的可迭代对象均匀遍历
'''
for item in zip([1, 2, 3], [4, 5, 6]):
    print(item)
输出：
(1, 4)
(2, 5)
(3, 6)
再次调用zip会返回原装
for item in zip(*zip([1, 2, 3], [4, 5, 6])):
... print(item)
...
(1, 2, 3)
(4, 5, 6)
'''

# 序列解包 （可用于任意序列类型）
'''
将序列解包到另一组变量中
>>> first, second, third = "foo", "bar", 100
>>> first
'foo'
>>> second
'bar'
>>> third
100
----------
>>> # 带星号的表达式可以获取序列的剩余部分。中间部分也一样
>>> first, second, *rest = 0, 1, 2, 3
>>> first
0
>>> second
1
>>> rest
[2, 3]
----------
嵌套解包
>>> # 嵌套解包
>>> (a, b), (c, d) = (1, 2), (3, 4)
>>> a, b, c, d
(1, 2, 3, 4)
'''