# coding: utf-8
from numpy.random import randint
from numpy.random import choice
words='''
我
我的
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止
椎間盤'''
phrase = words.split('\n')
n = randint(3, 6)

for i in range(n):
    k = randint(5, 8)
    egg = choice(phrase, k)
    ham = ' '.join(egg)
    print(ham)
