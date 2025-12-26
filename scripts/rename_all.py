#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bisheng → Terminus 一键重命名脚本

功能：
1. Python 代码重命名
2. Docker 配置重命名
3. 配置文件重命名
4. 文档更新
5. 生成完整报告
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

# ==================== 配置 ====================
PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

# 颜色输出
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text: str):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text:^60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}\n")

def print_success(text: str):
    print(f"{Colors.OKGREEN}✅ {text}{Colors.ENDC}")

def print_error(text: str):
    print(f"{Colors.FAIL}❌ {text}{Colors.ENDC}")

def print_warning(text: str):
    print(f"{Colors.WARNING}⚠️  {text}{Colors.ENDC}")

def print_info(text: str):
    print(f"{Colors.OKCYAN}ℹ️  {text}{Colors.ENDC}")

# ==================== 执行步骤 ====================

def step_1_check_prerequisites():
    """步骤 1: 检查前提条件"""
    print_header("步骤 1: 检查前提条件")

    checks = []

    # 检查是否在 Git 仓库中
    git_dir = PROJECT_ROOT / ".git"
    if git_dir.exists():
        print_success("Git 仓库检测成功")
        checks.append(True)
    else:
        print_error("不在 Git 仓库中！")
        checks.append(False)

    # 检查 scripts 目录
    if SCRIPTS_DIR.exists():
        print_success("Scripts 目录存在")
        checks.append(True)
    else:
        print_error("Scripts 目录不存在！")
        checks.append(False)

    # 检查关键脚本
    required_scripts = [
        "rename_python.py",
        "rename_docker.py",
    ]

    for script in required_scripts:
        script_path = SCRIPTS_DIR / script
        if script_path.exists():
            print_success(f"  {script} 存在")
            checks.append(True)
        else:
            print_error(f"  {script} 不存在")
            checks.append(False)

    # 检查 Git 状态
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=True
        )
        if result.stdout.strip():
            print_warning("Git 工作区有未提交的修改")
            print_info("建议先提交或 stash 修改")
        else:
            print_success("Git 工作区干净")
    except:
        print_warning("无法检查 Git 状态")

    print()

    return all(checks)


def step_2_python_rename(dry_run: bool = True):
    """步骤 2: Python 代码重命名"""
    print_header("步骤 2: Python 代码重命名")

    print_info(f"模式: {'试运行（DRY RUN）' if dry_run else '实际执行'}")

    try:
        cmd = [sys.executable, str(SCRIPTS_DIR / "rename_python.py")]
        if not dry_run:
            cmd.append("--execute")

        result = subprocess.run(
            cmd,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True
        )

        print(result.stdout)
        if result.stderr:
            print_error(result.stderr)

        return result.returncode == 0

    except Exception as e:
        print_error(f"执行失败: {e}")
        return False


def step_3_docker_rename(dry_run: bool = True):
    """步骤 3: Docker 配置重命名"""
    print_header("步骤 3: Docker 配置重命名")

    print_info(f"模式: {'试运行（DRY RUN）' if dry_run else '实际执行'}")

    try:
        cmd = [sys.executable, str(SCRIPTS_DIR / "rename_docker.py")]
        if not dry_run:
            cmd.append("--execute")

        result = subprocess.run(
            cmd,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True
        )

        print(result.stdout)
        if result.stderr:
            print_error(result.stderr)

        return result.returncode == 0

    except Exception as e:
        print_error(f"执行失败: {e}")
        return False


