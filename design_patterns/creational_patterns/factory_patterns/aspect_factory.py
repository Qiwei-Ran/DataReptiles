#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""抽象工厂设计模式是抽象方法的一种泛化，单个类包含许多个工厂方法，
抽象工厂是一组（逻辑上）工厂方法，其中每个工厂方法产生不同种类的对象，
开始时使用工厂方法，当需要很多工厂方法时，再引入抽象工厂，
抽象工厂可改变激活的工厂方法，列如：改变窗口风格（不用重启）
场景：(a)想要追踪对象的创建时，
(b)想要将对象的创建与使用解耦时，
(c)想要优化应用的性能和资源占用时。
"""


# 包含两个游戏，一个面向孩子，一个面向成人。
# 在运行时，基于用户输入，决定该创建哪个游戏并运行。游戏的
# 创建部分由一个抽象工厂维护

# ***创建具体实现的类***
class Frog(object):
    """Create a frog object contain interact_with method"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print ('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))


class Bug(object):
    """The class will create a bug object"""

    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


# ***抽象工厂（包含了俩个工厂方法）***
class FrogWorld(object):
    def __init__(self, name):
        print (self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------Frog World------'

    def make_character(self):  # 工厂方法1
        return Frog(self.player_name)

    def make_obstacle(self):  # 工厂方法2
        return Bug()


# ***第二个游戏的具体实现类***
class Wizard(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print ('{} the Wizard battles against {} and {}!'.format(self, obstacle, obstacle.action()))


class Ork(object):
    def __str__(self):
        return 'an evil prk'

    def action(self):
        return 'kills it'


# 创建抽象工厂
class WizardWorld(object):
    def __init__(self, name):
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork


# 游戏的主入口
class GameEnvironment(object):
    def __init__(self, factory):  # 通过工厂创建角色，可以传入不同的抽象工厂
        self.hero = factory.make_character()  # 调用一个工厂方法， 不同抽象工厂有相同的该抽象方法.生成一个对象
        self.obstacle = factory.make_obstacle()

    def play(self):  # 游戏中角色的交互
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input('Welcom {}, How old are you?'.format(name))
        age = int(age)
    except ValueError as err:
        print ("Age {} is invalid , please try again...".format(age))
        return False, age
    return True, age


def main():
    name = input("Hello, What's your name?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)  # 对输入进行校验
    game = FrogWorld if age < 18 else WizardWorld  # 根据年龄不同选择不同的抽象工厂
    environment = GameEnvironment(game(name))  # 通过不同的工厂创建角色， game(name)已经通过不同的工厂创建了
    environment.play()  # 执行交互


if __name__ == '__main__':
    main()
