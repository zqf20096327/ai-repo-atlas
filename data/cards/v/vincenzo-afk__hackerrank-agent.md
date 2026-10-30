# vincenzo-afk/hackerrank-agent

⭐ 37 · Python · 推送 2026-08-23 · [GitHub](https://github.com/vincenzo-afk/hackerrank-agent) · 个人维护

**终端版多领域客服工单分流 agent，基于本地文档库生成回答**

为 HackerRank 挑战赛开发的命令行工单处理工具：对 HackerRank、Claude、Visa 三个领域的客服工单进行分类，从 data/ 本地语料中做混合检索（Sentence Transformers 语义相似度 + 关键词评分 + 公司域加权），经 Groq API（默认 llama-3.3-70b-versatile）生成有据回答；对提示注入、破坏性命令、敏感 PII、欺诈等高风险请求按规则升级人工而非作答。提供批量 CSV 与交互式 REPL 两种模式，通过环境变量配置模型与检索参数。限制：分类为启发式、语料外请求一律升级、首次建嵌入索引较慢、仓库内无测试套件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合检索：语义相似度 + 关键词评分 + 公司域加权
- 规则式安全升级：提示注入、PII、欺诈、分数操纵等 10 类场景
- 批量 CSV 与交互式 REPL 双模式，回答附源文件依据
- 嵌入缓存本地复用，配置全部经环境变量

## 适用场景

- 客服团队批量分流传入的工单 CSV
- 客服坐席在终端 REPL 中带公司上下文提问
- 需要可溯源回答来源文件的内部支持场景

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L28: **HackerRank Orchestrate** processes support tickets for three domains—HackerRank, Claude, and Visa—using only the 
> L34: - **Hybrid retrieval:** combines Sentence Transformers semantic similarity with a lightweight keyword score and an 
> L57: |LLM integration|`groq>=0.9.0`; default model `llama-3.3-70b-versatile`|

## 星数曲线

```mermaid
xychart-beta
    title "vincenzo-afk/hackerrank-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `119ade5876f2` · [字段定义](../../DATASET.md)*
