# Aryan-Pardeshi/CiteProof-AI-MCP

⭐ 88 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Aryan-Pardeshi/CiteProof-AI-MCP) · [官网](https://citeproof.top/) · 个人维护

**系统综述审计工具集：MCP 审计服务器 + 证据落地研究应用**

两部分组成：一是无内置 LLM 的 MCP 服务器（24 个审计工具），为 Claude Science 等 agent 记录并核验系统综述流程——引文与引语是否真实出现于原文、PRISMA 计数守恒、两审稿人 Cohen's kappa、DOI 有效性与偏倚风险规则；二是多 agent 研究应用，24 个 agent 分 5 阶段经 3 个人工审批门产出全文论文，证据记录与 PRISMA 计数由代码确定性生成，导出 PDF/DOCX。限制：MCP 端不做检索与 PDF 解析，校验仅到'已解析'而非'被支持'。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 24 个 MCP 审计工具：引语核验、PRISMA 流量不变量、Cohen's kappa、DOI/撤稿查询、RoB 2/ROBINS-I/N-O 规则检查
- MCP 服务器无内置 LLM、无需 API key，存储决策并拒绝不良输入
- 研究应用 24 agent / 5 阶段 / 3 个人工审批门（LangGraph interrupt），产出带 PRISMA 流程图与证据映射的全文论文
- 证据存储与 PRISMA 计数为确定性计算，非 LLM 生成；导出 .pdf/.docx/.md

## 适用场景

- 为我的系统综述建立可导出的 PRISMA 与筛选审计轨迹
- 核验 AI 综述中引语、数字与引用是否真正来自原文
- 经人工审批门产出证据落地、引用可溯源的学术论草稿

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Audit tools for AI literature reviews.** CiteProof checks that a review's citations, quotes, counts and risk-of-bi
> L29: CiteProof MCP keeps the records a systematic review needs and checks them: a protocol, a PRISMA record, a screening
> L31: The server has no language model inside. The agent searches, reads, decides and writes. The server stores each deci

## 星数曲线

```mermaid
xychart-beta
    title "Aryan-Pardeshi/CiteProof-AI-MCP 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-10-25"]
    y-axis "stars" 87 --> 90
    line [89, 88]
```

2026-10-24 89 → 2026-10-25 88（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8d34a9986286` · [字段定义](../../DATASET.md)*
