#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bisheng → Terminus Docker 配置重命名脚本

功能：
1. 更新 docker-compose.yml 文件
2. 更新 Docker 容器名称
3. 更新镜像名称
4. 更新环境变量
"""

import os
import re
from pathlib import Path
from datetime import datetime

# ==================== 配置 ====================
PROJECT_ROOT = Path(__file__).parent.parent
DOCKER_DIR = PROJECT_ROOT / "docker"

# Docker 文件模式
DOCKER_FILES = [
    "docker-compose.yml",
    "docker-compose-ft.yml",
    "docker-compose-office.yml",
    "docker-compose-uns.yml",
]

# 替换规则
REPLACEMENTS = {
    # 容器名称
    'container_name: bisheng-': 'container_name: terminus-',

    # 镜像名称
    'image: dataelement/bisheng-': 'image: dataelement/terminus-',

    # 数据库名称
    'MYSQL_DATABASE: bisheng': 'MYSQL_DATABASE: terminus',

    # 环境变量前缀
    'BS_': 'TS_',  # Bisheng System → Terminus System
    'BISHENG_': 'TERMINUS_',

    # 网络名称
    'networks:\n    bisheng': 'networks:\n    terminus',

    # 卷名称
    'volumes:\n    bisheng': 'volumes:\n    terminus',
}

# ==================== 工具函数 ====================

def find_docker_files() -> list[Path]:
    """查找所有 Docker 配置文件"""
    docker_files = []

    for file_pattern in DOCKER_FILES:
        file_path = DOCKER_DIR / file_pattern
        if file_path.exists():
            docker_files.append(file_path)

    # 查找 docker/bisheng/ 目录下的配置
    bisheng_config_dir = DOCKER_DIR / "bisheng"
    if bisheng_config_dir.exists():
        for config_file in bisheng_config_dir.rglob("*.yaml"):
            docker_files.append(config_file)
        for config_file in bisheng_config_dir.rglob("*.yml"):
            docker_files.append(config_file)

    return sorted(set(docker_files))


def replace_in_docker_file(file_path: Path, replacements: dict, dry_run: bool = True) -> dict:
    """在 Docker 文件中执行替换"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content

        changes = []

        # 执行所有替换
        for pattern, replacement in replacements.items():
            if pattern in content:
                content = content.replace(pattern, replacement)
                count = original_content.count(pattern)
                changes.append({
                    'pattern': pattern,
                    'replacement': replacement,
                    'count': count
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


def rename_bisheng_directory(dry_run: bool = True) -> dict:
    """重命名 docker/bisheng/ 目录为 docker/terminus/"""
    bisheng_dir = DOCKER_DIR / "bisheng"
    terminus_dir = DOCKER_DIR / "terminus"

    if not bisheng_dir.exists():
        return {
            'status': 'skip',
            'reason': 'docker/bisheng/ 目录不存在'
        }

    if terminus_dir.exists():
        return {
            'status': 'skip',
            'reason': 'docker/terminus/ 目录已存在'
        }

    if not dry_run:
        import shutil
        shutil.copytree(bisheng_dir, terminus_dir)
        # 注意：实际应该用 git mv
        return {
            'status': 'renamed',
            'from': str(bisheng_dir),
            'to': str(terminus_dir)
        }

    return {
        'status': 'dry_run',
        'would_rename': str(bisheng_dir.relative_to(PROJECT_ROOT))
    }


def generate_report(results: list, dir_result: dict, dry_run: bool = True) -> str:
    """生成修改报告"""
    report_lines = [
        "# Docker 配置重命名报告",
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
        f"",
    ])

    # 目录重命名状态
    report_lines.extend([
        f"## 目录重命名",
        f"状态: {dir_result.get('status', 'N/A')}",
    ])
    if 'reason' in dir_result:
        report_lines.append(f"原因: {dir_result['reason']}")
    if 'from' in dir_result:
        report_lines.append(f"从: {dir_result['from']}")
        report_lines.append(f"到: {dir_result['to']}")
    report_lines.append("")

    report_lines.append(f"\n{'='*60}\n")

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

    # Git 命令提示
    if not dry_run:
        report_lines.extend([
            "## Git 操作建议",
            "",
            "```bash",
            "# 重命名目录",
            "cd docker",
            "git mv bisheng terminus",
            "cd ..",
            "",
            "# 查看修改",
            "git diff docker/",
            "",
            "# 提交",
            "git add docker/",
            "git commit -m 'refactor: rename bisheng to terminus (docker layer)'",
            "```",
            ""
        ])

    return '\n'.join(report_lines)


# ==================== 主函数 ====================

def main(dry_run: bool = True):
    """主函数"""
    print("=" * 60)
    print("Bisheng → Terminus Docker 配置重命名工具")
    print("=" * 60)
    print(f"\n项目根目录: {PROJECT_ROOT}")
    print(f"Docker 目录: {DOCKER_DIR}")
    print(f"模式: {'试运行（DRY RUN）' if dry_run else '实际执行'}\n")

    # 查找 Docker 文件
    print("正在扫描 Docker 配置文件...")
    docker_files = find_docker_files()
    print(f"找到 {len(docker_files)} 个配置文件\n")

    if not docker_files:
        print("⚠️  未找到任何 Docker 配置文件！")
        return 1

    # 显示文件列表
    print("配置文件列表:")
    for f in docker_files:
        print(f"  - {f.relative_to(PROJECT_ROOT)}")
    print()

    # 处理目录重命名
    print("检查目录重命名...")
    dir_result = rename_bisheng_directory(dry_run)
    print(f"  状态: {dir_result.get('status', 'N/A')}\n")

    # 执行替换
    print("正在执行替换...")
    results = []
    for file_path in docker_files:
        result = replace_in_docker_file(file_path, REPLACEMENTS, dry_run)
        if result:
            results.append(result)

    print(f"\n完成！处理了 {len(results)} 个文件\n")

    # 生成报告
    report = generate_report(results, dir_result, dry_run)
    report_file = PROJECT_ROOT / "RENAME_DOCKER_REPORT.md"

    report_file.write_text(report, encoding='utf-8')
    print(f"报告已生成: {report_file}\n")

    # 显示摘要
    modified = [r for r in results if r and r.get('status') in ['modified', 'dry_run']]
    errors = [r for r in results if r and r.get('status') == 'error']

    print("=" * 60)
    print("执行摘要:")
    print(f"  扫描文件: {len(docker_files)}")
    print(f"  修改文件: {len(modified)}")
    print(f"  错误文件: {len(errors)}")
    print("=" * 60)

    if errors:
        print("\n⚠️  发现错误，请检查报告文件！")
        return 1

    if dry_run:
        print("\n✅ 试运行完成！")
        print("   检查报告后，使用 --execute 参数实际执行")
        print("   python scripts/rename_docker.py --execute")

        # 提示手动操作
        if dir_result.get('status') == 'dry_run':
            print("\n⚠️  注意：目录重命名需要手动执行")
            print("   cd docker && git mv bisheng terminus && cd ..")
    else:
        print("\n✅ Docker 配置重命名完成！")
        print("   请使用 Git 查看并提交修改")

    return 0


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Bisheng → Terminus Docker 配置重命名工具"
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='实际执行修改（默认为试运行模式）'
    )

    args = parser.parse_args()

    main(dry_run=not args.execute)
