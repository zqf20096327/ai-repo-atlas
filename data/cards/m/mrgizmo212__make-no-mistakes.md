# mrgizmo212/make-no-mistakes

⭐ 28 · CSS · 推送 2026-07-02 · [GitHub](https://github.com/mrgizmo212/make-no-mistakes) · [官网](https://mrgizmo212.github.io/make-no-mistakes/) · 个人维护

**面向开发者的模型无关 agent harness 架构研究笔记（电子书）**

一份仍在编辑中的架构规格笔记，探讨如何构建模型无关的 agent harness（循环、记忆、子代理、工具、MCP、技能、语音），按 5 层架构组织，并从 Hermes、Codex、Pi、LangGraph、OpenClaw、LiteLLM 等既有项目中提取各层模式。明确主张各项目作为模式供体通过既有接口（OpenAI 兼容 API、MCP、SSE、SKILL.md）组合而非合并代码库。内容以 GitHub Pages 在线阅读或 git clone 离线阅读形式提供，作者为个人，CC BY 4.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 5 层架构组织 agent harness 的循环/记忆/子代理/工具/MCP/技能/语音议题
- 从 Hermes、Codex、Pi、LangGraph、OpenClaw、LiteLLM 等项目提取各层模式
- 通过 OpenAI 兼容 API、MCP、SSE、SKILL.md 等既有接口组合而非合并代码库

## 适用场景

- 设计自己的 agent harness 前查阅分层架构建议
- 了解各开源 agent 项目在不同架构层的模式取舍
- 离线或在线研读完整的 harness 架构规格与研究报告

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5:  Notes toward a model-agnostic agent harness.
> L14: Working notes on how to build a clean, model-agnostic **agent harness** — loops, memory, subagents, tools, MCPs, sk
> L62: |IV · Studies|Hermes, Codex, Pi, LangGraph, LangChain, OpenClaw, LiteLLM, …|

## 星数曲线

```mermaid
xychart-beta
    title "mrgizmo212/make-no-mistakes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `02758e69ea9f` · [字段定义](../../DATASET.md)*
