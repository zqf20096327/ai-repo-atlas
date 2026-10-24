# physical-superintelligence-lab/Agent-Driver

⭐ 302 · Python · MIT · 推送 2025-12-09 · [GitHub](https://github.com/physical-superintelligence-lab/Agent-Driver) · [官网](https://physical-superintelligence-lab.github.io/Agent-Driver/) · 组织维护

**用 LLM 作认知 agent 的自动驾驶语言 agent 研究代码**

论文 Agent-Driver 的官方代码库，将 LLM 作为认知 agent 引入自动驾驶：通过函数调用提供工具库、提供常识与经验知识的认知记忆、以及支持思维链推理、任务规划、运动规划与自我反思的推理引擎。运行需 OpenAI API 账号，需先微调 GPT 运动规划器（默认 10% 数据、约 10 美元内），在 nuScenes 数据集上训练与评测。面向自动驾驶与具身智能方向的研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 认知 agent：工具库 + 认知记忆 + 推理引擎
- 需 OpenAI API 账号并微调 GPT 运动规划器
- 在 nuScenes 数据集上训练与评测运动规划

## 适用场景

- 复现论文的自动驾驶规划实验
- 在 nuScenes 上评测语言 agent 的规划性能
- 研究 LLM 工具调用与推理在驾驶任务中的应用

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This is a repo of our arXiv pre-print Agent-Driver [Project Page].
> L9: Human-level driving is an ultimate goal of autonomous driving. Conventional approaches formulate autonomous driving 

## 星数曲线

```mermaid
xychart-beta
    title "physical-superintelligence-lab/Agent-Driver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 300 --> 302
    line [301, 301]
```

2026-10-18 301 → 2026-10-24 301（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `e4d5eee83f72` · [字段定义](../../DATASET.md)*
