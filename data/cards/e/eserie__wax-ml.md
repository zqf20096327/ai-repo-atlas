# eserie/wax-ml

⭐ 64 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/eserie/wax-ml) · [官网](https://eserie.github.io/wax-ml/) · 个人维护

**面向流数据与时间序列的 JAX 机器学习研究库**

WAX-ML 是研究导向的 Python 库，基于 JAX 与 Haiku 函数式范式，提供流数据与时间序列算法工具：'unroll' 变换可将任意有状态变换应用于序列数据并泛化 RNN 架构；stream 模块用 Poincaré–Einstein 式同步机制对齐不同时间分辨率的多个数据流，并配合数据追踪机制保证因果性；提供 pandas/xarray 访问器使 JAX 函数可直接作用于 DataFrame、Series、Dataset、DataArray；含 EWMA 滤波、OnlineSupervisedLearner 在线学习与 GymFeedback 反馈循环模块。当前流式处理基于内存数据，真实流支持尚在提案阶段（WEP4）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- unroll 变换：泛化 RNN 架构以实现任意有状态'滤波器'
- 多时间分辨率数据流同步机制，数据追踪保证不泄漏未来信息、尊重因果性
- pandas/xarray 访问器，一行式 .stream(…).apply(…) 调用 JAX 函数
- 为 JAX 补充 datetime64 与 string_ dtype 支持（编码方案）

## 适用场景

- 在 pandas/xarray 工作流中直接使用 JAX 生态的时间序列算法
- 同步并处理多个不同采样频率的传感器/观测数据流
- 以 Gym 风格反馈循环实现与测试在线学习和强化学习算法

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L21: WAX-ML is a research-oriented Python library
> L50: For now, WAX-ML focuses on **time-series** algorithms as this is one of the areas of machine learning

## 星数曲线

```mermaid
xychart-beta
    title "eserie/wax-ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-31 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `27b81415e664` · [字段定义](../../DATASET.md)*
