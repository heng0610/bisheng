# 🚀 Terminus 重命名快速开始指南

> **Bisheng → Terminus 项目重命名**
> 方案 B - 快速流程（3-5 天完成）

---

## ✅ 准备工作已完成

### 📁 已创建的文件

| 文件 | 说明 |
|------|------|
| `RENAME_TO_TERMINUS.md` | 详细执行计划 |
| `scripts/rename_python.py` | Python 代码重命名脚本 |
| `scripts/rename_docker.py` | Docker 配置重命名脚本 |
| `scripts/rename_all.py` | 一键执行脚本 |

---

## 🎯 三种执行方式

### 方式 1️⃣: 全自动（推荐新手）

```bash
# Step 1: 试运行（查看会修改什么）
python scripts/rename_all.py

# Step 2: 检查生成的报告
# - RENAME_TERMINUS_REPORT.md
# - RENAME_PYTHON_REPORT.md
# - RENAME_DOCKER_REPORT.md

# Step 3: 实际执行
python scripts/rename_all.py --execute

# Step 4: 执行手动操作（见报告）
# - 重命名目录
# - 更新文档
# - 测试验证
```

---

### 方式 2️⃣: 分步执行（推荐有经验者）

```bash
# 阶段 1: Python 代码
python scripts/rename_python.py              # 试运行
python scripts/rename_python.py --execute    # 实际执行
cd src/backend
git mv bisheng terminus
git mv bisheng_langchain terminus_langchain
cd ../..

# 阶段 2: Docker 配置
python scripts/rename_docker.py              # 试运行
python scripts/rename_docker.py --execute    # 实际执行
cd docker
git mv bisheng terminus
cd ..

# 阶段 3: 更新文档
# 手动编辑 README.md 等文件
# 替换: Bisheng → Terminus, bisheng → terminus

# 阶段 4: 测试
cd src/backend
pytest test/ -v

# 阶段 5: 提交
git add src/backend/
git commit -m "refactor: rename bisheng to terminus (code)"
```

---

### 方式 3️⃣: 完全手动（最安全但耗时）

详见 `RENAME_TO_TERMINUS.md` 的详细步骤。

---

## 📋 执行检查清单

### ✅ 执行前

- [ ] 已创建 feature 分支
- [ ] 已提交当前所有修改
- [ ] 已备份数据库（如果有重要数据）
- [ ] 已阅读执行计划

### ✅ 执行中

- [ ] Python 代码替换完成
- [ ] 目录重命名完成
- [ ] Docker 配置更新完成
- [ ] 文档更新完成
- [ ] pyproject.toml 更新完成

### ✅ 执行后

- [ ] 所有测试通过 (`pytest test/ -v`)
- [ ] Docker 容器启动成功
- [ ] API 健康检查通过
- [ ] 前端构建成功
- [ ] Git 分阶段提交完成

---

## ⚡ 快速命令参考

### 试运行（不修改文件）

```bash
# 完整试运行
python scripts/rename_all.py

# 仅 Python
python scripts/rename_python.py

# 仅 Docker
python scripts/rename_docker.py
```

### 实际执行

```bash
# 完整执行
python scripts/rename_all.py --execute

# 仅 Python
python scripts/rename_python.py --execute

# 仅 Docker
python scripts/rename_docker.py --execute
```

### 手动操作

```bash
# 重命名 Python 包
cd src/backend
git mv bisheng terminus
git mv bisheng_langchain terminus_langchain

# 重命名 Docker 目录
cd ../../docker
git mv bisheng terminus

# 运行测试
cd ../src/backend
pytest test/ -v

# Docker 测试
cd ../../docker
docker compose up -d
curl http://localhost:7860/health
```

---

## 🔄 回滚方案

如果出现问题：

```bash
# 回滚最后一次提交
git reset --hard HEAD~1

# 回滚到指定提交
git reflog
git checkout <commit-hash>

# 查看所有提交
git log --oneline -10
```

---

## 📊 影响范围速览

| 类型 | 数量 | 风险 |
|------|------|------|
| Python 文件 | ~400 | 🟡 中 |
| 配置文件 | ~50 | 🟢 低 |
| Docker 配置 | 20+ | 🟢 低 |
| 文档 | ~20 | 🟢 低 |
| 数据库 | 1 | 🟠 中高 |

**总计**: 638 个文件

---

## ❓ 常见问题

### Q: 脚本报错 "Module not found"？
**A**: 确保使用正确的 Python 环境：
```bash
python --version  # 应该是 3.10+
```

### Q: Git 提示 "nothing to commit"？
**A**: 可能是因为还在试运行模式，使用 `--execute` 参数。

### Q: 测试失败怎么办？
**A**:
1. 检查导入语句是否正确
2. 检查 `__init__.py` 文件
3. 查看详细错误信息: `pytest test/ -v --tb=short`

### Q: Docker 容器启动失败？
**A**:
1. 检查容器名称冲突: `docker ps -a`
2. 检查配置文件: `docker-compose.yml`
3. 查看日志: `docker compose logs backend`

---

## 🎯 验收标准

✅ **完成标准**:
- [ ] 所有 Python 导入正常
- [ ] 所有测试通过
- [ ] Docker 容器启动成功
- [ ] API 响应正常
- [ ] 文档更新完整

🚫 **阻塞问题**:
- 任何单元测试失败
- Docker 容器无法启动
- API 无法访问

---

## 📞 获取帮助

### 文档

- **执行计划**: `RENAME_TO_TERMINUS.md`
- **BMad 指南**: `.bmad-core/BMad完整使用指南.md`

### 检查日志

```bash
# Git 日志
git log --oneline -10

# 测试日志
pytest test/ -v > test_results.txt

# Docker 日志
docker compose logs > docker_logs.txt
```

---

## 🎉 开始执行

准备好了吗？选择一种方式开始：

```bash
# 推荐: 全自动试运行
python scripts/rename_all.py
```

**祝您顺利！Terminus 项目即将诞生！** 🚀

---

**创建时间**: 2025-12-26
**预计完成**: 3-5 天
**当前状态**: 准备就绪
