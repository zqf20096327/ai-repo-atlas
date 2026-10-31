# lucidrains/HoST-pytorch

⭐ 46 · Python · MIT · 推送 2026-08-05 · [GitHub](https://github.com/lucidrains/HoST-pytorch) · 个人维护

**人形机器人起身控制论文的 PyTorch 复现库（wip）**

PyTorch 实现论文 Learning Humanoid Standing-up Control across Diverse Postures（arXiv:2502.08378）提出的人形机器人站立/起身强化学习控制方法：包含一组奖励函数设计，并采用波士顿大学提出的多 critic 方法进行验证。以 Python 库形式提供，pip 安装后可实例化 Agent 并在 mock 环境中运行训练流程。README 标注为 wip（进行中）状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 复现论文的多姿态人形起身控制
- 包含论文提出的奖励函数集合
- 采用多 critic（multiple critics）训练方法

## 适用场景

- 复现或学习人形机器人起身控制论文方法
- 在 mock 环境中试验强化学习训练流程

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: ## HoST - Pytorch (wip)
> L5: Implementation of Humanoid Standing Up, from the paper Learning Humanoid Standing-up Control across Diverse Postures

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/HoST-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8ffa4c0cc8c0` · [字段定义](../../DATASET.md)*
