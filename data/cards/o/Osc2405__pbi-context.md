# Osc2405/pbi-context

⭐ 15 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/Osc2405/pbi-context) · [官网](https://pypi.org/project/pbi-docs/) · 个人维护

**把 Power BI .pbit/.pbip 模型编译为可查询上下文供 AI agent 使用**

面向数据工程师、BI 顾问与构建 AI copilot 的团队的零依赖 Python 工具：解析 .pbit（ZIP+TMSL）与 PBIP（TMDL）文件，生成 Markdown 文档、metadata.json、面向 RAG 的 JSONL、index.json 等七类输出；提供 CLI 批处理、版本 diff 与影响分析、图导出，以及只读 MCP server 供 agent 实时查询。明确排除 TMDL 写入与 PBIR 报表层解析；Fabric 兼容性预期但未实测。纯 Python 实现，无需 .NET 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 解析 .pbit 与 PBIP/TMDL 并生成 Markdown 文档与索引化 JSON/JSONL 上下文
- 提供只读 MCP server（--mcp-serve）与查询 CLI 供 LLM agent 调用
- 内容感知的模型版本 diff 与影响分析（--diff / --diff-impact）
- 零外部依赖，纯 Python，无需 .NET

## 适用场景

- 批量为公司未文档化的 Power BI 仪表盘生成文档
- 让新分析师通过 AI agent 问答快速理解模型结构与度量
- 审计对比两个版本间度量、关系与 DAX 的变更

## 场景标签

`RAG` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L9: **pbi-context is the zero-dependency context compiler that lets any AI agent read, query, and audit
> L70: |**Let an AI agent query the model live**|Read-only MCP server (`--mcp-serve`) — validated against a test harness, 

## 星数曲线

```mermaid
xychart-beta
    title "Osc2405/pbi-context 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6926bfdd939e` · [字段定义](../../DATASET.md)*
