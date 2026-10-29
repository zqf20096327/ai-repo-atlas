# google-deepmind/egg

⭐ 20 · Python · Apache-2.0 · 推送 2026-04-15 · [GitHub](https://github.com/google-deepmind/egg) · 组织维护

**探索 LLM 强化学习的轻量 CPU 仿真环境**

DeepMind 维护的极简仿真环境，用于在大规模分布式训练之前探索 LLM 上的强化学习。设计目标为轻量透明（不依赖大型框架）、算法优先（代码贴近论文伪代码）、可秒级启动迭代，且概念可迁移到更大规模。提供 baseline 实验脚本与测试套件，通过 pip 从源码安装，附 BibTeX 引用格式。面向做 RL on LLM 研究与快速原型的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无大型框架依赖的极简 RL 仿真环境
- CPU 友好，秒级启动与测试想法
- 代码风格贴近论文伪代码
- 提供 baseline 实验与 pytest 测试

## 适用场景

- 在大规模训练前快速验证 RL on LLM 想法
- 教学或研究中复现算法伪代码
- 在 CPU 环境做轻量 RL 实验迭代

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: A minimal, CPU-friendly simulation environment for exploring RL on LLMs — before
> L12: - **Tiny + Transparent**: No big framework, no magic.
> L13: - **Algorithm-first**: Code should resemble paper pseudocode.

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/egg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b8386a604f69` · [字段定义](../../DATASET.md)*
