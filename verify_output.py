#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""验证输出文档是否正确添加了标注"""

from docx import Document


def verify_output():
    """验证输出文档"""
    doc = Document("测试视频脚本_带标注.docx")

    print("=" * 60)
    print("输出文档验证")
    print("=" * 60)

    # 预期的标题和标注
    expected = [
        ("第一部分：引入", "约79字，00:00-00:22"),
        ("第二部分：知识点讲解", "约306字，00:22-01:45"),
        ("第三部分：综合练习", "约173字，01:45-02:32"),
        ("第四部分：总结", "约112字，02:32-03:03"),
    ]

    for i, (title_part, annotation_part) in enumerate(expected):
        # 查找包含该标题的段落
        found = False
        for para in doc.paragraphs:
            if title_part in para.text:
                print(f"\n✓ 找到: {para.text}")

                # 检查是否包含预期的标注
                if annotation_part in para.text:
                    print(f"  ✓ 标注正确: {annotation_part}")
                else:
                    print(f"  ✗ 标注不符合预期")
                    print(f"     预期包含: {annotation_part}")

                found = True
                break

        if not found:
            print(f"\n✗ 未找到标题: {title_part}")

    print("\n" + "=" * 60)
    print("验证完成！")
    print("=" * 60)


if __name__ == '__main__':
    verify_output()
