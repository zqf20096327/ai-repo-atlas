# phcp-tech/toolmaker-agent

⭐ 92 · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/phcp-tech/toolmaker-agent) · [官网](https://toolmaker.io) · 组织维护 · 中文 README

**人类与 AI agent 协作的 SDLC 结构化数据平台**

单文件自包含可执行的软件工程工作台：以类型化的 Product/Feature/Requirement/Testcase/Defect/UML 记录（带 OID、修订、父子关系）替代散落的 Markdown 文档，内置 Go REST API、SQLite 与编译嵌入的 React 前端。提供 Web UI 表单、LLM 对话 agent（propose-confirm 工具调用流）与官方 SDK 实现的 MCP 服务器（48 个工具，Streamable HTTP）三种操作入口；支持 4+1 视图 Mermaid 图（7 种图型，可导出 PNG/SVG）与可选的 RAG 语义搜索（按实体异步嵌入）。LLM 提供商可插拔，含 OpenAI/Anthropic/Gemini/DeepSeek/Ollama 等，也可通过 OpenAI 兼容自定义端点接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Product/Feature/Requirement/Testcase/Defect/UML 六类实体的类型化 CRUD，带 OID、修订与乐观并发
- LLM 对话 agent 的 propose→confirm 写入流程，模型不确认不落库
- MCP 服务器暴露 48 个工具，Claude Code/Codex/DeepSeek Harness 可直接读写同一数据
- 七个平台/架构的预编译自包含二进制，无安装器、无外部数据库依赖

## 适用场景

- 把规格、需求、设计文档从散落 Markdown 收拢为可查询的结构化记录
- 通过自然语言对话创建和维护需求与 UML 图
- 让 Claude Code/Codex 等编码 agent 在终端直接管理工程数据
- 用语义搜索按含义查找跨产品的实体

## 场景标签

`语义搜索` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L11: Toolmaker Agent is an Agentic AI SDLC platform — humans and agents collaborate on the same structured data model.
> L135: Plain forms and detail panels: click "+ Create", type into a field, hit save. No AI in the loop at all — the basel

## 星数曲线

```mermaid
xychart-beta
    title "phcp-tech/toolmaker-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 90 --> 93
    line [91, 92, 92]
```

2026-10-18 91 → 2026-10-29 92（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `213bdd99bf42` · [字段定义](../../DATASET.md)*
