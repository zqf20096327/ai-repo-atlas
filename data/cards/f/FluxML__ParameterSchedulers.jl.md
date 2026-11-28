# FluxML/ParameterSchedulers.jl

⭐ 41 · Julia · MIT · 推送 2026-11-24 · [GitHub](https://github.com/FluxML/ParameterSchedulers.jl) · 组织维护

**给 ML 训练提供超参数调度函数的 Julia 库**

ParameterSchedulers.jl 提供 ML 常见超参数调度器：实现 Step、Exp、CosAnneal、OneCycle、Triangle、Poly、Inv、Sin 等 13 种调度函数，覆盖衰减型与循环型两类，并提供组合工具以构造更高阶调度。包本身与框架解耦，同时提供与 Flux.jl 优化器配套的 Scheduler 接口，可将调度直接包裹到优化器上。README 未给出安装命令与许可证信息。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 13 种常见超参数调度函数（衰减型与循环型）
- 框架无关，另提供与 Flux.jl 优化器配套的 Scheduler 接口
- 提供高阶调度组合工具，支持自定义新调度
- 每个调度附 UnicodePlots 示例绘图

## 适用场景

- 训练时按步数或迭代次数衰减学习率/动量
- 训练中使用余弦退火或 OneCycle 等循环调度
- 基于已有调度组合构造更复杂的调度曲线

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L6: ParameterSchedulers.jl provides common machine learning (ML) schedulers for hyper-parameters. Though this package is
> L16: This is a table of the common schedules implemented, but ParameterSchedulers provides utilities for creating more e

## 星数曲线

```mermaid
xychart-beta
    title "FluxML/ParameterSchedulers.jl 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-11-26 41 → 2026-11-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `8586b77d829a` · [字段定义](../../DATASET.md)*
