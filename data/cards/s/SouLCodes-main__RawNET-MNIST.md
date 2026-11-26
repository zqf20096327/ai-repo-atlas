# SouLCodes-main/RawNET-MNIST

⭐ 3 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/SouLCodes-main/RawNET-MNIST) · 个人维护

**纯 NumPy 从零实现的手写数字分类神经网络**

教育导向的前馈神经网络完整实现：仅用 NumPy 完成前向/反向传播，自建数学引擎，含 He 初始化、ReLU/Softmax 激活、mini-batch 梯度下降与交叉熵损失，不依赖 PyTorch/TensorFlow 自动微分。支持动态配置任意层数结构（如 [784,128,64,10]），训练后权重以 .npy 序列化保存，并通过本地 Gradio 网页画布实时绘制数字测试推理。面向学习深度学习原理的用户，需 Python 3.13+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 NumPy 从零实现，无 PyTorch/TensorFlow
- 动态 L 层架构，可配置任意层数与节点数
- Gradio 本地网页画布实时推理测试
- 权重序列化为 .npy 文件，UI 免重训加载

## 适用场景

- 理解神经网络前向/反向传播的底层机制
- 实验不同网络深度对手写数字识别准确率的影响
- 学习 NumPy 向量化与梯度状态管理实践

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A pure-NumPy, functional-style neural network built entirely from scratch to classify handwritten digits. This proje
> L16: RawNET-MNIST is an educational project that dives deep into the fundamental principles of neural networks. It is a 
> L18: Originally built as a 2-layer network, it has been engineered into a **Dynamic L-Layer Architecture**, capable of g

## 星数曲线

```mermaid
xychart-beta
    title "SouLCodes-main/RawNET-MNIST 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-24 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `98a23390c286` · [字段定义](../../DATASET.md)*
