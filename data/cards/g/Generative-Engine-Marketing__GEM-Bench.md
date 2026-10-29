# Generative-Engine-Marketing/GEM-Bench

⭐ 19 · Python · Apache-2.0 · 推送 2026-07-04 · [GitHub](https://github.com/Generative-Engine-Marketing/GEM-Bench) · [官网](https://gem-bench.org) · 组织维护

**生成式引擎营销（GEM）的广告注入回答生成与评测基准**

面向 Generative Engine Marketing 领域的完整基准：研究如何将相关广告整合进 LLM 回答（ad-injected response 生成），并提供评测框架。内置三个数据集（MT-Human 多轮对话、LM-Market 真实营销对话、CA-Prod 搜索 AI 概览场景），覆盖定量指标（流畅性、注入率、CTR）与定性指标（满意度、参与度）。实现 Ad-Chat、Ad-LLM（GI-R/GIR-R/GIR-P）、RAG-AdChat 等基线方案，并提供 gembench CLI 用于广告库校验、注入与评分，以及模型价格表管理。论文被 KDD '26 接收。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个数据集覆盖 chatbot 与搜索两类广告注入场景
- 定量+定性的多维度指标体系（流畅性/注入率/CTR/满意度/参与度）
- 提供 gembench CLI 支持广告库校验、注入、评分与模型价格管理
- 内置 Ad-Chat、Ad-LLM 多配置、RAG-AdChat 基线实现

## 适用场景

- 研究者复现和比较广告注入回答的生成方案
- 为 LLM 广告投放系统做生成与评分的批量评测
- 校验自定义广告库并按项目需求覆盖模型价格配置

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: This repository provides a complete benchmark for **Generative Engine Marketing (GEM)**, an emerging field that focu
> L13: * **GEM-BENCH:** The first complete benchmark designed for the generation and evaluation of ad-injected responses.

## 星数曲线

```mermaid
xychart-beta
    title "Generative-Engine-Marketing/GEM-Bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a1c40f049c06` · [字段定义](../../DATASET.md)*
