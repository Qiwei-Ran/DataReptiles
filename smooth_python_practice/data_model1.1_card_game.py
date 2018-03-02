import collections
from random import choice

"""特殊方法1.-纸牌游戏"""
# __getitem__()样式的是特殊方法，被框架本身调用（也叫魔术方法）
'''
1.namedtuple ，用以构建只有少数属性但是没有方法的对象.创建简单类
2.通过实现特殊方法来利用 Python 数据模型的两个好处：
    a.作为你的类的用户，他们不必去记住标准操作的各式名称
    b.可以更加方便地利用 Python 的标准库，比如 random.choice 函数
3.特殊方法的存在是为了被 Python 解释器调用的
4.执行 len(my_object) 的时候，如果 my_object 是一个自定义类的对象，那么 Python 会
自己去调用其中由你实现的 __len__ 方法。如果是python内置的数据类型，len是直接读取的ob_size属性（更快）
通过内置的函数（例如 len、iter、str，等等）来使用特殊方法是最好的选择
'''
# 构建一个纸牌的简单类
Card = collections.namedtuple('Card', ['rank', 'suit'])

# 构建单张纸牌测试
beer_card = Card('7', 'diamonds')
print(beer_card)


# 对序列数据类型的模拟是特殊方法用得最多的地方
# 将对象变成可迭代的，因为实例化后就变成列表了
class FrenchDeck:  # 一叠纸牌的类， 将其他类对象建成列表作为自己的元素
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]  # 列表中是多个Card实例化的对象

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):  # 将Card类的对象集合列表作为可迭代的， 可以像操作列表一样操作对象
        return self._cards[position]


if __name__ == '__main__':
    # 查看一叠纸牌有多少张
    deck = FrenchDeck()
    print(len(deck))

    # 抽取特定纸牌
    print('first:', deck[0])
    print('last: ', deck[-1])

    # 随机抽取卡牌
    print('random:', choice(deck))

    # 取范围
    print('tree first:', deck[:3])

    # 迭代
    '''for card in reversed(deck):  # doctest: +ELLIPSIS
        print('iter:', card)'''

    '''
    譬如说一个集合类型没有实现__contains__方法，
    那么 in 运算符就会按顺序做一次迭代搜索'''
    print(Card('Q', 'hearts') in deck)

    # 排序
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]  # 将rank的每个值与suit花色求和，再排序


    for card in sorted(deck, key=spades_high):  # 排完顺序再迭代打印，deck是一个列表对象，每个deck对象都有一个key
        print(card)
