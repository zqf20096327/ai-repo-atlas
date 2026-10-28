# NikolasMarkou/dl_techniques

⭐ 26 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/NikolasMarkou/dl_techniques) · 组织维护

**Keras/TensorFlow 高级深度学习组件库：模型、层、损失与训练工具集**

基于 Keras 3 / TensorFlow 的深度学习组件库，由 Electi Consulting 赞助维护。收录 102 个模型包（12 个家族，覆盖 BERT、Qwen、CLIP、DINO、DETR、SAM、扩散模型、时间序列预测、GNN 等）、约 375 个层模块（注意力、MoE、RoPE 等配注册表工厂）、55 个损失函数、17 个优化器、模型分析套件（校准/权重/信息流/谱分析），以及约 70 个训练入口脚本和 1,558 模块的测试套件。面向用 Keras 构建与训练神经网络的研究者和工程师，以 Python 包形式通过 pip 安装。

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

- 102 个模型包（语言/视觉/多模态/时间序列/GNN），含 BERT、Qwen、CLIP、SAM 等 Keras 3 实现
- 约 375 个层模块，配注意力/归一化/FFN/激活等注册表工厂，可单行替换组件
- 55 个损失函数（含 AnyLoss：将混淆矩阵指标转为可微损失）与 17 个优化器
- ModelAnalyzer 五维分析（训练动态/权重健康/校准/信息流/谱分析）与 1,558 模块测试套件

## 适用场景

- 在 Keras 3 中直接复用论文架构而不必逐仓库收集实现
- 训练前用谱分析与权重分析评估模型泛化和健康度
- 在不平衡数据上用 AnyLoss 直接优化 F1 等指标

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L27: - **Next-Generation Language Models** (19 packages): Production-ready implementations of **`BERT`**, **`Gemma`**, *
> L38: - **Unified Factory Architecture**: A consistent, powerful factory system for creating and validating **35 attentio
> L71: * **Modern, Maintainable, and Future-Proof**: Built from the ground up for Keras 3 and modern Python, `dl_technique

## 星数曲线

```mermaid
xychart-beta
    title "NikolasMarkou/dl_techniques 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8b7dc87446c3` · [字段定义](../../DATASET.md)*
