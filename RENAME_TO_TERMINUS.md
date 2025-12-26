# 🚀 Bisheng → Terminus 重命名执行计划

> **项目重命名方案 B - 快速流程**
> 创建时间: 2025-12-26
> 预计完成时间: 3-5 天

---

## 📊 执行概览

### 重命名目标
- **源名称**: `bisheng`
- **目标名称**: `terminus`
- **品牌来源**: 阿西莫夫《基地》系列 - 端点星

### 影响范围
| 类型 | 数量 | 风险等级 |
|------|------|----------|
| Python 文件 | ~400 | 🟡 中 |
| 配置文件 | ~50 | 🟢 低 |
| Docker 配置 | 20+ | 🟢 低 |
| 文档 | ~20 | 🟢 低 |
| 数据库 | 1 | 🟠 中高 |
| **总计** | **638 文件** | **🟡 中** |

---

## 🎯 执行策略

### 分阶段执行

```
阶段 1: 代码层重构 (1-2 天)
  ├─ 文件夹重命名
  ├─ Python 包重命名
  └─ 导入语句更新

阶段 2: 配置层重构 (1 天)
  ├─ Docker 配置
  ├─ 环境变量
  └─ 配置文件

阶段 3: 数据库层重构 (0.5-1 天)
  ├─ 数据库迁移脚本
  ├─ 数据验证
  └─ 性能测试

阶段 4: 文档和收尾 (0.5 天)
  ├─ README 更新
  ├─ 迁移指南
  └─ 发布说明
```

---

## 📝 详细任务清单

### ✅ 阶段 1: 代码层重构

#### 任务 1.1: 文件夹重命名

**Git 操作:**
```bash
# 进入后端目录
cd E:\workplace\bisheng\src\backend

# 重命名主包目录
git mv bisheng terminus

# 重命名 LangChain 扩展包目录
git mv bisheng_langchain terminus_langchain
```

**验证:**
```bash
# 检查目录结构
ls -la | grep terminus
```

---

#### 任务 1.2: Python 文件批量替换

**替换规则:**

| 模式 | 替换为 | 说明 |
|------|--------|------|
| `import bisheng` | `import terminus` | 导入语句 |
| `from bisheng` | `from terminus` | From 导入 |
| `bisheng_langchain` | `terminus_langchain` | LangChain 扩展 |
| `class Bisheng` | `class Terminus` | 类名（可选） |
| `def bisheng_` | `def terminus_` | 函数名（可选） |

**自动化脚本 (Python):**

使用提供的 `rename_python.py` 脚本:
```bash
cd E:\workplace\bisheng
python scripts\rename_python.py
```

**手动验证:**
```bash
# 检查导入是否正确
grep -r "import bisheng" src/backend/
grep -r "from bisheng" src/backend/
# 应该返回空结果
```

---

### ✅ 阶段 2: 配置层重构

#### 任务 2.1: Docker 配置更新

**文件清单:**
- `docker/docker-compose.yml`
- `docker/docker-compose-ft.yml`
- `docker/docker-compose-office.yml`
- `docker/docker-compose-uns.yml`
- `docker/bisheng/*` → `docker/terminus/*`

**替换内容:**
```yaml
# 容器名称
container_name: bisheng-mysql → terminus-mysql
container_name: bisheng-redis → terminus-redis
container_name: bisheng-backend → terminus-backend

# 镜像名称
image: dataelement/bisheng-backend → dataelement/terminus-backend
image: dataelement/bisheng-frontend → dataelement/terminus-frontend

# 数据库名称
MYSQL_DATABASE: bisheng → terminus

# 环境变量前缀
BISHENG_* → TERMINUS_*
```

**使用脚本:**
```bash
python scripts\rename_docker.py
```

---

#### 任务 2.2: 配置文件更新

**文件类型:**
- YAML 配置文件 (`*.yaml`, `*.yml`)
- JSON 配置文件 (`*.json`)
- 环境变量文件 (`.env*`)
- Nginx 配置 (`*.conf`)

**使用脚本:**
```bash
python scripts\rename_configs.py
```

**手动检查:**
```bash
# 检查是否还有遗漏
grep -r "bisheng" docker/*.yml
grep -r "BISHENG" .
```

---

### ✅ 阶段 3: 数据库层重构

#### 任务 3.1: 创建数据库迁移脚本

**创建 Alembic 迁移:**
```bash
cd src/backend
alembic revision -m "rename_bisheng_to_terminus"
```

**迁移脚本内容:**
```python
# alembic/versions/xxx_rename_bisheng_to_terminus.py

def upgrade():
    # 重命名表（如果有 bisheng 前缀的表）
    # op.rename_table('bisheng_users', 'terminus_users')
    # op.rename_table('bisheng_flows', 'terminus_flows')
    # ... 根据实际情况添加

    # 更新数据库中的配置值
    # op.execute("""
    #     UPDATE config SET key = REPLACE(key, 'bisheng', 'terminus')
    # """)

def downgrade():
    # 回滚操作
    pass
```

---

#### 任务 3.2: 数据验证

