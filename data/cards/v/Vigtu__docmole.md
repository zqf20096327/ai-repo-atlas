# Vigtu/docmole

⭐ 18 · TypeScript · MIT · 推送 2026-04-18 · [GitHub](https://github.com/Vigtu/docmole) · [官网](https://www.npmjs.com/package/docmole) · 个人维护

**让 AI 助手查询任意文档站的 MCP 服务器**

面向 Claude、Cursor 等 MCP 兼容客户端的文档检索服务器，提供两种模式：Local RAG 模式抓取任意文档站、用 OpenAI 生成嵌入、存入 LanceDB，混合语义与关键词检索；Mintlify 模式零配置代理 Mintlify AI Assistant API，内置多个已知项目 ID。支持多轮对话上下文，内置 CLI 完成索引与启动，需 Bun 运行时，本地 RAG 模式需 OPENAI_API_KEY。Ollama 本地模式与通用 HTML 抽取列为待开发功能。

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

- Local RAG：抓取文档站→OpenAI 嵌入→LanceDB 向量库，混合检索
- Mintlify 零配置模式：代理 Mintlify AI Assistant API，免 API key
- MCP 协议原生，接入 Claude、Cursor 等 MCP 客户端
- bunx 直接运行，无需安装

## 适用场景

- 让 Claude/Cursor 等客户端直接查询项目文档
- 为团队内部文档站建立可被 AI 检索的索引
- 通过已知项目 ID 即时查询 Mintlify 托管的文档

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L14: Docmole is an MCP server that lets you query **any documentation site** from AI assistants like Claude, Cursor, or 
> L102: │ MCP Client  │────▶│   Docmole   │────▶│ Embedded: LanceDB    │
> L110: **Mintlify Mode**: Proxies requests to Mintlify's AI Assistant API. Zero setup, instant results.

## 星数曲线

```mermaid
xychart-beta
    title "Vigtu/docmole 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d3063efbb673` · [字段定义](../../DATASET.md)*
