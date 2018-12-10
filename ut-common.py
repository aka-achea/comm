#!/usr/bin/python
#coding:utf-8

import unittest,configparser


# customized module
import openlink



class Test_openlink(unittest.TestCase):
 
    def setUp(self):
        print('setUp...')
 
    def tearDown(self):
        print('tearDown...')

    def test_op_simple(self):
        print('Test op_simple')
        url = 'http://www.xiami.com/widget/xml-single/sid/1769402049'
        html = openlink.op_simple(url)
        # print(url)
        self.assertEqual(html[1],200)
 
if __name__ == '__main__':
	unittest.main()