**验证清单:**
- [ ] 数据库连接正常
- [ ] 所有表可访问
- [ ] 配置数据已更新
- [ ] API 调用正常
- [ ] 性能无退化

**验证脚本:**
```bash
# 运行测试
cd src/backend
pytest test/ -v

# 检查数据库
mysql -u root -p -e "USE terminus; SHOW TABLES;"
```

---

### ✅ 阶段 4: 文档和收尾

#### 任务 4.1: 更新文档

**文档清单:**
- [ ] `README.md` (英文)
- [ ] `README_CN.md` (中文)
- [ ] `README_JPN.md` (日文)
- [ ] `SECURITY.md`
- [ ] `CLAUDE.md` (所有层级)
- [ ] `.bmad-core/` 中的配置

**更新内容:**
- 项目名称
- 描述文本
- 链接引用
- 命令示例

---

#### 任务 4.2: 创建迁移指南

**创建 `MIGRATION_TO_TERMINUS.md`:**
```markdown
# 迁移指南

## 从 Bisheng 迁移到 Terminus

### 环境变量变更
- `BISHENG_*` → `TERMINUS_*`

### Docker 容器变更
- 容器名称: `bisheng-*` → `terminus-*`
- 镜像名称: `dataelement/bisheng-*` → `dataelement/terminus-*`

### 数据库变更
- 数据库名: `bisheng` → `terminus`
...
```

---

#### 任务 4.3: Git 提交

**分阶段提交:**
```bash
# 阶段 1: 代码层
git add src/backend/
git commit -m "refactor: rename bisheng to terminus (code layer)"

# 阶段 2: 配置层
git add docker/ src/frontend/
git commit -m "refactor: rename bisheng to terminus (config layer)"

# 阶段 3: 数据库层
git add src/backend/bisheng/core/database/
git commit -m "refactor: rename bisheng to terminus (database layer)"

# 阶段 4: 文档
git add *.md docs/
git commit -m "docs: rename bisheng to terminus (documentation)"
```

---

## 🧪 测试验证

### 单元测试
```bash
cd src/backend
pytest test/ -v --tb=short
```

### 集成测试
```bash
# 启动服务
cd docker
docker compose up -d

# 健康检查
curl http://localhost:7860/health

# API 测试
curl http://localhost:7860/api/v1/env
```

### 性能测试
```bash
# 对比重构前后的性能
# 使用 Apache Bench 或 wrk
ab -n 1000 -c 10 http://localhost:7860/api/v1/flows
```

---

## ⚠️ 风险控制

### 回滚方案

**如果出现问题:**
```bash
# 回滚到上一个工作版本
git reset --hard HEAD~1

# 或使用特定提交
git checkout <commit-hash>

# 恢复数据库
alembic downgrade -1
```

### 备份清单

**执行前备份:**
- [ ] 数据库完整备份
- [ ] Docker volumes 备份
- [ ] 配置文件备份
- [ ] 当前 Git 提交记录

---

## 📊 进度跟踪

### 执行状态

| 阶段 | 任务 | 状态 | 完成时间 |
|------|------|------|----------|
| 1 | 文件夹重命名 | ⬜ 待执行 | - |
| 1 | Python 文件替换 | ⬜ 待执行 | - |
| 2 | Docker 配置 | ⬜ 待执行 | - |
| 2 | 配置文件 | ⬜ 待执行 | - |
| 3 | 数据库迁移 | ⬜ 待执行 | - |
| 3 | 数据验证 | ⬜ 待执行 | - |
| 4 | 文档更新 | ⬜ 待执行 | - |
| 4 | 迁移指南 | ⬜ 待执行 | - |

---

## 🎯 验收标准

### 完成标准

✅ 所有 Python 导入正常
✅ 所有测试通过
✅ Docker 容器启动成功
✅ API 响应正常
✅ 数据库连接和查询正常
✅ 文档更新完整
✅ 性能无明显退化 (<5%)

### 质量门控

🚫 **阻塞**: 任何 P0 测试失败
⚠️ **关注**: 性能下降 >5%
✅ **通过**: 所有标准满足

---

## 📞 支持与问题

### 常见问题

**Q: 导入错误怎么办?**
A: 检查 `__init__.py` 文件，确保包结构正确。

**Q: Docker 无法启动?**
A: 检查容器名称冲突，使用 `docker ps -a` 查看。

**Q: 数据库连接失败?**
A: 检查 `config.yaml` 中的数据库连接字符串。

---

## 📝 变更日志

### v2.3.0-beta3-terminus (待发布)

**BREAKING CHANGES:**
- 包名从 `bisheng` 改为 `terminus`
- Docker 容器从 `bisheng-*` 改为 `terminus-*`
- 环境变量从 `BISHENG_*` 改为 `TERMINUS_*`
- 数据库名从 `bisheng` 改为 `terminus`

**迁移:**
- 参考 `MIGRATION_TO_TERMINUS.md`

---

**执行计划创建时间**: 2025-12-26
**预计完成时间**: 3-5 天
**当前状态**: 准备就绪，等待执行
