# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import mistune
import mistune_contrib.meta as m_meta

COMMON_CASE = '''
Title: A Metadata DEMO
Author: Hsiaoming Yang
        Zhechuan Chen,
Tags:   a, b, c

The Text are starting here...
'''

def test_common():
    a = m_meta.parse(COMMON_CASE, split_str=r'[\n,]')
    if a:
        meta, text = a
        print(">>-----The meta data ---------<<")
        print(meta)
        print("--------------------------------")
        print(">>-----The text data ---------<<")
        print(text)
        print("--------------------------------")

if __name__ == "__main__":
    test_common()
