# Docker 配置重命名报告

生成时间: 2025-12-26 18:22:30
模式: 实际执行

============================================================

## 统计摘要
- 扫描文件数: 5
- 修改文件数: 5
- 错误文件数: 0

## 目录重命名
状态: renamed
从: E:\workplace\bisheng\docker\bisheng
到: E:\workplace\bisheng\docker\terminus


============================================================

## 修改详情

### docker\bisheng\config\config.yaml
状态: modified
  - `BS_` → `TS_` (11 处)

### docker\docker-compose-ft.yml
状态: modified
  - `container_name: bisheng-` → `container_name: terminus-` (1 处)
  - `image: dataelement/bisheng-` → `image: dataelement/terminus-` (1 处)

### docker\docker-compose-office.yml
状态: modified
  - `container_name: bisheng-` → `container_name: terminus-` (1 处)

### docker\docker-compose-uns.yml
状态: modified
  - `container_name: bisheng-` → `container_name: terminus-` (1 处)
  - `image: dataelement/bisheng-` → `image: dataelement/terminus-` (1 处)

### docker\docker-compose.yml
状态: modified
  - `container_name: bisheng-` → `container_name: terminus-` (9 处)
  - `image: dataelement/bisheng-` → `image: dataelement/terminus-` (3 处)
  - `MYSQL_DATABASE: bisheng` → `MYSQL_DATABASE: terminus` (1 处)
  - `BS_` → `TS_` (22 处)

## Git 操作建议

```bash
# 重命名目录
cd docker
git mv bisheng terminus
cd ..

# 查看修改
git diff docker/

# 提交
git add docker/
git commit -m 'refactor: rename bisheng to terminus (docker layer)'
```
