# AQ-MedAI/RagQALeaderboard

⭐ 28 · Python · NOASSERTION · 推送 2026-01-27 · [GitHub](https://github.com/AQ-MedAI/RagQALeaderboard) · [官网](https://huggingface.co/datasets/AQ-MedAI/RAG-QA-Leaderboard) · 组织维护 · 中文 README

**RAG 问答系统的评测基准与排行榜框架**

面向研究人员和开发者的 RAG 系统评测框架：整合 HotpotQA、PopQA、MuSiQue、TriviaQA、2Wiki、PubMedQA 等问答数据集（共 30,135 条查询，检索池约 109 万篇维基百科文档），通过 make 命令或 Python 脚本一键运行评测，输出 Accuracy、F1、Exact Match 等指标并生成 HTML/JSON 报告。支持 API 端点与本地模型（vLLM）两种推理方式，并可对 Retriever 与 Generator 组件单独评测。安装方式为 git clone 源码加 pip 依赖，评测数据从 Hugging Face Hub 下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 整合 6 个 QA 数据集共 30,135 条查询，含单跳/多跳/领域特定场景
- 一键生成 HTML/JSON 评测报告，支持 Accuracy/F1/Exact Match 指标
- 支持 API 与本地推理（vLLM/transformers）两种评测模式
- 可对 Retriever 与 Generator 组件进行隔离评测

## 适用场景

- 统一条件下对比多个 RAG 模型的问答性能
- 分析检索器与生成器各组件的表现
- 以可复现基准测试新 RAG 模型并生成报告

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A standardized and fair evaluation framework and leaderboard for Retrieval-Augmented Generation (RAG) systems.
> L5: `RAGQA-Leaderboard` aims to provide researchers and developers with a unified and reproducible benchmark for evaluat
> L12: * **📊 Standardized Evaluation Framework**: Provides a unified and fair evaluation pipeline, ensuring that different

## 星数曲线

```mermaid
xychart-beta
    title "AQ-MedAI/RagQALeaderboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ccfa3b693767` · [字段定义](../../DATASET.md)*
