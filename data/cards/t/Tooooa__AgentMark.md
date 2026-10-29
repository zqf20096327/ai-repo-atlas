# Tooooa/AgentMark

⭐ 100 · Python · MIT · 推送 2026-04-08 · [GitHub](https://github.com/Tooooa/AgentMark) · [官网](https://arxiv.org/abs/2601.03294) · 组织维护 · 中文 README

**LLM Agent 行为水印框架：为 Agent 嵌入可溯源版权水印**

实现 Agent Mark 论文（ACL 2026）效用保持与分布保留水印算法的实验与评测框架。将 Agent 决策分解为规划行为与执行动作，在规划阶段通过分布保留采样嵌入多比特水印，支持鲁棒性验证（日志缺失、轨迹截断、语义重写攻击）与误报率分析。提供 Docker 一键部署的 Web 可视化平台、无需改码的 OpenAI Chat Completions 兼容代理网关，覆盖 ToolBench、ALFWorld、Oasis 三类实验环境。面向 AI 安全与版权保护研究者和 Agent 开发者，属实验性研究代码库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规划阶段分布保留采样嵌入水印，保持任务效用
- 代理网关模式：改 API Base URL 即可为现有 Agent 加水印，兼容 OpenAI Chat Completions 协议框架
- 支持多比特容量嵌入与 RLNC 抗擦除编码的鲁棒性评测
- 覆盖 ToolBench 工具调用、ALFWorld 具身智能、Oasis 社交模拟三类环境

## 适用场景

- 为已上线的 Agent 系统增加版权保护与溯源能力
- 评测行为水印算法在复杂 Agent 任务中的性能与鲁棒性
- 研究日志缺失、语义重写等攻击下水印的存活能力

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L21: **AgentMark** 是一个专注于 **LLM Agent 行为水印** 的实验与评测框架，实现了 **Agent Mark** 论文中提出的效用保持和分布保留水印算法。
> L32: 本项目旨在提供一套可复现、模块化且易于扩展的代码库，用于评估水印算法在复杂 Agent 任务中的性能、鲁棒性及隐蔽性。核心机制将 Agent 的决策过程分解为 **规划行为** 和 **执行动作**，通过在规划阶段进行分布保留采样
> L156: 无需修改原有代码，只需将现有 Agent 的 API Base URL 指向网关地址，即可一键获得行为水印能力。这种模式特别适合开发者在不触动核心逻辑的情况下，快速为已有 Agent 系统增加版权保护与溯源功能。

## 星数曲线

```mermaid
xychart-beta
    title "Tooooa/AgentMark 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 98 --> 101
    line [99, 100, 100]
```

2026-10-18 99 → 2026-10-29 100（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `51e8b4b4edcc` · [字段定义](../../DATASET.md)*
