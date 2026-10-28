# omar-haris/smart-coding-mcp

⭐ 200 · JavaScript · MIT · 推送 2026-01-06 · [GitHub](https://github.com/omar-haris/smart-coding-mcp) · 个人维护

**给 AI 编程助手的本地语义代码搜索 MCP 服务器**

基于 Model Context Protocol 的服务器，为 Claude、Cursor、Windsurf 等 AI 编程助手提供本地语义代码搜索。它用 nomic-embed-text-v1.5（MRL，嵌入维度 64-768 可调）对代码库建索引，通过余弦相似度加精确匹配加权实现按含义检索代码；支持渐进式索引、增量更新、SQLite 缓存与 Tree-sitter AST 分块。附带包版本查询、重建索引、切换工作区等工具。全部推理在本地运行，无 API 调用、无遥测。npm 全局安装后配置到各 IDE 的 MCP 配置文件即可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 AI 嵌入（nomic-embed-text-v1.5，MRL 维度 64-768 可调）语义代码搜索
- 渐进式索引：索引过程中即可搜索；CPU 默认限 50%
- 支持 VS Code/Cursor/Windsurf/Claude Desktop/OpenCode/Raycast/Antigravity 等客户端接入
- 附加工具：20+ 生态的包最新版本查询、工作区运行时切换

## 适用场景

- 让 AI 编程助手按语义（而非关键词）查找代码库中的相关实现
- 在术语不一致或查询有拼写错误的场景下定位代码
- 在不联网、代码不出本机的约束下为 AI 助手提供代码检索

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L8: An extensible Model Context Protocol (MCP) server that provides intelligent semantic code search for AI assistants. 
> L14: This MCP server solves that by indexing your codebase with AI embeddings. Your AI assistant can search by meaning i
> L222: |**Protocol**|Model Context Protocol (JSON-RPC)|

## 星数曲线

```mermaid
xychart-beta
    title "omar-haris/smart-coding-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 199 --> 201
    line [200, 200]
```

2026-10-18 200 → 2026-10-28 200（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `b15a05e1b274` · [字段定义](../../DATASET.md)*
