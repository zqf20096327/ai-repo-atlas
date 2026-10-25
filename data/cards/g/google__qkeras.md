# google/qkeras

⭐ 584 · Python · Apache-2.0 · 推送 2026-02-23 · [GitHub](https://github.com/google/qkeras) · 组织维护

**面向 TensorFlow Keras 的深度神经网络量化扩展库**

QKeras 由 Google 维护，是 Keras 的量化扩展：提供 QDense、QConv2D 等可直接替换 Keras 原生层的量化层，以及 binary/ternary/quantized_bits 等多种量化激活函数，用于构建低比特量化神经网络。用户将 Dense、Conv2D 等层替换为对应的 Q 层即可得到量化版本网络。附带 QTools（生成每层数据类型映射、估算模型能耗，单位 pJ，基于 45nm 工艺数据）与 AutoQKeras（借助 Keras-Tuner 将量化与再平衡作为超参数搜索，支持随机搜索、hyperband、高斯过程）。部分层（如 QBatchNormalization）仍处实验阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 提供 QDense/QConv2D/QSeparableConv2D/QLSTM 等 Keras 层的量化替换层
- 支持 binary/ternary/stochastic/quantized_bits 等多种量化激活函数
- QTools 生成数据类型映射并按 pJ 估算模型能耗（45nm 基准）
- AutoQKeras 基于 Keras-Tuner 自动搜索量化配置与再平衡

## 适用场景

- 把现有 Keras 模型改写为低比特量化网络用于边缘/FPGA 部署
- 估算量化模型各层数据类型与内存/MAC 能耗
- 自动搜索满足精度与能耗权衡的量化方案

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L7: QKeras is a quantization extension to Keras that provides drop-in
> L32: QKeras is being designed to extend the functionality of Keras using

## 星数曲线

```mermaid
xychart-beta
    title "google/qkeras 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 583 --> 585
    line [584, 584]
```

2026-10-18 584 → 2026-10-25 584（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `28e579fc401f` · [字段定义](../../DATASET.md)*
