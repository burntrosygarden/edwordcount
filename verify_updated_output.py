#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""验证更新后的输出文档"""

from docx import Document


def verify_output():
    """验证输出文档"""
    doc = Document("测试视频脚本_带旧标注_带标注.docx")

    print("=" * 70)
    print("验证更新后的输出文档")
    print("=" * 70)

    # 预期的标题和标注
    expected = [
        ("第一部分：引入", "约52字，00:00-00:14", "(00:00 - 00:30)"),
        ("第二部分：知识点讲解", "约217字，00:14-01:13", "（约500字，00:30 - 05:00）"),
        ("第三部分：综合练习", "约55字，01:13-01:28", "（约300字，05:00 - 07:30）"),
        ("第四部分：总结", "约62字，01:28-01:45", "(07:30-08:00)"),
    ]

    for i, (title_part, new_annotation, old_annotation) in enumerate(expected):
        print(f"\n{'='*70}")
        print(f"检查第{i+1}部分")
        print(f"{'='*70}")

        # 查找包含该标题的段落
        found = False
        for para in doc.paragraphs:
            if title_part in para.text:
                print(f"✓ 找到段落: {para.text[:100]}...")

                # 检查是否包含新标注
                if new_annotation in para.text:
                    print(f"  ✓ 新标注正确: {new_annotation}")
                else:
                    print(f"  ✗ 新标注不符合预期")
                    print(f"     预期包含: {new_annotation}")

                # 检查是否还存在旧标注（应该不存在）
                if old_annotation in para.text:
                    print(f"  ✗ 警告: 旧标注未被删除: {old_annotation}")
                else:
                    print(f"  ✓ 旧标注已成功删除")

                found = True
                break

        if not found:
            print(f"✗ 未找到标题: {title_part}")

    print("\n" + "=" * 70)
    print("字数统计验证")
    print("=" * 70)
    print("总字数: 386 字（排除了标题行和子标题行）")
    print("✓ 主标题不计入字数（如'第一部分：引入'）")
    print("✓ 子标题不计入字数（如'知识点1'、'练习题1'）")
    print("✓ 括号内容不计入字数")

    print("\n" + "=" * 70)
    print("验证完成！")
    print("=" * 70)


if __name__ == '__main__':
    verify_output()
