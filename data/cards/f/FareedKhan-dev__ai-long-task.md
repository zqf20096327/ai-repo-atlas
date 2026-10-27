# FareedKhan-dev/ai-long-task

⭐ 56 · Python · Apache-2.0 · 推送 2026-01-08 · [GitHub](https://github.com/FareedKhan-dev/ai-long-task) · [官网](https://medium.com/@fareedkhandev/e48b8b39cc9e) · 个人维护

**AlphaEvolve 启发的长周期任务代码进化框架（多 agent 进化引擎）**

受 Google AlphaEvolve 启发的开源框架 LongHorizon，面向需要数小时到数天持续迭代优化的工程与科研任务。机制包括：MAP-Elites 多样性存档、岛屿模型并行进化、多级级联评估（测试、性能剖析、视觉检查、LLM-as-a-Judge）、diff 式代码进化、断点续跑，以及基于 browser-use 的自主网络调研（SOTA Hunter）。计算层为 provider 无关的 LLM 集成接口，支持任意 OpenAI 兼容 API，可混用多模型加权采样。提供 CLI 与 Python API 两种使用方式，附 Dockerfile。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MAP-Elites + 岛屿模型的进化引擎，保持解多样性
- 多级级联评估管道（测试/性能/视觉 QA/LLM-as-a-Judge）
- 基于 SEARCH/REPLACE 块的 diff 式进化以降低 token 成本
- 浏览器自主调研（GitHub/arXiv）注入 SOTA 知识，支持断点续跑

## 适用场景

- 长时间迭代优化代码（如 GPU kernel、算法实现）
- 将进化引擎作为 Python 库集成到自动化工程流水线
- 多模型混用下平衡成本与能力的自动代码搜索实验

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L14: State-of-the-art AI models can maintain reasoning chains for hours, but achieving reliable, multi-day performance o
> L196: - **`llm.base.LLMInterface`**: An abstract base class that defines the contract for all LLM clients, ensuring our 

## 星数曲线

```mermaid
xychart-beta
    title "FareedKhan-dev/ai-long-task 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-27 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `30349a1619c7` · [字段定义](../../DATASET.md)*
