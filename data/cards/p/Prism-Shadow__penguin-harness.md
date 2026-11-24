# Prism-Shadow/penguin-harness

⭐ 3,301 · TypeScript · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/Prism-Shadow/penguin-harness) · [官网](https://penguin.ooo/) · 组织维护 · 中文 README

**面向开发者的 agent 自进化（RSI）统一框架与平台**

PenguinHarness 是一个开源 agent 自进化（递归自我改进/RSI）框架：模型固定不变，框架层（提示词、Skills、工具、hooks）由 agent 迭代优化。内置 10 种 RSI 算法插件（OPRO、APE、ACE、AWM、SkillAdam 等）与 17 个 Docker 化基准，评分进入评估中心，每次变更前有快照。同时提供一句话生成 agent 应用、浏览器自动化、远程机器接入、统一 Agent API 与 A2UI 回复。以桌面应用、Web App、CLI、SDK 四种形态运行，支持闭源与开源模型及自定义 OpenAI 协议端点。

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

- 10 种 RSI 算法以插件形式共用同一基准、计分板与快照机制
- 一句话让 agent 生成带页面与运行说明的应用
- 17 个内置基准以 Harbor 任务形式在 Docker 中运行
- 桌面应用/Web App/CLI/SDK 四种形态，CLI 可被其他 agent 驱动

## 适用场景

- 对固定模型做提示词与 Skills 的自动化迭代优化
- 一句话生成合同审查等垂直 agent 应用
- 在基准上评估并对比多轮自进化后的 agent 表现

## 场景标签

`提示工程` `浏览器自动化` `编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L36: PenguinHarness is an open-source framework for agent self-evolution (recursive self-improvement, RSI). The model st
> L38: - **Every RSI algorithm in one framework.** Default, OPRO, APE, ACE, AWM, SkillAdam, SkillOpt, OpenSkill and TRACE 

## 星数曲线

```mermaid
xychart-beta
    title "Prism-Shadow/penguin-harness 星数(近 28 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 2860 --> 3341
    line [2900, 2916, 2929, 2941, 2949, 2973, 2992, 3024, 3059, 3071, 3078, 3090, 2941, 3196, 3207, 3215, 3222, 3230, 3237, 3244, 3252, 3262, 3272, 3289, 3294, 3297, 3301, 3301]
```

2026-10-22 2,900 → 2026-11-24 3,301（+401）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `eea26d0e4ebd` · [字段定义](../../DATASET.md)*
