# najva-ai/zoekt-mcp

⭐ 23 · Python · MIT · 推送 2025-11-25 · [GitHub](https://github.com/najva-ai/zoekt-mcp) · 组织维护

**为 AI 助手提供 Zoekt 代码搜索能力的 MCP 服务器**

基于 Model Context Protocol 的服务器，将 Zoekt（Sourcegraph 使用的三元组索引代码搜索引擎）接入 AI 助手。提供三个工具：search（正则/语言过滤/布尔运算符查询索引代码库）、search_prompt_guide（生成面向目标的查询构建指南）、fetch_content（读取文件内容与目录结构）。需自行部署 Zoekt 实例并通过环境变量配置地址，支持 Python 3.10+、UV/pip 运行及 Docker 构建，可在 Cursor 等 MCP 客户端中调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 search / search_prompt_guide / fetch_content 三个 MCP 工具
- 基于 Zoekt 三元组索引，支持正则、文件/语言过滤与布尔运算符查询
- 支持 SSE 与 Streamable HTTP 两种服务端口
- 提供 UV、pip、Docker 三种运行方式

## 适用场景

- 让 Cursor 等 AI 助手在大型代码库中检索代码模式
- 通过 AI 助手浏览仓库文件与目录结构
- 为 AI 编码工具补充索引式代码搜索后端

## 场景标签

 · 领域:开发工具/LLM 基础设施

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that provides code search capabilities powered by Zoekt, the indexed code sear
> L9: This MCP server integrates with Zoekt, a text search engine optimized for code repositories. Zoekt provides trigram-
> L66: ## Usage with AI Tools

## 星数曲线

```mermaid
xychart-beta
    title "najva-ai/zoekt-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ca3fccfa3945` · [字段定义](../../DATASET.md)*
