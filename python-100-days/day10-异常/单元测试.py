"""
 @Time: 2021/5/17 17:42
 @Author: flying
 @Desc: https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936
"""
import unittest
from Dict import *

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d = Dict()
