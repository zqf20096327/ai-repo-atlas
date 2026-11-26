# HATS-ICT/decoy

⭐ 10 · Jupyter Notebook · MIT · 推送 2026-09-26 · [GitHub](https://github.com/HATS-ICT/decoy) · 组织维护

**面向多智能体策略规划研究的 CS:GO 离散化模拟环境**

DECOY 将 3D CS:GO 游戏转化为离散化模拟：使用在职业比赛数据上训练的神经模型（伤害指示与伤害结果 checkpoint 随仓库提供），以航点图上的 9 个离散动作和固定维度观测实现 2v2 等小规模对战。环境实现 PettingZoo AEC API，智能体异步决策，奖励项可通过 env/rewards.py 配置，含 objective_progress 势能塑形项。附 IPPO 基线训练代码，单进程仅能运行一个环境（Panda3D 限制），Windows 下 torch 需先于 Panda3D 导入。

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

- 实现 PettingZoo AEC API 并通过 pettingzoo.test.api_test
- 神经模型基于职业 CS:GO 锦标赛数据训练（预训练 checkpoint 随仓库提供）
- 可配置奖励规范（shape/sparse）与基于 Dijkstra 距离场的 objective_progress 塑形项
- 自带 IPPO 基线（约 500 行 torch+numpy，支持 action masking 与 GAE）

## 适用场景

- 研究 CS:GO 场景下的多智能体策略规划
- 训练与评估 MARL 算法（如 IPPO、selfplay）
- 以无头模式在 CPU 上跑约 1000 决策/秒的快速模拟
- 基于真实比赛回放数据训练伤害模型

## 场景标签

`多智能体` `强化学习` · 领域:Agent 开发

## 证据(README 行号)

> L3: 🎯 **A high-fidelity CS:GO simulation environment for strategic multi-agent planning research.** DECOY transforms com
> L32: DECOY implements the PettingZoo AEC API and
> L122: `marl/` contains a self-contained IPPO implementation (independent PPO with


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `fa70e0f453b2` · [字段定义](../../DATASET.md)*
