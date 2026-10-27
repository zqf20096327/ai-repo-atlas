# MurrellGroup/Flowfusion.jl

⭐ 40 · Julia · MIT · 推送 2026-05-29 · [GitHub](https://github.com/MurrellGroup/Flowfusion.jl) · [官网](https://murrellgroup.github.io/Flowfusion.jl/) · 组织维护

**Julia 生成式模型库：统一训练与采样扩散/流匹配模型**

Julia 语言包，在单一框架与接口内提供扩散模型与流匹配模型的训练和采样，覆盖连续、离散与多种黎曼流形状态空间（经 Manifols.jl 支持），并支持复合状态（连续与离散变量联合采样）。核心机制是 bridge 过程采样中间状态、训练模型预测朝 X1 的移动，gen 函数用学习到的模型生成序列。提供确定性流匹配、流形布朗桥、离散流匹配等变体与多个示例脚本，通过 Julia 包管理器从 GitHub 安装。

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

- 连续、离散、流形状态空间统一在同一框架与接口
- 复合状态支持（连续与离散变量联合采样）
- 条件生成（masking）与可控噪声/全确定性路径
- 时间缩放调度与多种过程变体（Deterministic/ManifoldProcess/离散流等）

## 适用场景

- 训练与采样流匹配/扩散生成模型
- 在环面、概率单纯形等流形上做生成建模
- 对部分观测条件下的变量做条件采样

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L8: Flowfusion.jl is a Julia package for training and sampling from diffusion and flow matching models (and some things 
> L16: - Flexible initial $X_0$ distribution
> L18: - States: Continuous, discrete, and a wide variety of manifolds supported (via Manifolds.jl)

## 星数曲线

```mermaid
xychart-beta
    title "MurrellGroup/Flowfusion.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-27 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4d2e373af6c4` · [字段定义](../../DATASET.md)*