def step_4_manual_instructions():
    """步骤 4: 手动操作说明"""
    print_header("步骤 4: 需要手动执行的操作")

    manual_tasks = [
        {
            "title": "重命名 Python 包目录",
            "commands": [
                "cd E:\\workplace\\bisheng\\src\\backend",
                "git mv bisheng terminus",
                "git mv bisheng_langchain terminus_langchain",
                "cd ..\\..\\",
            ]
        },
        {
            "title": "重命名 Docker 配置目录",
            "commands": [
                "cd E:\\workplace\\bisheng\\docker",
                "git mv bisheng terminus",
                "cd ..",
            ]
        },
        {
            "title": "更新 README 文档",
            "commands": [
                "# 手动编辑以下文件",
                "README.md",
                "README_CN.md",
                "README_JPN.md",
                "",
                "# 搜索替换:",
                "# Bisheng → Terminus",
                "# bisheng → terminus",
            ]
        },
        {
            "title": "更新 pyproject.toml",
            "commands": [
                "# 手动编辑 src/backend/pyproject.toml",
                "",
                "# 更新依赖包名（如果有 fork 版本）:",
                "# bisheng_pyautogen → terminus_pyautogen",
                "# bisheng-ragas → terminus-ragas",
                "",
                "# 更新描述:",
                '# description = "BISHENG backend service"',
                '# →',
                '# description = "Terminus backend service"',
            ]
        },
        {
            "title": "数据库迁移（可选）",
            "commands": [
                "# 创建 Alembic 迁移脚本",
                "cd src/backend",
                "alembic revision -m 'rename_bisheng_to_terminus'",
                "",
                "# 编辑生成的迁移文件，添加表名重命名逻辑",
                "",
                "# 执行迁移",
                "alembic upgrade head",
            ]
        },
        {
            "title": "测试验证",
            "commands": [
                "# 单元测试",
                "cd src/backend",
                "pytest test/ -v",
                "",
                "# Docker 启动测试",
                "cd ..\\docker",
                "docker compose up -d",
                "",
                "# 健康检查",
                "curl http://localhost:7860/health",
            ]
        },
    ]

    for i, task in enumerate(manual_tasks, 1):
        print(f"\n{Colors.OKCYAN}{i}. {task['title']}{Colors.ENDC}")
        print(f"{'─'*60}")
        for cmd in task['commands']:
            print(f"  {cmd}")

    print()


def step_5_commit_instructions():
    """步骤 5: Git 提交说明"""
    print_header("步骤 5: Git 提交建议")

    commits = [
        {
            "stage": "阶段 1: 代码层",
            "files": "src/backend/",
            "message": "refactor: rename bisheng to terminus (code layer)"
        },
        {
            "stage": "阶段 2: 配置层",
            "files": "docker/ src/frontend/",
            "message": "refactor: rename bisheng to terminus (config layer)"
        },
        {
            "stage": "阶段 3: 文档层",
            "files": "*.md docs/",
            "message": "docs: rename bisheng to terminus (documentation)"
        },
    ]

    for commit in commits:
        print(f"\n{Colors.OKBLUE}{commit['stage']}{Colors.ENDC}")
        print(f"{'─'*60}")
        print(f"git add {commit['files']}")
        print(f"git commit -m \"{commit['message']}\"")

    print(f"\n{Colors.WARNING}提示: 检查修改后再提交！{Colors.ENDC}")
    print(f"  git diff --staged")
    print()


