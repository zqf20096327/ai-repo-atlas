# byerlikaya/SmartRAG

⭐ 31 · C# · MIT · 推送 2026-03-09 · [GitHub](https://github.com/byerlikaya/SmartRAG) · [官网](https://byerlikaya.github.io/SmartRAG/) · 个人维护

**.NET 多模态 RAG 库：自然语言查询数据库、文档、图像与音频**

面向 .NET 6 的多模态 RAG 库，通过 NuGet 安装并以依赖注入接入 Web API 应用：单条自然语言查询可跨 SQL Server/MySQL/PostgreSQL/SQLite 多库联合检索，同时支持 PDF、Word、Excel、图像 OCR、语音转文本等文档处理。AI 层支持 OpenAI、Anthropic、Gemini、Azure OpenAI、Ollama（本地）与 LM Studio；向量存储支持 Qdrant、Redis、InMemory 等。内置浏览器 Dashboard 用于文档管理与对话，提供 MCP 客户端集成、文件夹监听自动索引与 docker-compose 示例环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨多数据库的自然语言联合查询与自动模式检测
- 多模态文档处理：PDF/Word/Excel/图像OCR/语音转文本
- 内置浏览器 Dashboard（文档管理+对话），默认仅开发环境启用
- MCP 客户端集成与文件夹监听自动索引

## 适用场景

- 在 .NET 应用中用自然语言查询多个业务数据库
- 对企业文档（PDF/表格/图像/音频）做统一检索问答
- 本地化部署满足 GDPR/KVKK/HIPAA 合规的数据问答

## 场景标签

`RAG` `多模态` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L20: dotnet add package SmartRAG
> L165: - **Native multi-database RAG capabilities** for .NET
> L252: **🤖 AI Models:** OpenAI, Anthropic, Gemini, Azure OpenAI, Ollama (local), LM Studio

## 星数曲线

```mermaid
xychart-beta
    title "byerlikaya/SmartRAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `d908198a80d8` · [字段定义](../../DATASET.md)*
