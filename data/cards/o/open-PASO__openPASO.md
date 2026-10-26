# open-PASO/openPASO

⭐ 29 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/open-PASO/openPASO) · [官网](https://open-paso.github.io/openPASO/) · 组织维护

**MCP 服务器：让 AI 模型调用并运行 9 个有限元/多物理求解器**

open Platform for Agentic Simulation and Optimization：一个 MCP server，把 scikit-fem、NGSolve、Kratos、DUNE-fem、FEniCSx、deal.II、FEBio、4C、SPARTA 九个求解器统一接入。用户用自然语言描述物理问题，AI 模型选择求解器、编写输入文件、运行求解并校验结果，支持跨求解器耦合与 24 个工具。需 Python 3.10–3.13，通过 pip 安装，可接入既有 AI 应用或使用自己的 OpenRouter key。项目自述处于活跃开发早期。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 九个有限元/多物理求解器统一接入一个 MCP server
- AI 模型完成选求解器、写输入、运行、校验答案的闭环
- 提供 openpaso install 命令与 setup_backend 工具按需安装求解器
- 支持在同一个问题上耦合两个求解器

## 适用场景

- 用自然语言驱动物理仿真而无需学习各求解器的输入格式
- 在 Claude Code/Cursor 等 AI 应用中直接运行有限元仿真
- 对比或耦合多个求解器求解同一物理问题

## 场景标签

 · 领域:计算力学/科学计算

## 证据(README 行号)

> L15:  An AI model picks a solver, writes its input, runs it, and checks the answer.
> L33: it: you describe what you want in a normal sentence, and the model picks a solver, writes the input,

## 星数曲线

```mermaid
xychart-beta
    title "open-PASO/openPASO 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-26 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `dce694a7415f` · [字段定义](../../DATASET.md)*
