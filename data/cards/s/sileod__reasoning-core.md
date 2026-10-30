# sileod/reasoning-core

⭐ 52 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/sileod/reasoning-core) · 个人维护

**程序化生成可验证推理数据的 Python 库：面向预训练/后训练/评测/RL**

Reasoning Core 以 Python 库形式程序化生成一阶逻辑、符号数学、规划、算法、语法等 55 类可验证文本推理任务，答案格式规范并附带任务原生打分器，可作为 SFT 目标或 RL 的确定性奖励使用。提供训练与影响力 API，支持可复现的配对基线/处理实验。可扩展到大规模数据集生成（并行、断点续跑、JSONL 分片、Hugging Face Datasets 后处理），并在 Hugging Face 上提供超 10B token 的预生成数据集合。可集成 Prime Intellect、OpenReward、OpenEnv、reasoning-gym、SynLogic。要求 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 55 类覆盖逻辑/数学/规划/算法/语法的程序化任务，附任务原生打分器
- 同一打分器可作 SFT 目标与 RL 确定性奖励
- 大规模数据集生成管线：并行、断点续跑、JSONL 分片、HF Datasets 后处理
- 配对基线/处理的训练影响力实验 API，结果可复现

## 适用场景

- 为 LLM 预训练或后训练生成带可验证答案的推理语料
- 为 RL 训练提供程序化环境的确定性奖励信号
- 评测模型推理能力并测量单个任务对训练的影响

## 场景标签

`模型训练` `强化学习` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: **Procedural reasoning data for language-model pre-training, post-training, evaluation, and RL.**
> L5: Reasoning Core generates verifiable textual tasks across first-order logic, symbolic mathematics, planning, algorith
> L9: Tasks target compact, canonical answers and expose task-native scorers—clean targets for supervised fine-tuning (SFT

## 星数曲线

```mermaid
xychart-beta
    title "sileod/reasoning-core 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 50 --> 53
    line [51, 52, 52]
```

2026-10-18 51 → 2026-10-30 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fd185515020e` · [字段定义](../../DATASET.md)*
