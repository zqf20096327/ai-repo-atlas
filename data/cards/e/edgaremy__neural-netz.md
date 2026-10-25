# edgaremy/neural-netz

⭐ 83 · Typst · MIT-0 · 推送 2025-12-08 · [GitHub](https://github.com/edgaremy/neural-netz) · [官网](https://typst.app/universe/package/neural-netz) · 个人维护

**Typst 包：绘制高质量神经网络架构示意图**

基于 Typst 的神经网络架构可视化包，提供单一 draw-network 函数，底层仅依赖 Typst 原生 CeTZ 绘图包。支持预定义层类型（input/conv/convres 等，含 warm/cold 两种配色）、自定义层、维度标注、智能图例、缩放控制以及层间额外连接（按 name 引用）。附 ResNet18、U-Net、FCN-8 等示例代码。风格与 API 参考 PlotNeuralNet（Python+LaTeX），作者为个人，发布于 HAL 并可引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 draw-network 函数绘制多层网络图，仅依赖 CeTZ
- 预定义层类型与可定制的 custom 层（支持多通道与激活带填充）
- 智能图例、scale 缩放与命名层间额外连接
- 提供 ResNet18/U-Net/FCN-8 完整示例代码

## 适用场景

- 在 Typst 论文或报告中插入神经网络架构图
- 复用现成架构示例（ResNet18、U-Net）快速出图
- 用 custom 层自定义不属于预定义类型的网络模块

## 场景标签

 · 领域:科学可视化/深度学习

## 证据(README 行号)

> L3: Visualize Neural Network Architectures in high-quality diagrams using Typst, with style and API inspired by PlotNeur
> L13: Under the hood, this package only uses the native Typst package CeTZ for building the diagrams.

## 星数曲线

```mermaid
xychart-beta
    title "edgaremy/neural-netz 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 81 --> 84
    line [82, 83, 83]
```

2026-10-18 82 → 2026-10-25 83（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `94c44f99d1bb` · [字段定义](../../DATASET.md)*
