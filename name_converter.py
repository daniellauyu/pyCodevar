#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PyCodeVar 
@Software : PyCharm
@File ：name_converter.py
@Author ：daniel lau
@Date ：2023/8/25 21:27
@site : www.liuyude.com
@describe : 变量规则转换类
"""

import re

class NameConverter(object):

    @staticmethod
    def _clean_input(s: str) -> str:
        """Removes all non-alphanumeric characters and replaces them with spaces."""
        return re.sub(r'[^a-zA-Z0-9]', ' ', s)

    @staticmethod
    def to_pascal_case(s: str) -> str:
        s = NameConverter._clean_input(s)
        words = s.split()
        return ''.join(word.capitalize() for word in words)

    @staticmethod
    def to_camel_case(s: str) -> str:
        s = NameConverter._clean_input(s)
        words = s.split()
        if not words:  # Check if the list is empty
            return ''
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

    @staticmethod
    def to_named_constant(s: str) -> str:
        s = NameConverter._clean_input(s)
        words = s.split()
        return '_'.join(word.upper() for word in words)

    @staticmethod
    def to_underline(s: str) -> str:
        s = NameConverter._clean_input(s)
        words = s.split()
        return '_'.join(word.lower() for word in words)

    @staticmethod
    def to_hyphen(s: str) -> str:
        s = NameConverter._clean_input(s)
        words = s.split()
        return '-'.join(word.lower() for word in words)