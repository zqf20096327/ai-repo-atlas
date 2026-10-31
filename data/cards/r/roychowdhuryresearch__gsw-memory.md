# roychowdhuryresearch/gsw-memory

⭐ 26 · Python · 推送 2026-08-01 · [GitHub](https://github.com/roychowdhuryresearch/gsw-memory) · 组织维护

**LLM 结构化长期记忆框架：为 RAG 构建生成式语义工作空间**

AAAI-26 与 ICML 2026 两篇论文的官方代码库，以 pip 包形式提供。功能包括将文档转换为结构化语义工作空间（GSW）、跨文档实体合并（local/global 两种策略）、基于实体抽取与匹配的问答，以及内置评测工具（Tulving Bench、LLM-as-a-Judge）。第二篇论文扩展出 Panini——写入时构建 QA 对结构化记忆、经 RICR 链式检索做多跳问答的持续学习系统，目前代码位于 playground 目录，正整合进主包。依赖 OpenAI 与 Voyage API key，基准数据发布在 HuggingFace。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 文档→GSW 结构化记忆转换与跨文档实体合并（local/global 策略）
- Panini：写入时构建 QA 对记忆、RICR 链式检索支持多跳问答与持续学习
- 内置 Tulving Bench 评测系统与 LLM-as-a-Judge 评估
- HuggingFace 提供 5 个数据集的 GSW 网络与 Platinum 评测分割（共 45,824 篇文档）

## 适用场景

- 为长叙事 RAG 构建情景记忆并做实体中心推理
- 多文档问答系统中维护结构化语义记忆
- 复现论文实验或在标准基准上评测记忆系统

## 场景标签

`Agent 记忆` `RAG` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: Official repository for the **Generative Semantic Workspaces (GSW)** framework. This codebase supports two papers:
> L8: A Python package for building structured memory systems using Generative Semantic Workspaces (GSW). The first paper 

## 星数曲线

```mermaid
xychart-beta
    title "roychowdhuryresearch/gsw-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `14a45c31c7dd` · [字段定义](../../DATASET.md)*
