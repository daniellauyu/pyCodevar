#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PyCodeVar 
@Software : PyCharm
@File ：xh.py
@Author ：daniel lau
@Date ：2023/8/27 00:55
@site : www.liuyude.com
@describe : 这里是描述
"""
import sys
from name_converter import NameConverter
from translator import YoudaoTranslator
from filter import TextFilter
import json


def main():
    q = sys.argv[1]
    # 输入查询字符串
    # q = "吃个饭"

    # 初始化翻译器和文本过滤器
    translator = YoudaoTranslator()
    text_filter = TextFilter()

    # 进行翻译，并获取翻译结果
    translation_result = translator.translate(q)
    items = translation_result.get('items', [])

    # 过滤和转换标题（title）
    filtered_and_converted_items = []
    for item in items:
        title = item['title']

        # 使用文本过滤器进行过滤
        filtered_title = text_filter.filter_text(title)

        # 使用 NameConverter 进行命名转换，这里以转换为驼峰式为例
        converted_title = NameConverter.to_underline(filtered_title)

        # 如果转换后的标题不为空，则添加到结果中
        if converted_title:
            new_item = item.copy()
            new_item['title'] = converted_title
            new_item['arg'] = converted_title  # 这里更新了 'arg' 的值
            filtered_and_converted_items.append(new_item)

    # 生成新的 Alfred 输出
    filtered_and_converted_result = {'items': filtered_and_converted_items}

    # Convert the dictionary to a JSON-formatted string
    json_str = json.dumps(filtered_and_converted_result, ensure_ascii=False)

    # Print or return the JSON-formatted string
    print(json_str)


if __name__ == '__main__':
    main()