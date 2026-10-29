# google-deepmind/fusion_surrogates

⭐ 44 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/google-deepmind/fusion_surrogates) · 组织维护

**托卡马克聚变模拟的输运替代模型库（含权重与推理代码）**

提供托卡马克聚变湍流输运的神经网络替代模型，含推理代码、模型权重与元数据，主要为 TORAX 模拟器设计，也可供其他聚变模拟器使用。当前收录 QLKNN_7_11 模型，它是 Qualikiz 准线性回旋动理学程序的替代，基于 Van de Plassche 等的 QLKNN10D 模型，用 QLKNN11D 与 QLKNN7D-edge 数据训练。输入归一化梯度、安全因子、磁剪切等 8 个局部等离子体参数，输出 ITG/ETG/TEM 各输运模式的离子与电子热流和粒子通量及最大增长率。以 pip 安装的 Python 库形式提供。模型细节论文尚未发布。

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

- 提供推理代码、模型权重与元数据三部分
- QLKNN_7_11 为 Qualikiz 准线性回旋动理学程序的替代模型
- 输出 ITG/ETG/TEM 各模式的离子/电子热流、粒子通量与离子尺度最大增长率
- 软件 Apache 2.0、其他材料 CC-BY 双许可条款

## 适用场景

- 在 TORAX 聚变模拟中以神经网络替代 Qualikiz 加速输运计算
- 其他聚变模拟器复用 QLKNN_7_11 替代模型
- 聚变等离子体湍流输运研究中的快速通量预测

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: This library provides both inference code and model weights and metadata. It is
> L11: Currently, this library only holds the QLKNN_7_11 model. This model is a
> L34: It outputs ion and electron heat and particle fluxes for each transport mode

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/fusion_surrogates 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `14e7c5db701d` · [字段定义](../../DATASET.md)*
