#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import xml.etree.ElementTree as etree

"""
工厂方法:执行单个函数，传入一个参数（表明我们想要什么），不需要关注具体实现，以及来自哪里
"""


# ***一，创建不同功能的具体实现的类***
class JSONConnector(object):
    """The class is a json parse class"""

    def __init__(self, file_path):
        self.data = dict()
        with open(file_path, mode='r') as f:
            self.data = json.load(f)  # json load后是字典格式

    @property
    def parsed_data(self):
        """
        :return: the data of parsed json
        """
        return self.data


class XMLConnector(object):
    def __init__(self, file_path):
        self.tree = etree.parse(file_path)  # 是一个etree的对象

    @property
    def parsed_data(self):
        return self.tree


# ***二，创建一个工厂方法***
def connector_factory(file_path):  # 该方法等同于一个调用入口，表示工厂, 调用连接器
    """
    :param file_path:
    :return:judge different input and return invoke different class.
    """
    if file_path.endswith('json'):
        connector = JSONConnector
    elif file_path.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cant connect to {}'.format(file_path))  # 抛出异常
    return connector(file_path)


# ***三，对入口进行一层包装，添加异常处理
def connect_to(file_path):
    factory = None
    try:
        factory = connector_factory(file_path)
    except ValueError as ve:  # 捕捉并打印异常，但是程序不中断，返回None
        print (ve)
    return factory


# ***四，使用该工厂方法的函数***
def main():
    sqlite_dactory = connect_to('d/ata/person.sq3')
    print ('{} \n'.format(sqlite_dactory))

    xml_factory = connect_to('data/person.xml')  # 只是进行了类的实例化,初始化了数据,返回一个对象
    xml_data = xml_factory.parsed_data  # 调用才返回
    print (xml_data)
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))  # 限定条件查找
    print ('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('\n first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        for p in liar.find('phoneNumbers'):
            print('phone number ({}):'.format(p.attrib['type']), p.text)
    print('\n')

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print (json_data)
    print ('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print ('\n name: {}'.format(donut['name']))
        print ('prince: {}'.format(donut['ppu']))
        for t in donut['topping']:
            print ('topping: {}'.format(t['id'], t['type']))


if __name__ == '__main__':
    main()
