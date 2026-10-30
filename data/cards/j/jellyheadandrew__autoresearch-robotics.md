# jellyheadandrew/autoresearch-robotics

⭐ 18 · Python · 推送 2026-03-10 · [GitHub](https://github.com/jellyheadandrew/autoresearch-robotics) · [官网](https://jellyheadandrew.github.io) · 个人维护

**让编码 agent 自主迭代机器人 RL 实验的实验框架**

基于 Karpathy 的 autoresearch 改造的机器人自主研究框架：编码 agent（如 Claude Code）读取 program.md 后循环执行分析→假设→修改 train.py→训练→评估，其中评估包含 MuJoCo 渲染的行为视觉分析。基线算法为 SAC+HER，默认任务 FetchReach（约 30 实验/小时），通过 setup_task.py 模板支持多个 MuJoCo 任务与 Isaac Sim 原型。要求 Python 3.10+、NVIDIA GPU 与编码 agent，人通过编辑 program.md 参与迭代。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent 自主循环：分析→假设→修改→训练→评估→保留/丢弃
- MuJoCo 渲染行为帧供 agent 视觉分析，配合定量指标
- setup_task.py 模板系统支持多任务与多模拟器（Isaac Sim 为原型）
- 固定 wall-clock 时间预算训练，指标为 eval_success_rate

## 适用场景

- 夜间无人值守地自动跑机器人 RL 超参/算法迭代实验
- 通过视觉反馈诊断机器人行为问题（如过冲与振荡）
- 以自定义 program.md 定义自己的 agent 实验流程

## 场景标签

`强化学习` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Karpathy's autoresearch adapted for robotics -- autonomous overnight experiment optimization with robotics simulatio
> L13: - **`train.py`** -- the single file the agent edits. Contains the full SAC+HER policy, optimizer, and training loop
> L45: The agent reads `program.md`, creates a branch, runs the baseline, then loops: analyze → hypothesize → modify `trai

## 星数曲线

```mermaid
xychart-beta
    title "jellyheadandrew/autoresearch-robotics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `765f7613060a` · [字段定义](../../DATASET.md)*
