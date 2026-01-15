#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试更新后的字数统计方法"""

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

# 新的字数统计方法（Word标准）
def count_characters_word_style(text):
    """Word标准：中文字符数 + 英文单词数 + 数字"""
    # 统计中文字符（包括汉字和中文标点）
    # Unicode范围：
    # \u4e00-\u9fff: CJK统一汉字
    # \u3000-\u303f: CJK符号和标点
    # \uff00-\uffef: 全角ASCII、全角标点
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', text))

    # 统计英文单词数（包括缩写词）
    english_words = len(re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)?", text))

    # 统计数字
    digits = len(re.findall(r'\d', text))

    return chinese_chars, english_words, digits, chinese_chars + english_words + digits

print("=" * 70)
print("字数统计测试（Word标准）")
print("=" * 70)

# 1. 包含括号
print("\n1. 原文本（包含括号）:")
c1, e1, d1, t1 = count_characters_word_style(text)
print(f"   中文字符: {c1}")
print(f"   英文单词: {e1}")
print(f"   数字: {d1}")
print(f"   总计: {t1}")

# 2. 去除括号
text_no_brackets = remove_brackets(text)
print("\n2. 去除括号后:")
c2, e2, d2, t2 = count_characters_word_style(text_no_brackets)
print(f"   中文字符: {c2}")
print(f"   英文单词: {e2}")
print(f"   数字: {d2}")
print(f"   总计: {t2}")

print("\n" + "=" * 70)
print("英文单词列表（去除括号后）:")
print("=" * 70)
english_words_list = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)?", text_no_brackets)
for i, word in enumerate(english_words_list, 1):
    print(f"{i:2d}. {word}")

print("\n" + "=" * 70)
print("结论:")
print("=" * 70)
print(f"按Word标准（中文字符+英文单词+数字），去除括号后共: {t2} 字")
print(f"用户说的是: 346 字")
print(f"差异: {abs(346 - t2)} 字")
