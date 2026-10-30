# ScottT2-spec/mnist-neural-network-

⭐ 16 · Python · MIT · 推送 2026-03-13 · [GitHub](https://github.com/ScottT2-spec/mnist-neural-network-) · [官网](https://www.kaggle.com/scottantwi) · 个人维护

**NumPy 手写神经网络识别手写数字的学习项目与 Kaggle 参赛方案**

两部分组成：其一为仅用 Python 与 NumPy 从零实现的神经网络（784-64-10 结构，sigmoid 激活，反向传播，批大小 64，测试准确率 95.75%），不使用任何深度学习框架，用于理解神经网络原理；其二为 Kaggle Digit Recognizer 参赛方案（99.685% 准确率），采用 5 个 CNN 架构集成（ResNet、SE-Net 等）、数据增强、TTA、伪标签与标签平滑，基于 TensorFlow/Keras。从零版本可在 Colab/Jupyter 约 2 分钟训练，参赛版本需 Kaggle GPU T4 x2 约 2-3 小时。另附分步教学指南 GUIDE.md。

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

- 从零版本仅依赖 Python + NumPy，无任何深度学习框架
- Kaggle 参赛版本 5 种 CNN 架构集成达 99.685% 准确率
- 配套分步教学指南 GUIDE.md（NumPy 基础到从零构建网络）
- 含预测示例与混淆矩阵可视化

## 适用场景

- 通过从零实现理解前向/反向传播的数学原理
- 在 Colab 或 Jupyter 中快速复现手写数字识别
- 参考 Kaggle 参赛技巧（集成、增强、TTA、伪标签）

## 场景标签

`教程课程` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L7: A neural network that recognizes handwritten digits (0-9), built using only Python and NumPy. No TensorFlow, no PyTo
> L14: The network learns through backpropagation — it makes a prediction, checks how wrong it was, then adjusts its weigh

## 星数曲线

```mermaid
xychart-beta
    title "ScottT2-spec/mnist-neural-network- 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ebf7b3453b7a` · [字段定义](../../DATASET.md)*
