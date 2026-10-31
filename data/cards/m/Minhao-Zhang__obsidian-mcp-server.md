# Minhao-Zhang/obsidian-mcp-server

⭐ 14 · TypeScript · AGPL-3.0 · 推送 2026-08-17 · [GitHub](https://github.com/Minhao-Zhang/obsidian-mcp-server) · 个人维护 · 中文 README

**Obsidian 插件：本地运行 MCP 服务器，向 AI 助手开放笔记库语义搜索与文件操作**

在 Obsidian 内启动基于 SSE 的本地 MCP 服务器，供 AI 助手、脚本等外部应用通过标准化接口访问笔记库。将 Markdown 笔记索引进 Orama 向量数据库，使用可配置的 OpenAI 兼容嵌入模型（含本地 Ollama 端点）生成向量，支持分块参数与 .gitignore 语法的排除规则。提供 10 个 MCP 工具，覆盖语义搜索、读写编辑文件与文件夹管理。自述为进行中项目，安全未经审查，索引会将笔记内容发送至所配置的嵌入端点；orama.json 超过 512MB 时索引可能失败。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SSE 本地 MCP 服务器，端口可配置、可自动启动
- 笔记内容索引进 Orama 向量库，嵌入模型可配置（OpenAI 兼容端点，含本地 Ollama）
- 10 个 MCP 工具：语义搜索、文件/文件夹读写与增删
- 支持中英文界面、逐工具启用/禁用开关

## 适用场景

- 让 MCP 客户端（如 AI 助手）检索和操作我的 Obsidian 笔记库
- 通过语义搜索在笔记库中查找相关内容
- 让外部脚本按标准化接口读写笔记文件

## 场景标签

`知识库管理` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5: This Obsidian plugin runs a local MCP (Model Context Protocol) server, allowing external applications (like AI assis
> L9: - **Local MCP Server:** Runs an SSE-based MCP server on a configurable port.

## 星数曲线

```mermaid
xychart-beta
    title "Minhao-Zhang/obsidian-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `90ee71c1a89d` · [字段定义](../../DATASET.md)*
