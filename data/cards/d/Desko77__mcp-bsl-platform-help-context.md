# Desko77/mcp-bsl-platform-help-context

⭐ 18 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/Desko77/mcp-bsl-platform-help-context) · [官网](https://github.com/DitriXNew/mcp-bsl-platform-context) · 个人维护

**为 AI 助手提供 1С 平台 API 文档检索的 MCP 服务器**

Python 实现的 MCP 服务器（Kotlin 版 mcp-bsl-platform-context 的移植），面向使用 Claude Desktop、Cursor 等 AI 编码助手的 1С:Предприятие 开发者。从本地安装目录读取 shcntx_ru.hbk 二进制帮助文件或预导出 JSON，通过 search/info/get_member 等 MCP 工具提供 API 类型、方法、构造器查询及 BSL 严格类型化与编码规范文档。支持 keyword/semantic/hybrid 三种检索（embeddings + Qdrant + reranker），默认俄语输出。语义检索需安装 torch/sentence-transformers 或外部 OpenAI 兼容 API。

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

- keyword/semantic/hybrid 三种检索模式，hybrid 用 RRF 融合 + cross-encoder 重排
- 直接读取 1С 平台 shcntx_ru.hbk 帮助文件，支持多版本自动发现
- 提供 STDIO/SSE/Streamable HTTP 三种传输方式
- 内置 BSL 严格类型化与编码规范文档查询工具

## 适用场景

- 在 Claude Desktop 或 Cursor 中查询 1С 平台 API 用法
- 让 AI 助手遵循 BSL 编码规范与严格类型化文档写代码
- 按自然语言描述定位 1С API 方法（语义检索）

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: **MCP-сервер для доступа к документации API платформы 1С:Предприятие**
> L20: - **Три транспорта**: STDIO (для Claude Desktop, Cursor), SSE и Streamable HTTP

## 星数曲线

```mermaid
xychart-beta
    title "Desko77/mcp-bsl-platform-help-context 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `ba6595852396` · [字段定义](../../DATASET.md)*
