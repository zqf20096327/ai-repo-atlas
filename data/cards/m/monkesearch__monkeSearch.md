# monkesearch/monkeSearch

⭐ 203 · Python · Apache-2.0 · 推送 2026-06-19 · [GitHub](https://github.com/monkesearch/monkeSearch) · 个人维护

**本地离线的自然语言文件搜索：为 AI 代理桥接 macOS Spotlight**

面向 macOS（依赖 Spotlight）的原型工具：用小型本地 LLM（如 LFM 2.5 1.2B）将自然语言查询解析为原生 Spotlight 搜索谓词，拆解为文件类型、时间语境与关键词三部分后返回文件路径。全离线、无需 GPU、不修改文件或维护索引，定位为 AI agent 与 LLM 编排管线的只读文件发现层。需运行 llama.cpp 的 llama-server 或任意 OpenAI 兼容端点，另有基于向量数据库（LEANN/ChromaDB）的跨平台分支。限制：仅元数据检索、仅简单时间表达、小模型可能误解复杂查询。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 小型本地 LLM 将自然语言解析为原生 Spotlight NSPredicate
- 完全离线、无需 GPU、只读不修改文件或维护索引
- 支持任意 OpenAI 兼容端点（MONKE_SERVER_URL 可配置）
- vectordb 分支提供基于 LEANN/ChromaDB 嵌入的跨平台方案

## 适用场景

- 在 Mac 上用自然语言按时间和类型查找本地文件
- 作为 AI agent 的文件发现工具，让 agent 自主定位文件
- 无 GPU 的机器上离线做语义化文件搜索

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L9: **Perfect for agentic use:** monkeSearch provides a direct LLM-to-filesystem bridge — natural language in, native Sp
> L18: monkeSearch uses a small local LLM (like LFM 1.2B) to parse queries and convert them into native macOS Spotlight se

## 星数曲线

```mermaid
xychart-beta
    title "monkesearch/monkeSearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 202 --> 204
    line [203, 203]
```

2026-10-18 203 → 2026-10-23 203（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ca8bbd651581` · [字段定义](../../DATASET.md)*
