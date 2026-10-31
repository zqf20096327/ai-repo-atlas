# agenerale/conditional-variable-flow-matching

⭐ 13 · Python · MIT · 推送 2026-03-16 · [GitHub](https://github.com/agenerale/conditional-variable-flow-matching) · [官网](https://arxiv.org/abs/2411.08314) · 个人维护

**科研代码库：条件变量流匹配训练条件连续归一化流**

论文 Conditional Variable Flow Matching (CVFM) 的官方代码仓库，复现其主要实验。CVFM 是 Flow Matching 的扩展，用于从非配对训练数据中训练摊销化条件连续归一化流（CNF），解耦并建模条件动态，仅需在某时刻观测到 (x,y) 对。仓库包含教程 notebook、2D 示例问题（two moons、8 gaussians 等）的生成代码，以及材料微结构演化（相场）案例研究代码。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Flow Matching 的条件扩展，支持非配对数据训练
- 教程 notebook 覆盖论文中多个 2D 映射测试用例
- 包含材料微结构演化（相场）案例研究代码

## 适用场景

- 复现 CVFM 论文的主要实验
- 学习条件流匹配在 2D 映射问题上的用法
- 将条件 CNF 方法应用于微结构演化建模

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: Conditional Variable Flow Matching (CVFM) is a robust extension to Flow Matching for training amortized conditional 
> L15: This repository contains the code to reproduce the main experiments for CVFM:

## 星数曲线

```mermaid
xychart-beta
    title "agenerale/conditional-variable-flow-matching 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d6a5ad235278` · [字段定义](../../DATASET.md)*
