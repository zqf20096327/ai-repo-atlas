# docdyhr/simplenote-mcp-server

⭐ 21 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/docdyhr/simplenote-mcp-server) · 个人维护

**让 Claude Desktop 读写 Simplenote 笔记的 MCP 服务器**

基于 MCP Python SDK 实现的 Simplenote 集成服务器，使 Claude Desktop 等 MCP 客户端可将 Simplenote 笔记作为记忆后端或内容源。提供 20 余个工具：笔记增删改查、软删除与回收站、全文搜索（布尔运算、标签与日期过滤）、版本回滚、按标题原子创建、追加日记、导出 Markdown/JSON、查重合并、发布笔记到公开 URL 等。支持可选客户端 AES-256-GCM 加密、内存缓存与后台同步。部署方式含 Docker、Smithery、pip 源码安装，并附 Helm/Kubernetes 部署方案。需要 Simplenote 账号凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20+ 笔记管理工具：增删改、标签、版本回滚、回收站操作
- 布尔运算全文搜索，含标签/日期过滤与分页
- 可选客户端 AES-256-GCM 加密；内存缓存与后台同步
- 提供 Docker 镜像与 Kubernetes Helm Chart 部署

## 适用场景

- 让 Claude Desktop 把我的 Simplenote 笔记当作记忆后端读写
- 通过 MCP 客户端对笔记做全文搜索与批量标签管理
- 把笔记导出为 Markdown/JSON 或发布到公开 URL

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: A lightweight MCP server that integrates Simplenote with Claude Desktop using the MCP Python SDK.
> L13: This allows Claude Desktop to interact with your Simplenote notes as a memory backend or content source.
> L56: - 🧩 **MCP Compatible**: Works with Claude Desktop and other MCP clients

## 星数曲线

```mermaid
xychart-beta
    title "docdyhr/simplenote-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3c30f00f21e4` · [字段定义](../../DATASET.md)*
