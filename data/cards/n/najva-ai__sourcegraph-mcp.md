# najva-ai/sourcegraph-mcp

⭐ 42 · Python · MIT · 推送 2025-11-25 · [GitHub](https://github.com/najva-ai/sourcegraph-mcp) · 组织维护

**为 AI 助手提供 Sourcegraph 代码搜索能力的 MCP 服务器**

基于 Model Context Protocol 的服务器，将 Sourcegraph 代码搜索平台接入 AI 助手：提供 search（正则/语言过滤/布尔运算符的高级查询）、search_prompt_guide（按目标生成查询构造指南）、fetch_content（浏览仓库文件与目录）三个 MCP 工具，并支持按名称发现仓库。面向需要在大型代码库中查找和理解代码模式的 LLM 应用开发者。运行需 Sourcegraph 实例（sourcegraph.com 或自托管）与 Python 3.10+，通过环境变量配置端点与认证 token，提供 UV、pip 与 Docker 三种安装运行方式。

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

- 三个 MCP 工具：search / search_prompt_guide / fetch_content
- 支持正则、文件/语言过滤与布尔运算符的查询语法
- 支持 SSE 与 Streamable HTTP 两种服务端口
- 可对接私有 Sourcegraph 实例（token 认证）

## 适用场景

- 让 Cursor 等 AI 编码工具跨仓库检索代码
- 为 LLM agent 提供按目标构造搜索查询的引导
- 通过 AI 助手浏览仓库文件结构与内容

## 场景标签

 · 领域:开发工具/代码搜索

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that provides AI-enhanced code search capabilities using Sourcegraph.
> L9: This MCP server integrates with Sourcegraph, a universal code search platform that enables searching across multiple
> L82: This server provides three powerful tools for AI assistants:

## 星数曲线

```mermaid
xychart-beta
    title "najva-ai/sourcegraph-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-29 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e637fdede37a` · [字段定义](../../DATASET.md)*
