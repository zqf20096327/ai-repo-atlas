# tanaikech/FileSearchStore-extension

⭐ 15 · JavaScript · MIT · 推送 2025-12-28 · [GitHub](https://github.com/tanaikech/FileSearchStore-extension) · [官网](https://medium.com/google-cloud/integrating-file-search-with-the-gemini-cli-extension-0d9e04ecde7d) · 个人维护

**Gemini CLI 扩展：在终端管理 File Search 存储并做 RAG 生成**

由 Tanaike 开发的 Node.js Gemini CLI 扩展，封装 Gemini API 的 File Search 功能，在命令行提供 11 个 MCP 工具，用于创建、列出、删除 File Search 存储与文档，支持从 URL 或本地文件上传数据，并调用 generate_content 基于私有文档生成检索增强内容。前置条件为已安装 Gemini CLI 并配置 GEMINI_API_KEY；模型默认 gemini-1.5-flash，可选 gemini-1.5-pro，通过 GEMINI_MODEL 环境变量切换。安装仅需一条 gemini extensions install 命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个 MCP 工具管理 File Search 存储与文档
- 支持从 URL、本地路径或引用文件上传数据
- 命令行内完成从数据摄取到接地内容生成的工作流
- 单条命令安装（gemini extensions install）

## 适用场景

- 在 Gemini CLI 中搭建基于私有文档的 RAG 问答
- 通过自然语言管理 File Search 存储与上传文档
- 终端内完成数据摄取到接地生成的完整流程

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L7: This repository introduces a new Gemini CLI extension that integrates File Search feature. This tool establishes a f

## 星数曲线

```mermaid
xychart-beta
    title "tanaikech/FileSearchStore-extension 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `471afa458031` · [字段定义](../../DATASET.md)*
