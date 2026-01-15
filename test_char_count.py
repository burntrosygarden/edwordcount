#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试字数统计逻辑"""

import re

text = """Hello everyone! 欢迎来到我们的"语法基地"！我是你们的首席语法工程师，Jade！

(凑近镜头，神秘地) 有些同学一听到"语法"这两个字，眉头就皱成了一个大大的"川"字。是不是觉得语法就是一堆枯燥的规则，听着就头大？

其实啊，你们被骗啦！学语法根本不是死记硬背。大家可以把学英语想象成是盖一座摩天大楼。我们背的那些单词，就是一块块砖头、水泥，它们是建筑材料。语法就是大楼的钢筋骨架！只要把骨架搭好，材料填进去，这栋大楼就会稳稳当当，又漂亮又结实！

在这门课程里，Jade老师会带着大家，从零开始，亲手搭建属于你自己的英语大厦！今天我们的任务是——打牢地基！也是对我们整个30天课程知识点的一个提前剧透！因为所有的课程都会围绕今天的"地基内容"展开。只要搞定今天这三个核心概念，我保证，你以后看英语句子的眼光都会不一样。

Are you ready? Let's build!"""

# 移除括号内容
def remove_brackets(text):
    BRACKET_PAIRS = [
        ('(', ')'),
        ('（', '）'),
        ('[', ']'),
        ('【', '】'),
        ('「', '」'),
        ('『', '』'),
        ('{', '}'),
        ('｛', '｝'),
    ]

    result = text
    for open_br, close_br in BRACKET_PAIRS:
        while True:
            open_escaped = re.escape(open_br)
            close_escaped = re.escape(close_br)
            pattern = open_escaped + r'[^' + open_escaped + close_escaped + r']*?' + close_escaped
            new_result = re.sub(pattern, '', result)
            if new_result == result:
                break
            result = new_result
    return result

print("=" * 70)
print("字数统计分析")
print("=" * 70)

# 1. 原始文本
text_no_space = re.sub(r'\s+', '', text)
print(f"\n1. 原始文本（包括括号）:")
print(f"   所有字符（含空白）: {len(text)}")
print(f"   去除空白后: {len(text_no_space)}")

# 2. 去除括号后
text_no_brackets = remove_brackets(text)
text_no_brackets_no_space = re.sub(r'\s+', '', text_no_brackets)
print(f"\n2. 去除括号后:")
print(f"   所有字符（含空白）: {len(text_no_brackets)}")
print(f"   去除空白后: {len(text_no_brackets_no_space)}")

# 3. 详细分类统计（去除括号后）
text_clean = text_no_brackets_no_space
chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text_clean))
english_chars = len(re.findall(r'[a-zA-Z]', text_clean))
digits = len(re.findall(r'\d', text_clean))
punctuation = len(re.findall(r'[^\w\s]', text_clean, re.UNICODE))

print(f"\n3. 字符分类（去除括号和空白后）:")
print(f"   中文字符: {chinese_chars}")
print(f"   英文字母: {english_chars}")
print(f"   数字: {digits}")
print(f"   标点符号: {punctuation}")
print(f"   总计: {len(text_clean)}")

# 4. 不同统计方法对比
print(f"\n4. 不同统计方法对比（去除括号后）:")

# 方法1: 当前方法 - 所有非空白字符
method1 = len(text_no_brackets_no_space)
print(f"   方法1 - 所有非空白字符: {method1}")

# 方法2: 只统计中文字符
chinese_in_text = re.findall(r'[\u4e00-\u9fff]', text_no_brackets)
method2 = len(chinese_in_text)
print(f"   方法2 - 仅中文字符: {method2}")

# 方法3: 中文字符 + 英文单词数
english_words_list = re.findall(r'[a-zA-Z]+', text_no_brackets)
english_words = len(english_words_list)
method3 = chinese_chars + english_words
print(f"   方法3 - 中文字符 + 英文单词数: {method3}")
print(f"           (中文: {chinese_chars} + 英文单词: {english_words})")

# 方法4: 中文字符 + 英文字母 (不含标点)
method4 = chinese_chars + english_chars
print(f"   方法4 - 中文字符 + 英文字母: {method4}")

# 方法5: 所有字母数字（不含标点）
alphanumeric_list = re.findall(r'[\u4e00-\u9fff\w]', text_no_brackets, re.UNICODE)
alphanumeric = len(alphanumeric_list)
print(f"   方法5 - 所有字母数字（不含标点）: {alphanumeric}")

print("\n" + "=" * 70)
print("分析结论:")
print("=" * 70)
print(f"用户说的346字，最接近的是方法3（中文+英文单词数）: {method3}")
print(f"当前工具统计的是方法1（所有非空白字符）: {method1}")
print(f"差异: {method1 - method3} 个字符")
