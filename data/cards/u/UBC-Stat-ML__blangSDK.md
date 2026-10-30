# UBC-Stat-ML/blangSDK

⭐ 25 · Xtend · BSD-2-Clause · 推送 2025-11-26 · [GitHub](https://github.com/UBC-Stat-ML/blangSDK) · [官网](https://www.stat.ubc.ca/~bouchard/blang/) · 组织维护

**贝叶斯概率编程语言 Blang 的 SDK：构建模型并做 MCMC 推断**

Blang 的软件开发工具包仓库，提供适用于采样的基础数据类型、创建新数据类型与分布的基础设施、标准概率分布，以及 Adaptive Non-Reversible Parallel Tempering、Sequential Change of Measure 等 MCMC 推断算法；另含 MCMC 测试基础设施、推断因子图及其稀疏模式的静态分析运行时，以及自动后处理（诊断、轨迹/密度图、摘要生成）。面向 Blang 语言的使用者与开发者，可通过 Pigeons-Blang 桥接以 MPI 在上千台机器上运行。有 Docker 镜像与 JSS 论文（2022）可引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供适用于采样的基础数据类型与标准概率分布
- 含 Adaptive Non-Reversible Parallel Tempering 等推断算法
- 运行时静态分析推断因子图及稀疏模式
- 经 Pigeons-Blang 桥接可用 MPI 在上千台机器上运行

## 适用场景

- 用 Blang 语言构建概率图模型并做 MCMC 推断
- 为 Blang 创建自定义数据类型与分布
- 自动生成 MCMC 诊断与后处理报告

## 场景标签

 · 领域:统计计算/概率编程

## 证据(README 行号)

> L11: This is one of the repositories hosting Blang's code. This one contains the Blang's SDK (Software Development Kit),
> L15: - Inference algorithms for such datatypes, such as Adaptive Non-Reversible Parallel Tempering and Sequential Change

## 星数曲线

```mermaid
xychart-beta
    title "UBC-Stat-ML/blangSDK 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `50e8044b329f` · [字段定义](../../DATASET.md)*
