#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试删除旧标注功能"""

import re

def remove_old_annotation(text):
    """删除标题中已有的时间标注"""
    # 匹配各种时间标注格式（从复杂到简单，避免误删）
    patterns = [
        r'[（(]\s*约?\s*\d+\s*字\s*[,，]\s*\d{1,2}:\d{2}\s*[-\-~～]\s*\d{1,2}:\d{2}\s*[）)]',  # (约150字，00:45-06:30)
        r'[（(]\s*\d{1,2}:\d{2}\s*[-\-~～]\s*\d{1,2}:\d{2}\s*[）)]',  # (00:45-06:30) 或 (0:00 - 0:45)
        r'[（(]\s*约?\s*\d+\s*字\s*[）)]',  # (约150字) 或 (157字)
    ]

    result = text
    for pattern in patterns:
        result = re.sub(pattern, '', result)

    return result.strip()


# 测试用例
# 注意：remove_old_annotation() 会删除所有旧标注，工具稍后会添加新的标注
test_cases = [
    ("第一部分：引入（约327字，00:00-01:29）", "第一部分：引入"),  # 即使是新格式也要删除，稍后会添加最新计算的标注
    ("第一部分：引入 (157字) (0:00 - 0:45)（约327字，00:00-01:29）", "第一部分：引入"),  # 用户的case - 删除所有旧标注
    ("第二部分：知识点讲解(00:45 - 06:30)", "第二部分：知识点讲解"),
    ("第三部分：综合练习（约300字，05:00 - 07:30）", "第三部分：综合练习"),
    ("第四部分：总结(157字)", "第四部分：总结"),
    ("第一部分：引入 (0:00 - 0:45)", "第一部分：引入"),
    ("第二部分：知识点讲解 (约500字) (0:45-6:30)", "第二部分：知识点讲解"),
]

print("=" * 70)
print("测试删除旧标注功能")
print("=" * 70)

all_passed = True
for i, (input_text, expected) in enumerate(test_cases, 1):
    result = remove_old_annotation(input_text)
    passed = (result == expected)
    all_passed = all_passed and passed

    status = "✓" if passed else "✗"
    print(f"\n测试 {i}: {status}")
    print(f"  输入: {input_text}")
    print(f"  期望: {expected}")
    print(f"  结果: {result}")
    if not passed:
        print(f"  ❌ 失败！")

print("\n" + "=" * 70)
if all_passed:
    print("✅ 所有测试通过！")
else:
    print("❌ 部分测试失败！")
print("=" * 70)