def generate_final_report(dry_run: bool = True):
    """生成最终报告"""
    report_file = PROJECT_ROOT / "RENAME_TERMINUS_REPORT.md"

    report_content = f"""# Bisheng → Terminus 重命名执行报告

**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**执行模式**: {'试运行（未实际修改）' if dry_run else '实际执行'}

---

## 执行摘要

- **源名称**: bisheng
- **目标名称**: terminus
- **品牌来源**: 阿西莫夫《基地》系列 - 端点星

---

## 执行状态

### ✅ 自动化步骤

| 步骤 | 状态 | 说明 |
|------|------|------|
| 前提条件检查 | ✅ | 已完成 |
| Python 代码重命名 | ✅ | 已生成报告 |
| Docker 配置重命名 | ✅ | 已生成报告 |

### ⚠️ 需要手动执行的步骤

| 步骤 | 状态 | 说明 |
|------|------|------|
| 重命名 Python 包目录 | ⬜ | 使用 `git mv` |
| 重命名 Docker 配置目录 | ⬜ | 使用 `git mv` |
| 更新 README 文档 | ⬜ | 手动编辑 |
| 更新 pyproject.toml | ⬜ | 手动编辑 |
| 数据库迁移 | ⬜ | 可选，按需执行 |
| 测试验证 | ⬜ | 运行测试套件 |
| Git 提交 | ⬜ | 分阶段提交 |

---

## 详细报告

### Python 代码重命名

详见: [`RENAME_PYTHON_REPORT.md`](./RENAME_PYTHON_REPORT.md)

### Docker 配置重命名

详见: [`RENAME_DOCKER_REPORT.md`](./RENAME_DOCKER_REPORT.md)

---

## 下一步操作

### 如果这是试运行（DRY RUN）

1. **检查报告文件**
   - `RENAME_PYTHON_REPORT.md`
   - `RENAME_DOCKER_REPORT.md`

2. **确认无误后，实际执行**
   ```bash
   # Python 代码
   python scripts/rename_python.py --execute

   # Docker 配置
   python scripts/rename_docker.py --execute
   ```

3. **执行手动操作**（见下方）

### 如果已完成自动化步骤

1. **重命名目录**
   ```bash
   # Python 包
   cd src/backend
   git mv bisheng terminus
   git mv bisheng_langchain terminus_langchain

   # Docker 配置
   cd ../../docker
   git mv bisheng terminus
   ```

2. **更新文档**
   - 编辑 `README.md`, `README_CN.md`, `README_JPN.md`
   - 搜索替换 `Bisheng` → `Terminus`

3. **更新依赖**
   - 编辑 `src/backend/pyproject.toml`
   - 更新包名和描述

4. **测试验证**
   ```bash
   cd src/backend
   pytest test/ -v
   ```

5. **Docker 测试**
   ```bash
   cd docker
   docker compose up -d
   curl http://localhost:7860/health
   ```

6. **提交修改**
   ```bash
   # 分阶段提交
   git add src/backend/
   git commit -m "refactor: rename bisheng to terminus (code layer)"

   git add docker/
   git commit -m "refactor: rename bisheng to terminus (config layer)"

   git add *.md
   git commit -m "docs: rename bisheng to terminus (documentation)"
   ```

---

## 回滚方案

如果出现问题需要回滚：

```bash
# 回滚到重命名之前
git reset --hard HEAD~1

# 或使用特定提交
git reflog
git checkout <commit-hash>

# 数据库回滚（如果执行了迁移）
cd src/backend
alembic downgrade -1
```

---

## 注意事项

⚠️ **重要提示**:

1. **不要跳过测试** - 必须运行完整的测试套件
2. **备份数据库** - 执行数据库迁移前务必备份
3. **分阶段提交** - 便于回滚和排查问题
4. **检查依赖包** - 确认 `bisheng_pyautogen` 等包的来源

---

## 联系与支持

如遇到问题：

1. 检查报告文件中的错误列表
2. 查看 Git 日志: `git log --oneline -10`
3. 运行测试定位问题: `pytest test/ -v`

---

**报告生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

    report_file.write_text(report_content, encoding='utf-8')
    print_success(f"完整报告已生成: {report_file.relative_to(PROJECT_ROOT)}")
    print()


# ==================== 主函数 ====================

def main(dry_run: bool = True):
    """主函数"""
    print(f"\n{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{'Bisheng → Terminus 重命名工具':^60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"\n{Colors.OKCYAN}品牌来源: 阿西莫夫《基地》系列 - 端点星{Colors.ENDC}")
    print(f"{Colors.OKCYAN}执行模式: {'试运行（DRY RUN）' if dry_run else '实际执行'}{Colors.ENDC}\n")

    # 执行步骤
    steps = [
        ("检查前提条件", step_1_check_prerequisites),
        ("Python 代码重命名", lambda: step_2_python_rename(dry_run)),
        ("Docker 配置重命名", lambda: step_3_docker_rename(dry_run)),
    ]

    results = []

    for step_name, step_func in steps:
        try:
            result = step_func()
            results.append((step_name, result))
        except Exception as e:
            print_error(f"{step_name} 执行出错: {e}")
            results.append((step_name, False))

    # 显示手动操作说明
    step_4_manual_instructions()
    step_5_commit_instructions()

    # 生成最终报告
    print_header("生成最终报告")
    generate_final_report(dry_run)

    # 显示摘要
    print_header("执行摘要")
    for step_name, result in results:
        status = f"{Colors.OKGREEN}✅{Colors.ENDC}" if result else f"{Colors.FAIL}❌{Colors.ENDC}"
        print(f"{status} {step_name}")

    print()

    # 提示
    if dry_run:
        print_warning("这是试运行模式，没有实际修改文件！")
        print_info("检查报告后，使用以下命令实际执行:")
        print(f"  {Colors.OKCYAN}python scripts/rename_all.py --execute{Colors.ENDC}")
    else:
        print_success("自动化步骤已完成！")
        print_info("请按照上面的说明执行手动操作")

    print()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Bisheng → Terminus 一键重命名工具"
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='实际执行修改（默认为试运行模式）'
    )

    args = parser.parse_args()

    try:
        main(dry_run=not args.execute)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}用户中断{Colors.ENDC}")
        sys.exit(1)
