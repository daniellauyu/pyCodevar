#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PyCodeVar 
@Software : PyCharm
@File ：filter.py
@Author ：daniel lau
@Date ：2023/8/10 16:20
@site : www.liuyude.com
@describe : 过滤一些连接词、前后缀
"""


class TextFilter(object):
    def __init__(self):
        # Filter criteria as provided
        self.filter_criteria = {
            'prep': ['and', 'or', 'the', 'a', 'at', 'of'],
            'prefix': [''],  # This is an empty prefix which would cause issues, let's handle it
            'suffix': ['ing', 'ed', 'ly'],
            'verb': ['was']
        }

    def filter_text(self, text):
        # Splitting the text into words
        words = text.split()

        # Filtering out words based on prep and verb criteria
        filtered_words = [word for word in words if
                          word.lower() not in self.filter_criteria['prep'] and word.lower() not in self.filter_criteria[
                              'verb']]

        # Filtering out words based on prefix and suffix criteria
        for prefix in self.filter_criteria['prefix']:
            if prefix:  # Check if prefix is not empty
                filtered_words = [word for word in filtered_words if not word.lower().startswith(prefix)]

        for suffix in self.filter_criteria['suffix']:
            if suffix:  # Check if suffix is not empty
                filtered_words = [word for word in filtered_words if not word.lower().endswith(suffix)]

        # Joining the filtered words back into a text
        filtered_text = ' '.join(filtered_words)

        # Remove the ' character from the filtered text
        filtered_text = filtered_text.replace("'", "")

        return filtered_text