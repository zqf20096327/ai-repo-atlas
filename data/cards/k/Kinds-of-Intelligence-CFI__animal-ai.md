# Kinds-of-Intelligence-CFI/animal-ai

⭐ 105 · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/Kinds-of-Intelligence-CFI/animal-ai) · [官网](https://sites.google.com/csah.cam.ac.uk/animalai/) · 组织维护

**Unity 仿真实验环境：供人与 AI 做跨物种认知测试**

基于 Unity3D 的比较认知研究环境，用于在人类、动物与 AI 之间开展跨学科测试。将 Unity 学习环境封装为 gym(nasium) 与 PettingZoo 格式，内置 Animal-AI Olympics 竞赛的 900 个任务与示例任务，支持 YAML 配置文件的过程化生成。提供玩家模式（人类测试）与训练模式（强化学习，支持 TensorFlow 分析），并集成在环境中运行 LLM 试验的通道。在 Windows 11、Linux、macOS 上测试，支持 Python 3.14.x，维护 ML-Agents 的分支以适配本项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Unity 环境封装为 gym(nasium) 与 PettingZoo 格式
- 900 个 Animal-AI Olympics 任务库
- YAML 配置文件过程化生成
- 支持在环境中用 LLM 运行试验

## 适用场景

- 在统一环境中对比测试 AI、人类与动物的认知能力
- 用 900 个现成任务或自生成配置做强化学习训练与评测
- 人类受试者通过玩家模式参与认知实验

## 场景标签

`强化学习` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L34: - Wraps Unity learning environments into both gym(nasium) and PettingZoo formats
> L52: - **Training Mode:** Designed for Reinforcement Learning, with support for TensorFlow analysis

## 星数曲线

```mermaid
xychart-beta
    title "Kinds-of-Intelligence-CFI/animal-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 103 --> 106
    line [104, 105]
```

2026-10-18 104 → 2026-10-29 105（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `48a9174f2c6e` · [字段定义](../../DATASET.md)*
