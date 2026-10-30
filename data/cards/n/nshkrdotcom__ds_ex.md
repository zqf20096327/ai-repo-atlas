# nshkrdotcom/ds_ex

⭐ 19 · Elixir · MIT · 推送 2026-08-27 · [GitHub](https://github.com/nshkrdotcom/ds_ex) · 组织维护

**DSPEx（Elixir 版 DSPy）的组件缺口清单文档**

本 README 是 DSPEx（BEAM/Elixir 实现的 AI 程序优化框架）对照 Python DSPy 的功能差距目录：逐项列出已实现组件（如 BootstrapFewShot、SIMBA、Predict/ChainOfThought/ReAct、OpenAI 基础客户端）与缺失组件（7/10 teleprompter、11/15 predict 模块、检索系统 0/25、断言 0/5、模型 provider 15/20 缺失等），并标注优先级与对应 DSPy 源文件。文档面向 DSPEx 贡献者，用于规划补齐 feature parity 的工作范围。

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

- 对照 DSPy 逐类盘点缺失组件及对应源文件路径
- 已实现：BootstrapFewShot、SIMBA、ChainOfThought/ReAct（含 Elixact 校验）、OpenAI 基础集成
- 检索系统 0/25、断言 0/5 完全缺失，为主要功能缺口

## 适用场景

- 评估 DSPEx 当前与 DSPy 的功能差距以决定选型
- 为 DSPEx 贡献者查找待实现组件及参考的 DSPy 文件
- 跟踪 SIMBA 等优化器的集成进度

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L5: This document provides a comprehensive catalog of ALL DSPy components that are missing or incomplete in DSPEx. It se
> L358: **DSPy integrates with 100+ models via LiteLLM**

## 星数曲线

```mermaid
xychart-beta
    title "nshkrdotcom/ds_ex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `2eaf0b1b3df4` · [字段定义](../../DATASET.md)*
