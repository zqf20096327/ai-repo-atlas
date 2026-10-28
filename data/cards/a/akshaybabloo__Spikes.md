# akshaybabloo/Spikes

⭐ 23 · Python · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/akshaybabloo/Spikes) · [官网](https://akshaybabloo.github.io/Spikes/) · 个人维护

**面向 SNN 的时间序列脉冲编码库（TBR/BSA/SF 三种）**

Python 包 pyspikes，为脉冲神经网络提供时间序列到脉冲序列的编码：含 Threshold Based Representation、Bens Spiker Algorithm、Step Forward 三种编码器，读取 CSV 格式的时空数据（每列一特征、每行一时间点），示例使用 PhysioNet EEG 运动想象数据集（160Hz、14 通道）。BSA 与 Step Forward 在安装 Numba 时运行更快，脉冲结果不变。通过 pip 安装，面向构建 SNN 输入的研究者与开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TBR / BSA / Step Forward 三种脉冲编码算法
- 读取 CSV 时空数据（列为特征、行为时间点）
- 可选 Numba 加速（pip install pyspikes[numba]）
- 附 PhysioNet EEG 示例数据

## 适用场景

- 将 EEG 等传感时间序列编码为 SNN 可用的脉冲输入
- 对比不同脉冲编码算法对同一数据的输出
- 搭建脉冲神经网络数据预处理流水线

## 场景标签

 · 领域:机器学习/神经形态计算

## 证据(README 行号)

> L9: This package consists of three types of spike encoders for spatio-temporal data:
> L11: 1. Threshold Based Representation (TBR) encoder

## 星数曲线

```mermaid
xychart-beta
    title "akshaybabloo/Spikes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `af217d65bdca` · [字段定义](../../DATASET.md)*
