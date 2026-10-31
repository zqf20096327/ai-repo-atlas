# xfloukiex-lab/magpie-search

⭐ 28 · Python · Apache-2.0 · 推送 2026-09-09 · [GitHub](https://github.com/xfloukiex-lab/magpie-search) · [官网](https://vektorgeist.com) · 组织维护

**本地优先的联邦搜索引擎：一次查询检索 AI 会话、文件、图谱、向量与网页**

面向 AI agent/LLM 的本地联邦搜索工具：单条查询并发分发到转录、文件、知识图谱、向量库与网页五类后端，提供 grep/关键词/语义/混合/重排五种模式，用信任加权 RRF 融合并跨源去重，结果带 fact/reference/lead/stale 信任层级并按 token 预算裁剪。核心是 SQLite 本地索引（FTS5 + sqlite-vec 向量），索引时剥离约 30 类敏感信息。通过 MCP server 暴露 search/recent/session 等只读工具，另带 deepweb 深度网页检索与转录备份功能。可选 Ollama 做会话摘要。运行于本机，Python 3.10+，pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五类后端联邦检索，信任加权 RRF 融合与跨源去重
- SQLite 本地索引：FTS5 全文 + sqlite-vec 向量（384 维本地嵌入）
- 索引时剥离约 30 类密钥/令牌等敏感信息
- 通过 MCP server 向 agent 暴露 search/recent/session 等 6 个工具

## 适用场景

- 我的 agent 会话崩溃后找回此前工作过的上下文
- 让 AI agent 通过 MCP 一次性检索本地文件、历史会话与网页
- 用 token 可控的 deepweb 命令做多角度网页检索与来源佐证
- 把 ~/.claude 转录备份到本地或远程 SSH 目标

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L84: And it exposes all of this to an AI over an **MCP server** — the tools it hands
> L42: It is a tool for an AI — an agent or an LLM.
> L198: Magpie speaks the Model Context Protocol, so any MCP-capable agent can call it.

## 星数曲线

```mermaid
xychart-beta
    title "xfloukiex-lab/magpie-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `af9f7e66a0c2` · [字段定义](../../DATASET.md)*
