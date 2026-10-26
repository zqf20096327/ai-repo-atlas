# google-deepmind/distribution_shift_framework

⭐ 90 · Python · Apache-2.0 · 推送 2026-05-19 · [GitHub](https://github.com/google-deepmind/distribution_shift_framework) · 组织维护

**给ML研究者：分布偏移下训练与评测模型的JAX框架**

DeepMind 论文 A Fine-Grained Analysis on Distribution Shift (Wiles et al., 2022) 的配套代码：基于 JAX/Jaxline 的分类实验框架，支持 ERM、IRM、DANN、SagNet、JTT 等 8 种训练方法，ResNet18/50/101 与 MLP 架构，dSprites、SmallNorb、Shapes3D 三个数据集；可配置 ood、correlated、lowdata 三类分布偏移场景及标签噪声、固定数据量修饰条件，并自动生成超参 sweep。通过 run.sh 创建虚拟环境安装依赖（测试于 Python 3.9.9），命令行运行训练与评测。

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

- 8 种训练方法（ERM/IRM/DANN/SagNet/JTT 等）与 ResNet/MLP 架构
- 3 类分布偏移场景（ood/correlated/lowdata）+ 噪声与固定数据量修饰
- 自动生成多超参 sweep，可通过配置项组合切换实验
- 基于 JAX/Jaxline，提供 run.sh 一键建环境并验证导入

## 适用场景

- 复现论文中的分布偏移实验结果
- 评测自己模型在不同分布偏移下的鲁棒性
- 比较 ERM、IRM、DANN 等方法在偏移场景的表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository contains the code of the distribution shift framework presented
> L4: in A Fine-Grained Analysis on Distribution Shift
> L11: Currently the following training methods are supported (by setting the

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/distribution_shift_framework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 89 --> 91
    line [90, 90]
```

2026-10-18 90 → 2026-10-26 90（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5e0be1a3b8d1` · [字段定义](../../DATASET.md)*
