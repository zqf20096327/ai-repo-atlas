# Consensus-NLP/consensus-api

⭐ 18 · MIT · 推送 2026-08-21 · [GitHub](https://github.com/Consensus-NLP/consensus-api) · [官网](https://docs.consensus.app/reference/v1_search) · 组织维护

**Consensus 学术搜索的 REST API：检索 2.2 亿+ 篇同行评审论文**

Consensus 官方 API 仓库，提供对 2.2 亿+ 篇同行评审论文语料库的单端点搜索：一次调用返回按相关性排序的论文，附带引用数、研究元数据（研究类型、样本量、人群类型等）、期刊质量信号（SJR 分位）与全文摘录。支持按年份、研究设计、方法学严谨性、医学模式等过滤。自助获取 API key，付费计划含 API 用量；另提供 MCP 服务器供 Claude、ChatGPT、Cursor 等 AI 助手远程调用。旧端点 /v1/quick_search 已声明废弃，2027-02-07 移除。

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

- 220M+ 同行评审论文语料的相关性排序搜索
- 结果含引用数、研究元数据、SJR 期刊质量信号与通俗要点
- 可选语义相关性评分与全文摘录（付费计划）
- 提供 MCP 服务器供 AI 助手客户端接入

## 适用场景

- 构建以可引用同行评审文献为依据的 LLM/RAG 应用
- 文献发现与系统性综述工具开发
- 为临床与政策团队构建证据面板

## 场景标签

`语义搜索` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L10: The Consensus API is a REST API for searching academic literature: one call returns relevance-ranked, peer-reviewed
> L87: - LLM and RAG applications grounded in citable, peer-reviewed sources
> L94: Looking to use Consensus inside an AI assistant instead of your own code? The Consensus MCP server gives Claude, Ch

## 星数曲线

```mermaid
xychart-beta
    title "Consensus-NLP/consensus-api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f3cb4a1efe26` · [字段定义](../../DATASET.md)*
