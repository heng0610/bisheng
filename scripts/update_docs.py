#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bisheng → Terminus 文档更新脚本

功能：
1. 更新 README 文档
2. 更新项目描述
3. 保留 URL 引用
"""

import os
import re
from pathlib import Path
from datetime import datetime

# ==================== 配置 ====================
PROJECT_ROOT = Path(__file__).parent.parent

# 需要更新的文档文件
DOCUMENTS = [
    "README.md",
    "README_CN.md",
    "README_JPN.md",
    "SECURITY.md",
    "CLAUDE.md",
    "src/backend/README.md",
]

# 替换规则（文档专用）
REPLACEMENTS = {
    # 标题和描述（全大写）
    r'\bBISHENG\b': 'Terminus',

    # 首字母大写
    r'\bBisheng\b': 'Terminus',

    # 全小写
    r'\bbisheng\b': 'terminus',
}

# 需要保留原样的 URL 模式（不替换）
URL_PATTERNS = [
    r'https://github\.com/dataelement/bisheng',
    r'https://dataelem\.com/bs/',
    r'dataelement/bisheng',
    r'bisheng\.slack\.com',
    r'github\.com/dataelement/bisheng',
]

# ==================== 工具函数 ====================

def should_preserve_url(text: str) -> bool:
    """检查是否应该保留原始 URL"""
    for pattern in URL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False


def replace_in_document(file_path: Path, replacements: dict, dry_run: bool = False) -> dict:
    """在文档中执行智能替换"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content

        # 逐个应用替换规则
        for pattern, replacement in replacements.items():
            # 使用函数来判断每一行是否应该替换
            lines = content.split('\n')
            new_lines = []

            for line in lines:
                # 如果这行包含 URL，则跳过
                if should_preserve_url(line):
                    new_lines.append(line)
                else:
                    # 执行替换
                    new_line = re.sub(pattern, replacement, line)
                    new_lines.append(new_line)

            content = '\n'.join(new_lines)

        # 检查是否有变化
        if content != original_content:
            if not dry_run:
                # 写入文件时保持原有换行符
                file_path.write_text(content, encoding='utf-8')
            return {
                'file': str(file_path.relative_to(PROJECT_ROOT)),
                'status': 'modified' if not dry_run else 'dry_run'
            }

    except Exception as e:
        return {
            'file': str(file_path.relative_to(PROJECT_ROOT)),
            'error': str(e),
            'status': 'error'
        }

    return None


def update_pyproject(file_path: Path, dry_run: bool = False) -> dict:
    """更新 pyproject.toml"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original = content

        # 特定替换
        replacements = [
            (r'description = "BISHENG backend service"', 'description = "Terminus backend service"'),
            (r'description = "BISHENG', 'description = "Terminus'),
            (r'name = "bisheng', 'name = "terminus'),
        ]

        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)

        if content != original:
            if not dry_run:
                file_path.write_text(content, encoding='utf-8')
            return {
                'file': str(file_path.relative_to(PROJECT_ROOT)),
                'status': 'modified' if not dry_run else 'dry_run'
            }

    except Exception as e:
        return {
            'file': str(file_path.relative_to(PROJECT_ROOT)),
            'error': str(e),
            'status': 'error'
        }

    return None


def find_document_files() -> list[Path]:
    """查找所有需要更新的文档"""
    docs = []

    for doc_pattern in DOCUMENTS:
        file_path = PROJECT_ROOT / doc_pattern
        if file_path.exists():
            docs.append(file_path)

    return docs


# ==================== 主函数 ====================

def main(dry_run: bool = True):
    """主函数"""
    print("=" * 60)
    print("Bisheng → Terminus 文档更新工具")
    print("=" * 60)
    print(f"\n项目根目录: {PROJECT_ROOT}")
    print(f"模式: {'试运行（DRY RUN）' if dry_run else '实际执行'}\n")

    results = []

    # 1. 更新 README 等文档
    print("正在扫描文档文件...")
    doc_files = find_document_files()
    print(f"找到 {len(doc_files)} 个文档文件\n")

    print("正在更新文档...")
    for file_path in doc_files:
        result = replace_in_document(file_path, REPLACEMENTS, dry_run)
        if result:
            results.append(result)
            if result.get('status') in ['modified', 'dry_run']:
                print(f"  ✓ {file_path.relative_to(PROJECT_ROOT)}")
            elif result.get('status') == 'error':
                print(f"  ✗ {file_path.relative_to(PROJECT_ROOT)}: {result.get('error')}")

    # 2. 更新 pyproject.toml
    print("\n正在更新 pyproject.toml...")
    pyproject_path = PROJECT_ROOT / "src" / "backend" / "pyproject.toml"
    if pyproject_path.exists():
        result = update_pyproject(pyproject_path, dry_run)
        if result and result.get('status') in ['modified', 'dry_run']:
            results.append(result)
            print(f"  ✓ {pyproject_path.relative_to(PROJECT_ROOT)}")

    # 生成报告
    print("\n" + "=" * 60)
    print("执行摘要")
    print("=" * 60)

    modified = [r for r in results if r and r.get('status') in ['modified', 'dry_run']]
    errors = [r for r in results if r and r.get('status') == 'error']

    print(f"扫描文件: {len(doc_files) + (1 if pyproject_path.exists() else 0)}")
    print(f"修改文件: {len(modified)}")
    print(f"错误文件: {len(errors)}")

    if errors:
        print("\n错误列表:")
        for err in errors:
            print(f"  - {err['file']}: {err.get('error')}")

    if dry_run:
        print("\n✅ 试运行完成！")
        print("   使用 --execute 参数实际执行")
        print("   python scripts/update_docs.py --execute")
    else:
        print("\n✅ 文档更新完成！")
        print("   请检查并提交修改")

    return 0 if not errors else 1


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Bisheng → Terminus 文档更新工具"
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='实际执行修改（默认为试运行模式）'
    )

    args = parser.parse_args()

    main(dry_run=not args.execute)
