# 🎭 BMad 完整使用指南

> 版本: 1.0
> 生成时间: 2025-12-26
> 项目: Bisheng

---

## 📚 目录

1. [系统概述](#系统概述)
2. [专家代理详细能力](#专家代理详细能力)
3. [任务系统](#任务系统)
4. [模板系统](#模板系统)
5. [检查清单系统](#检查清单系统)
6. [典型使用场景](#典型使用场景)
7. [快速上手指南](#快速上手指南)
8. [命令速查表](#命令速查表)
9. [项目文档结构](#项目文档结构)

---

## 系统概述

### BMad 是什么？

**BMad (BMad Method)** 是一套完整的 AI 驱动软件开发方法论，通过 8 位专业代理协同工作，实现从想法到实现的完整开发流程。

### 核心特性

- ✅ **8 位专业代理** - 涵盖产品、架构、开发、QA、UX、分析等全流程
- ✅ **23 个可执行任务** - 标准化的工作流程
- ✅ **13 个专业模板** - 确保文档一致性
- ✅ **6 个质量检查清单** - 保证交付质量
- ✅ **统一的命令系统** - 所有命令以 `*` 开头
- ✅ **灵活的代理切换** - 随时转换到合适的专家
- ✅ **交互式协作** - 编号选项、清晰引导

### 基本规则

⚠️ **重要：所有命令都必须以 `*` 开头**

```bash
*help              # 显示帮助
*agent [name]      # 转换为代理
*task [name]       # 运行任务
*exit              # 退出当前代理
```

---

## 专家代理详细能力

### 🏃 Bob - Scrum Master (ID: `sm`)

**核心职责：敏捷流程与故事准备**

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `*draft` | 创建详细的用户故事 | 开发前准备具体任务 |
| `*correct-course` | 纠偏与流程调整 | 项目偏离轨道时 |
| `*story-checklist` | 执行故事草稿检查清单 | 验证故事完整性 |

**工作示例：**
```
用户: "我需要为登录功能创建一个用户故事"
→ *agent sm → *draft
→ Bob 会引导您完成故事创建，包括：
   - 验收标准
   - 技术任务分解
   - 测试要求
   - 开发者备注
```

**转换命令：** `*agent sm` 或 `*agent bob`

---

### 🎨 Sally - UX Expert (ID: `ux-expert`)

**核心职责：用户体验与界面设计**

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `*create-front-end-spec` | 创建前端规范文档 | 设计前端组件/页面 |
| `*generate-ui-prompt` | 生成 AI UI 提示词 | 使用 v0/Lovable 等 AI 工具 |

**工作示例：**
```
用户: "我需要设计一个用户设置页面"
→ *agent ux-expert → *create-front-end-spec
→ Sally 会创建包含以下内容的规范：
   - 用户流程图
   - 交互设计
   - 视觉设计规范
   - 可访问性要求
   - AI UI 生成提示词
```

**转换命令：** `*agent ux-expert` 或 `*agent sally`

---

### 🧪 Quinn - QA Test Architect (ID: `qa`)

**核心职责：质量保证与测试策略**

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `*review {story}` | 全面审查故事 | 代码审查前的质量检查 |
| `*gate {story}` | 质量门控决策 | 决定是否可以合并代码 |
| `*test-design {story}` | 设计测试场景 | 创建全面的测试计划 |
| `*trace {story}` | 需求可追溯性 | 验证所有需求都有测试 |
| `*risk-profile {story}` | 风险评估矩阵 | 识别和量化风险 |
| `*nfr-assess {story}` | 非功能需求评估 | 验证性能/安全性等 |

**工作示例：**
```
用户: "审查支付功能的故事"
→ *agent qa → *review payment-feature
→ Quinn 会提供：
   - PASS/CONCERNS/FAIL/WAIVED 决策
   - 测试覆盖分析
   - 风险评估
   - 改进建议
```

**转换命令：** `*agent qa` 或 `*agent quinn`

---

### 📋 John - Product Manager (ID: `pm`)

**核心职责：产品战略与文档**

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `*create-prd` | 创建 PRD 文档 | 新功能/产品规划 |
| `*create-brownfield-prd` | 为现有项目创建 PRD | 文档化现有系统 |
| `*create-epic` | 创建史诗 | 大型功能规划 |
| `*shard-prd` | 拆分 PRD 文档 | 管理大型 PRD |
| `*correct-course` | 产品战略调整 | 方向修正 |

**工作示例：**
```
用户: "我需要为新的推荐系统创建 PRD"
→ *agent pm → *create-prd
→ John 会引导您完成：
   - 问题陈述
   - 目标用户
   - 功能需求
   - 成功指标
   - 竞品分析
```

**转换命令：** `*agent pm` 或 `*agent john`

---

### 📝 Sarah - Product Owner (ID: `po`)

**核心职责：待办管理与需求细化**

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `*create-story` | 创建用户故事 | 从需求到可执行故事 |
| `*validate-story-draft` | 验证故事草稿 | 质量把关 |
| `*shard-doc` | 拆分文档 | 管理大型文档 |
| `*execute-checklist-po` | 执行 PO 检查清单 | 验证工作完整性 |

**工作示例：**
```
用户: "验证这个故事草稿"
→ *agent po → *validate-story-draft story-123
→ Sarah 会检查：
   - 需求完整性
   - 验收标准清晰度
   - 技术任务可执行性
   - 与 PRD/架构的一致性
```

**转换命令：** `*agent po` 或 `*agent sarah`

---

### 💻 James - Full Stack Developer (ID: `dev`)

**核心职责：代码实现与开发**

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `*develop-story` | 实现用户故事 | 核心开发流程 |
| `*run-tests` | 运行测试 | 验证代码质量 |
| `*review-qa` | 应用 QA 修复 | 修复 QA 发现的问题 |
| `*explain` | 解释实现细节 | 学习和代码审查 |

**工作示例：**
```
用户: "实现登录故事"
→ *agent dev → *develop-story
→ James 会：
   1. 读取故事中的所有任务
   2. 按顺序实现每个任务
   3. 编写测试
   4. 运行验证
   5. 更新故事文件
   6. 完成后设置状态为 "Ready for Review"
```

**转换命令：** `*agent dev` 或 `*agent james`

---

### 📊 Mary - Business Analyst (ID: `analyst`)

**核心职责：市场研究与战略分析**

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `*brainstorm {topic}` | 结构化头脑风暴 | 创意生成 |
| `*create-project-brief` | 创建项目简介 | 新项目启动 |
| `*create-competitor-analysis` | 竞品分析 | 市场研究 |
| `*perform-market-research` | 市场研究 | 深度市场分析 |
| `*elicit` | 高级需求启发 | 深度需求挖掘 |
| `*research-prompt {topic}` | 创建研究提示词 | 深度研究 |

**工作示例：**
```
用户: "为新的 AI 功能进行头脑风暴"
→ *agent analyst → *brainstorm AI features
→ Mary 会引导您：
   - 使用多种头脑风暴技术
   - 生成广泛的想法
   - 组织和分类想法
   - 识别最有前景的方向
```

**转换命令：** `*agent analyst` 或 `*agent mary`

---

### 🏗️ Winston - Architect (ID: `architect`)

**核心职责：系统设计与技术架构**

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `*create-full-stack-architecture` | 全栈架构文档 | 完整系统设计 |
| `*create-backend-architecture` | 后端架构 | 服务端设计 |
| `*create-front-end-architecture` | 前端架构 | 客户端设计 |
| `*create-brownfield-architecture` | 现有系统架构 | 文档化现有系统 |
| `*document-project` | 文档化项目 | 自动生成项目文档 |
| `*research {topic}` | 技术研究 | 深度技术调研 |

**工作示例：**
```
用户: "设计微服务架构"
→ *agent architect → *create-full-stack-architecture
→ Winston 会创建：
   - 系统组件图
   - 数据流
   - API 设计
   - 技术栈选择
   - 部署架构
   - 安全考虑
```

**转换命令：** `*agent architect` 或 `*agent winston`

---

## 任务系统

BMad 拥有 **23 个可执行任务**，它们是具体的工作流程，不是参考材料。

### 📋 核心任务分类

#### 文档创建任务

| 任务名称 | 功能 | 使用者 |
|----------|------|--------|
| `create-doc` | 使用模板创建文档 | PM, Architect, Analyst, UX |

**工作流程：**
1. 选择合适的模板
2. 通过交互式提问收集信息
3. 生成结构化文档
4. 保存到指定位置

---

#### 故事管理任务

| 任务名称 | 功能 | 使用者 |
|----------|------|--------|
| `create-next-story` | 创建详细用户故事 | Scrum Master |
| `brownfield-create-story` | 为现有项目创建故事 | PM, PO |
| `brownfield-create-epic` | 创建史诗 | PM, PO |
| `validate-next-story` | 验证故事质量 | PO, Dev |

**故事包含：**
- 故事描述
- 验收标准
- 技术任务和子任务
- 测试要求
- 开发者备注
- QA 结果
- 开发代理记录

---

#### 质量保证任务

| 任务名称 | 功能 | 使用者 |
|----------|------|--------|
| `review-story` | 全面审查故事 | QA |
| `qa-gate` | 质量门控决策 | QA |
| `test-design` | 设计测试场景 | QA |
| `trace-requirements` | 需求可追溯性 | QA |
| `risk-profile` | 风险评估 | QA |
| `nfr-assess` | 非功能需求评估 | QA |
| `apply-qa-fixes` | 应用 QA 修复 | Dev |

**QA 审查维度：**
- 需求完整性
- 测试覆盖度
- 代码质量
- 安全性
- 性能
- 可维护性

---

#### 研究分析任务

| 任务名称 | 功能 | 使用者 |
|----------|------|--------|
| `advanced-elicitation` | 高级需求启发 | Analyst |
| `create-deep-research-prompt` | 创建研究提示词 | Analyst, Architect |
| `facilitate-brainstorming-session` | 引导头脑风暴 | Analyst |
| `document-project` | 文档化项目 | Architect |

---

#### 项目管理任务

| 任务名称 | 功能 | 使用者 |
|----------|------|--------|
| `correct-course` | 纠偏与调整 | PM, PO, SM |
| `shard-doc` | 拆分大型文档 | PM, PO, Architect |

---

#### 通用工具任务

| 任务名称 | 功能 | 使用者 |
|----------|------|--------|
| `execute-checklist` | 执行检查清单 | 所有代理 |
| `index-docs` | 索引文档 | 系统 |
| `kb-mode-interaction` | 知识库交互 | 系统 |

---

## 模板系统

BMad 提供 **13 个专业模板**，确保文档一致性和质量。

### 📄 模板分类

#### 产品文档模板

| 模板名称 | 用途 | 输出格式 |
|----------|------|----------|
| `prd-tmpl` | 产品需求文档 | 结构化 PRD |
| `brownfield-prd-tmpl` | 现有项目 PRD | 文档化现有系统 |

**PRD 模板包含：**
- 执行摘要
- 问题陈述
- 目标用户
- 功能需求
- 非功能需求
- 用户故事
- 成功指标
- 竞品分析
- 技术考虑
- 时间线

---

#### 架构文档模板

| 模板名称 | 用途 | 输出格式 |
|----------|------|----------|
| `architecture-tmpl` | 通用架构文档 | 系统架构 |
| `fullstack-architecture-tmpl` | 全栈架构 | 前后端完整架构 |
| `front-end-architecture-tmpl` | 前端架构 | 客户端架构 |
| `brownfield-architecture-tmpl` | 现有系统架构 | 文档化现有架构 |

**架构模板包含：**
- 系统概述
- 架构图
- 组件说明
- 数据流
- API 设计
- 技术栈
- 部署架构
- 安全考虑
- 扩展性考虑

---

#### 用户故事模板

| 模板名称 | 用途 | 输出格式 |
|----------|------|----------|
| `story-tmpl` | 用户故事模板 | 详细可执行故事 |

**故事模板结构：**
```yaml
Story:
  Epic: 所属史诗
  As A: 角色
  I Want: 需求
  So That: 价值

Acceptance Criteria:
  - 验收标准 1
  - 验收标准 2

Tasks:
  - [ ] 任务 1
    - [ ] 子任务 1.1
    - [ ] 子任务 1.2

Dev Notes:
  - 技术备注

Testing:
  Type: 测试类型
  Scenarios:
    - 测试场景

QA Results:
  Status: 待审查

Dev Agent Record:
  Status: Draft
```

---

#### 前端规范模板

| 模板名称 | 用途 | 输出格式 |
|----------|------|----------|
| `front-end-spec-tmpl` | 前端规范 | UI/UX 规范文档 |

**前端规范包含：**
- 组件概述
- 用户流程
- 交互设计
- 视觉设计
- 状态管理
- API 集成
- 可访问性
- 响应式设计
- AI UI 生成提示词

---

#### 质量保证模板

| 模板名称 | 用途 | 输出格式 |
|----------|------|----------|
| `qa-gate-tmpl` | 质量门控 | QA 决策文档 |

**QA 门控包含：**
- 决策 (PASS/CONCERNS/FAIL/WAIVED)
- 审查摘要
- 测试覆盖
- 风险评估
- 改进建议
- 必修复项 vs 建议项

---

#### 分析研究模板

| 模板名称 | 用途 | 输出格式 |
|----------|------|----------|
| `project-brief-tmpl` | 项目简介 | 项目概览 |
| `market-research-tmpl` | 市场研究 | 市场分析报告 |
| `competitor-analysis-tmpl` | 竞品分析 | 竞争对手分析 |
| `brainstorming-output-tmpl` | 头脑风暴输出 | 创意记录 |

---

## 检查清单系统

BMad 提供 **6 个专业检查清单**，确保工作质量。

### ✅ 检查清单列表

| 检查清单 | 用途 | 使用场景 | 使用者 |
|----------|------|----------|--------|
| `story-draft-checklist` | 故事草稿验证 | 验证故事完整性 | Scrum Master |
| `story-dod-checklist` | 故事完成定义 | 验证故事完成质量 | Developer |
| `po-master-checklist` | PO 主检查清单 | 全面质量把关 | Product Owner |
| `pm-checklist` | PM 检查清单 | 产品文档验证 | Product Manager |
| `architect-checklist` | 架构师检查清单 | 架构质量验证 | Architect |
| `change-checklist` | 变更检查清单 | 变更管理 | PM, PO |

---

### 检查清单内容示例

#### Story Draft Checklist（故事草稿检查清单）

- [ ] 故事描述清晰完整
- [ ] 验收标准可测试
- [ ] 技术任务分解合理
- [ ] 依赖关系明确
- [ ] 测试场景定义
- [ ] 开发者备注充分
- [ ] 与 PRD 一致
- [ ] 与架构一致

#### Story DoD Checklist（故事完成定义）

- [ ] 所有任务已完成
- [ ] 所有测试通过
- [ ] 代码符合规范
- [ ] 文档已更新
- [ ] Code Review 完成
- [ ] QA 审查通过
- [ ] 无已知严重问题
- [ ] 性能符合要求

---

## 典型使用场景

### 场景 1️⃣：从想法到实现的完整流程

```
第 1 步：头脑风暴（初始想法）
用户: "我想做一个 AI 聊天机器人"
→ *agent analyst → *brainstorm "AI chatbot features"
→ Mary 引导您生成功能想法

第 2 步：项目简介
→ *agent analyst → *create-project-brief
→ 创建项目概览文档

第 3 步：创建 PRD
→ *agent pm → *create-prd
→ John 引导您创建完整的产品需求文档

第 4 步：设计架构
→ *agent architect → *create-full-stack-architecture
→ Winston 设计系统架构

第 5 步：创建用户故事
→ *agent sm → *draft
→ Bob 创建详细的用户故事

第 6 步：质量审查
→ *agent qa → *review {story}
→ Quinn 审查故事质量

第 7 步：实现功能
→ *agent dev → *develop-story
→ James 实现代码

第 8 步：质量门控
→ *agent qa → *gate {story}
→ Quinn 做出最终质量决策
```

---

### 场景 2️⃣：现有项目功能开发

```
用户: "在现有系统中添加支付功能"

第 1 步：创建故事
→ *agent po → *create-story
→ Sarah 创建用户故事

第 2 步：架构更新
→ *agent architect → *create-brownfield-architecture
→ Winston 更新架构文档

第 3 步：前端规范
→ *agent ux-expert → *create-front-end-spec
→ Sally 设计前端界面规范

第 4 步：开发实现
→ *agent dev → *develop-story
→ James 实现功能

第 5 步：QA 审查
→ *agent qa → *review {story}
→ Quinn 全面审查

第 6 步：修复问题
→ *agent dev → *review-qa
→ James 修复 QA 发现的问题
```

---

### 场景 3️⃣：快速原型设计

```
用户: "快速设计一个用户设置界面"

→ *agent ux-expert
→ Sally: 我可以帮您创建前端规范或生成 AI UI 提示词

选项 1: *create-front-end-spec
  - 详细的 UI/UX 规范
  - 交互设计
  - 可访问性要求

选项 2: *generate-ui-prompt
  - 直接生成用于 v0/Lovable 的提示词
  - 快速创建可交互原型

选择 2: *generate-ui-prompt
→ Sally 生成优化过的提示词
→ 您复制到 v0.dev
→ 几分钟内获得可交互原型！
```

---

### 场景 4️⃣：项目质量审计

```
用户: "审查所有待开发的故事的质量"

→ *agent qa
→ Quinn: 我可以进行全面的质量审查

选项 1: *review {specific-story}
  - 单个故事的深度审查
  - 包含所有质量维度

选项 2: *test-design {story}
  - 设计全面的测试场景
  - Given-When-Then 格式

选项 3: *risk-profile {story}
  - 风险评估矩阵
  - 优先级建议

选项 4: *trace {story}
  - 需求可追溯性
  - 确保所有需求都有测试

→ 选择适合的审查类型
→ Quinn 提供详细的分析报告
```

---

### 场景 5️⃣：技术调研

```
用户: "调研微服务架构的最佳实践"

→ *agent architect
→ Winston: 我可以帮您进行深度技术调研

→ *research "microservices best practices"
→ Winston 创建深度研究提示词
→ 引导您使用研究工具
→ 生成结构化的技术调研报告

报告包含:
- 技术概述
- 关键概念
- 最佳实践
- 权衡考虑
- 实施建议
- 参考资源
```

---

## 快速上手指南

### 基础工作流程

#### 1. 确定您的需求

- **新功能/产品** → 使用 PM → Architect → Dev 流程
- **现有项目扩展** → 使用 PO → Dev 流程
- **UI/UX 设计** → 使用 UX Expert
- **质量审查** → 使用 QA
- **头脑风暴/研究** → 使用 Analyst

#### 2. 启动对应的代理

```bash
*agent [代理ID或名称]
# 例如:
*agent pm        # 转换为产品经理
*agent dev       # 转换为开发者
*agent qa        # 转换为 QA
```

#### 3. 执行具体命令

```bash
# 在代理内执行命令
*help                    # 查看该代理的所有命令
*create-prd             # 创建 PRD
*develop-story          # 开发故事
*review {story}         # 审查故事
```

#### 4. 与代理协作

- 代理会**提问**以收集必要信息
- 提供**编号选项**供您选择
- 使用**交互式检查清单**验证工作
- 支持**Yolo 模式**跳过部分确认（`*yolo`）

---

### 效率技巧

#### 直接转换

```
*agent dev           # 直接转换为开发者
*develop-story       # 立即开始开发
```

#### 使用编号选择

```
代理会显示:
1. 选项 A
2. 选项 B
3. 选项 C

您只需输入: 1 或 2 或 3
```

#### 批量操作

```
*yolo               # 启用快速模式
# 然后执行命令时跳过部分确认
```

---

## 命令速查表

### 🎯 通用命令（所有代理可用）

| 命令 | 功能 |
|------|------|
| `*help` | 显示帮助和可用命令 |
| `*status` | 显示当前状态和进度 |
| `*yolo` | 切换快速模式（跳过确认） |
| `*exit` | 退出当前代理 |
| `*agent [name]` | 转换到另一个代理 |

---

### 📋 Product Manager (John) 命令

| 命令 | 功能 |
|------|------|
| `*create-prd` | 创建产品需求文档 |
| `*create-brownfield-prd` | 为现有项目创建 PRD |
| `*create-epic` | 创建史诗 |
| `*shard-prd` | 拆分 PRD 文档 |
| `*correct-course` | 产品战略调整 |

---

### 🏗️ Architect (Winston) 命令

| 命令 | 功能 |
|------|------|
| `*create-full-stack-architecture` | 创建全栈架构 |
| `*create-backend-architecture` | 创建后端架构 |
| `*create-front-end-architecture` | 创建前端架构 |
| `*create-brownfield-architecture` | 文档化现有架构 |
| `*document-project` | 自动生成项目文档 |
| `*research {topic}` | 技术调研 |

---

### 🏃 Scrum Master (Bob) 命令

| 命令 | 功能 |
|------|------|
| `*draft` | 创建用户故事 |
| `*correct-course` | 流程纠偏 |
| `*story-checklist` | 故事检查清单 |

---

### 📝 Product Owner (Sarah) 命令

| 命令 | 功能 |
|------|------|
| `*create-story` | 创建用户故事 |
| `*create-epic` | 创建史诗 |
| `*validate-story-draft` | 验证故事草稿 |
| `*shard-doc {doc} {dest}` | 拆分文档 |
| `*execute-checklist-po` | 执行 PO 检查清单 |

---

### 💻 Developer (James) 命令

| 命令 | 功能 |
|------|------|
| `*develop-story` | 实现用户故事 |
| `*run-tests` | 运行测试 |
| `*review-qa` | 应用 QA 修复 |
| `*explain` | 解释实现细节 |

---

### 🧪 QA (Quinn) 命令

| 命令 | 功能 |
|------|------|
| `*review {story}` | 全面审查故事 |
| `*gate {story}` | 质量门控决策 |
| `*test-design {story}` | 设计测试场景 |
| `*trace {story}` | 需求可追溯性 |
| `*risk-profile {story}` | 风险评估 |
| `*nfr-assess {story}` | 非功能需求评估 |

---

### 🎨 UX Expert (Sally) 命令

| 命令 | 功能 |
|------|------|
| `*create-front-end-spec` | 创建前端规范 |
| `*generate-ui-prompt` | 生成 AI UI 提示词 |

---

### 📊 Analyst (Mary) 命令

| 命令 | 功能 |
|------|------|
| `*brainstorm {topic}` | 头脑风暴 |
| `*create-project-brief` | 创建项目简介 |
| `*create-competitor-analysis` | 竞品分析 |
| `*perform-market-research` | 市场研究 |
| `*elicit` | 高级需求启发 |
| `*research-prompt {topic}` | 创建研究提示词 |

---

## 项目文档结构

### 📁 默认文档位置

根据 `.bmad-core/core-config.yaml` 配置：

```
docs/
├── prd/                    # PRD 文档（分片存储）
│   ├── prd.md
│   └── prd-*.md           # 分片文件
├── architecture/           # 架构文档（分片存储）
│   ├── architecture.md
│   └── architecture-*.md  # 分片文件
├── stories/                # 用户故事
│   ├── epic-{n}/
│   │   └── story-{slug}.yaml
└── qa/                     # QA 文档
    └── gates/             # 质量门控
        └── {epic}.{story}-{slug}.yml
```

---

### 文档版本管理

- **PRD 版本**: v4
- **架构版本**: v4
- **分片模式**: 已启用
- **故事模式**: brownfield（现有项目）

---

## 常用快捷命令

### 🎯 按需求快速选择

| 需求 | 快捷命令 |
|------|----------|
| 我不知道从哪开始 | `*workflow-guidance` |
| 快速创建故事 | `*agent sm` → `*draft` |
| 审查代码质量 | `*agent qa` → `*review {story}` |
| 设计 UI | `*agent ux-expert` → `*generate-ui-prompt` |
| 实现功能 | `*agent dev` → `*develop-story` |
| 技术研究 | `*agent architect` → `*research {topic}` |
| 头脑风暴 | `*agent analyst` → `*brainstorm {topic}` |
| 创建 PRD | `*agent pm` → `*create-prd` |
| 设计架构 | `*agent architect` → `*create-full-stack-architecture` |

---

## 核心概念

### 🔄 BMad 工作流程

```
想法 → 分析 → 产品定义 → 架构设计 → 故事创建 → 开发实现 → 质量保证 → 部署
  ↓       ↓         ↓          ↓          ↓          ↓          ↓        ↓
Analyst  PM    Architect   Architect    SM      Dev       QA      Ops
```

---

### 📊 代理协作模式

1. **独立工作** - 每个代理在自己的领域内工作
2. **顺序协作** - 按工作流程依次接力
3. **交叉验证** - QA 验证所有阶段的工作
4. **反馈循环** - 通过 `*correct-course` 进行调整

---

### 🎯 质量保证三道防线

1. **自我检查** - 代理使用检查清单验证工作
2. **交叉审查** - PO/PO 验证文档和故事
3. **专业审查** - QA 进行全面质量审查

---

## 最佳实践

### ✅ 推荐做法

1. **从 PM 开始** - 新功能从 PRD 开始
2. **先架构后开发** - 确保技术方案正确
3. **故事要详细** - 详细的减少返工
4. **QA 必不可少** - 质量门控保证质量
5. **文档同步更新** - 保持文档与代码同步

---

### ❌ 避免的做法

1. **跳过 PRD** - 直接开发容易迷失方向
2. **忽略架构** - 技术债会累积
3. **故事不完整** - 导致频繁返工
4. **跳过 QA** - 质量问题会堆积
5. **文档过时** - 降低团队效率

---

## 故障排查

### ❓ 常见问题

**Q: 我应该从哪个代理开始？**

A: 根据您的需求：
- 新功能 → `*agent pm`
- 现有功能 → `*agent po`
- UI 设计 → `*agent ux-expert`
- 代码问题 → `*agent dev`
- 质量问题 → `*agent qa`

---

**Q: 如何知道当前在哪个代理？**

A: 使用 `*status` 命令查看当前状态

---

**Q: 如何切换代理？**

A: 直接使用 `*agent [name]` 命令

---

**Q: 如何退出当前代理？**

A: 使用 `*exit` 命令返回 Orchestrator

---

**Q: Yolo 模式是什么？**

A: 快速模式，跳过部分确认，提高效率。使用 `*yolo` 切换

---

**Q: 故事文件格式是什么？**

A: YAML 格式，包含故事描述、验收标准、任务、测试等

---

**Q: 如何使用生成的文档？**

A: 文档保存在 `docs/` 目录，可以使用任何编辑器查看

---

## 附录

### 📖 相关资源

- **BMad 核心配置**: `.bmad-core/core-config.yaml`
- **代理定义**: `.bmad-core/agents/*.md`
- **任务定义**: `.bmad-core/tasks/*.md`
- **模板文件**: `.bmad-core/templates/*.yaml`
- **检查清单**: `.bmad-core/checklists/*.md`

---

### 🔧 技术支持

如果您遇到问题或需要帮助：

1. 使用 `*help` 查看帮助
2. 使用 `*status` 查看当前状态
3. 使用 `*workflow-guidance` 获取工作流建议
4. 使用 `*kb-mode` 加载完整知识库

---

## 更新日志

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 1.0 | 2025-12-26 | 初始版本，完整功能文档 |

---

**文档结束**

> 💡 提示：将此文档保存到项目根目录，方便随时查阅！
