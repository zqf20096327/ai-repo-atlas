# liruiw/GenSim

⭐ 360 · Python · MIT · 推送 2026-08-18 · [GitHub](https://github.com/liruiw/GenSim) · [官网](https://liruiw.github.io/gensim) · 组织维护

**用 LLM 生成机器人仿真任务与环境的研究框架**

GenSim 探索用 LLM 代码生成流水线编写 PyBullet 机器人仿真环境与专家目标，以自底向上/自顶向下两类提示范式批量生成仿真任务，输出编译、运行时与多样性统计。生成任务可用于多任务策略训练与算法基准测试（100+ 任务），并支持对 GPT-3.5/davinci 微调及 Code-LLAMA 微调与离线评测。安装需配置 OpenAI API key（默认 GPT-4），训练与任务脚本位于 cliport 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 代码生成流水线批量生成机器人仿真任务与环境
- 提供 GPT/davinci 微调与 Code-LLAMA 微调及离线评测脚本
- 100+ 生成任务可用于多任务策略训练基准
- 统计输出涵盖编译、运行时、任务设计与多样性分数

## 适用场景

- 批量生成机器人操作仿真任务扩充训练环境
- 在 100+ 任务上做多任务策略训练与算法基准测试
- 微调 LLM 提升任务生成质量并离线评测

## 场景标签

`代码生成` `微调` · 领域:编码与开发

## 证据(README 行号)

> L1: # GenSim: Generating Robotic Simulation Tasks via Large Language Models
> L7: This repo explores the use of an LLM code generation pipeline to write simulation environments and expert goals to a
> L55: 0. Note that the 100+ generated tasks by GenSim can be used for benchmarking algorithms in multitask policy trainin

## 星数曲线

```mermaid
xychart-beta
    title "liruiw/GenSim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 359 --> 361
    line [360, 360]
```

2026-10-18 360 → 2026-10-29 360（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7a976959bf5d` · [字段定义](../../DATASET.md)*
