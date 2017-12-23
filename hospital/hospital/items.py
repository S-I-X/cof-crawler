# -*- coding: utf-8 -*-
'''
Created on 2017��10��19��

@author: sangfor
'''
import scrapy
class  hospitalItem(scrapy.Item):
     #ҽԺ��
     name=scrapy.Field()
     #url
     url=scrapy.Field()
class  hospitalDetailItem(scrapy.Item):
     #url
     url=scrapy.Field()
     #ҽԺ����
     nickname=scrapy.Field()
     #ҽԺ����
     property=scrapy.Field()
     #ҽԺ�ȼ�
     rank=scrapy.Field()
     #��ϵ�绰
     tel=scrapy.Field()
     #��ַ
     address=scrapy.Field()