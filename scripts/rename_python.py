#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bisheng → Terminus Python 文件重命名脚本

功能：
1. 批量替换 Python 文件中的导入语句
2. 替换类名、函数名（可选）
3. 生成修改报告
"""

import os
import re
from pathlib import Path
from datetime import datetime

# ==================== 配置 ====================
PROJECT_ROOT = Path(__file__).parent.parent
SOURCE_DIR = PROJECT_ROOT / "src" / "backend"

# 替换规则
REPLACEMENTS = {
    # 导入语句（必须）
    r'import bisheng\b': 'import terminus',
    r'from bisheng\b': 'from terminus',
    r'import bisheng_langchain\b': 'import terminus_langchain',
    r'from bisheng_langchain\b': 'from terminus_langchain',

    # 类名（可选，谨慎使用）
    r'\bBishengConfig\b': 'TerminusConfig',
    r'\bBishengClient\b': 'TerminusClient',

    # 字符串中的引用（需要仔细检查）
    r'"bisheng': '"terminus',  # 双引号
    r"'bisheng": "'terminus'",  # 单引号
}

# 排除的目录
EXCLUDE_DIRS = {
    '.git',
    '__pycache__',
    'node_modules',
    '.pytest_cache',
    'venv',
    'env',
    '.venv',
    'dist',
    'build',
    '*.egg-info',
}

# 排除的文件
EXCLUDE_PATTERNS = {
    '*.pyc',
    '*.pyo',
    '*.pyd',
    '.DS_Store',
    'Thumbs.db',
}

# ==================== 工具函数 ====================

def should_exclude(path: Path) -> bool:
    """检查路径是否应该被排除"""
    # 检查目录
    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True

    # 检查文件模式
    for pattern in EXCLUDE_PATTERNS:
        if path.match(pattern):
            return True

    return False


def find_python_files(directory: Path) -> list[Path]:
    """查找所有 Python 文件"""
    python_files = []
    for root, dirs, files in os.walk(directory):
        # 过滤排除的目录
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            file_path = Path(root) / file
            if not should_exclude(file_path) and file_path.suffix == '.py':
                python_files.append(file_path)

    return python_files


def replace_in_file(file_path: Path, replacements: dict, dry_run: bool = True) -> dict:
    """在文件中执行替换"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content

        changes = []
        for pattern, replacement in replacements.items():
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, replacement, content)
                changes.append({
                    'pattern': pattern,
                    'replacement': replacement,
                    'count': len(matches)
                })

        if content != original_content:
            if not dry_run:
                file_path.write_text(content, encoding='utf-8')
            return {
                'file': str(file_path.relative_to(PROJECT_ROOT)),
                'changes': changes,
                'status': 'modified' if not dry_run else 'dry_run'
            }

    except Exception as e:
        return {
            'file': str(file_path.relative_to(PROJECT_ROOT)),
            'error': str(e),
            'status': 'error'
        }

    return None


def generate_report(results: list, dry_run: bool = True) -> str:
    """生成修改报告"""
    report_lines = [
        "# Bisheng → Terminus 重命名报告",
        f"\n生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"模式: {'试运行（不会修改文件）' if dry_run else '实际执行'}",
        f"\n{'='*60}\n",
    ]

    # 统计
    modified = [r for r in results if r and r.get('status') in ['modified', 'dry_run']]
    errors = [r for r in results if r and r.get('status') == 'error']

    report_lines.extend([
        f"## 统计摘要",
        f"- 扫描文件数: {len(results)}",
        f"- 修改文件数: {len(modified)}",
        f"- 错误文件数: {len(errors)}",
        f"\n{'='*60}\n",
    ])

    # 详细修改列表
    if modified:
        report_lines.append("## 修改详情\n")
        for item in modified:
            report_lines.append(f"### {item['file']}")
            report_lines.append(f"状态: {item['status']}")
            for change in item.get('changes', []):
                report_lines.append(
                    f"  - `{change['pattern']}` → `{change['replacement']}` "
                    f"({change['count']} 处)"
                )
            report_lines.append("")

    # 错误列表
    if errors:
        report_lines.append("## 错误列表\n")
        for item in errors:
            report_lines.append(f"### {item['file']}")
            report_lines.append(f"错误: {item.get('error', 'Unknown')}")
            report_lines.append("")

    # 建议
    if dry_run:
        report_lines.extend([
            "## 下一步",
            "",
            "1. 检查上述修改是否正确",
            "2. 确认无误后，运行实际执行:",
            "   ```bash",
            "   python scripts/rename_python.py --execute",
            "   ```",
            ""
        ])

    return '\n'.join(report_lines)


# ==================== 主函数 ====================

def main(dry_run: bool = True):
    """主函数"""
    print("=" * 60)
    print("Bisheng → Terminus Python 文件重命名工具")
    print("=" * 60)
    print(f"\n项目根目录: {PROJECT_ROOT}")
    print(f"源代码目录: {SOURCE_DIR}")
    print(f"模式: {'试运行（DRY RUN）' if dry_run else '实际执行'}\n")

    # 查找 Python 文件
    print("正在扫描 Python 文件...")
    python_files = find_python_files(SOURCE_DIR)
    print(f"找到 {len(python_files)} 个 Python 文件\n")

    # 执行替换
    print("正在执行替换...")
    results = []
    for i, file_path in enumerate(python_files, 1):
        if i % 50 == 0:
            print(f"  进度: {i}/{len(python_files)}")

        result = replace_in_file(file_path, REPLACEMENTS, dry_run)
        if result:
            results.append(result)

    print(f"\n完成！处理了 {len(results)} 个文件\n")

    # 生成报告
    report = generate_report(results, dry_run)
    report_file = PROJECT_ROOT / "RENAME_PYTHON_REPORT.md"

    report_file.write_text(report, encoding='utf-8')
    print(f"报告已生成: {report_file}\n")

    # 显示摘要
    modified = [r for r in results if r and r.get('status') in ['modified', 'dry_run']]
    errors = [r for r in results if r and r.get('status') == 'error']

    print("=" * 60)
    print("执行摘要:")
    print(f"  扫描文件: {len(python_files)}")
    print(f"  修改文件: {len(modified)}")
    print(f"  错误文件: {len(errors)}")
    print("=" * 60)

    if errors:
        print("\n⚠️  发现错误，请检查报告文件！")
        return 1

    if dry_run:
        print("\n✅ 试运行完成！")
        print("   检查报告后，使用 --execute 参数实际执行")
        print("   python scripts/rename_python.py --execute")
    else:
        print("\n✅ 重命名完成！")
        print("   请运行测试验证: pytest test/")

    return 0


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Bisheng → Terminus Python 文件重命名工具"
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='实际执行修改（默认为试运行模式）'
    )
    parser.add_argument(
        '--dir',
        type=str,
        default=None,
        help='指定要处理的目录（默认: src/backend）'
    )

    args = parser.parse_args()

    # 如果指定了目录，更新源目录
    if args.dir:
        SOURCE_DIR = Path(args.dir)

    main(dry_run=not args.execute)
