# Kendiukhov/ergodicity_library

⭐ 24 · Python · MIT · 推送 2026-08-29 · [GitHub](https://github.com/Kendiukhov/ergodicity_library) · 个人维护

**遍历性与随机过程研究库：模拟、求解与训练决策智能体**

Python 科研库，面向遍历性经济学及更广的随机过程研究：提供布朗运动、Lévy 过程、分数布朗运动等过程的模拟，重尾过程分析，SDE 的数值与符号求解，多进程并行计算与动态可视化。Agents 模块用进化算法与机器学习模型训练在不确定性下决策的人工智能体。依赖 numpy/scipy/TensorFlow/Keras，机器学习组件可选；ffmpeg 仅用于部分可视化功能，缺失不影响核心功能。提供文档站点与配套 ErgodicityGPT 问答助手。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多种随机过程模拟（布朗运动、Lévy、分数布朗运动、带记忆过程）
- SDE 的符号与数值求解（solve.py / partial_sde.py）
- 进化算法与机器学习训练决策智能体（Agents 模块）
- 多进程并行支持大规模模拟

## 适用场景

- 模拟并分析金融市场中的几何布朗运动等随机模型
- 研究非遍历动力学与时间平均行为
- 在随机环境中用进化算法训练决策智能体
- 对厚尾分布过程做拟合与预渐近行为分析

## 场景标签

`金融量化` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L11: - **Artificial Agents**: Evolutionary algorithms and machine learning models for training agents to make decisions 
> L156: 3. **Agents**: Tools to create and train artificial agents using evolutionary algorithms and machine learning mode
> L161:  - `evolutionary_nn.py`: Implements evolutionary training for agent neural networks.

## 星数曲线

```mermaid
xychart-beta
    title "Kendiukhov/ergodicity_library 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `5a37dd35e315` · [字段定义](../../DATASET.md)*
