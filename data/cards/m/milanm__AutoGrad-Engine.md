# milanm/AutoGrad-Engine

⭐ 402 · C# · MIT · 推送 2026-10-24 · [GitHub](https://github.com/milanm/AutoGrad-Engine) · 个人维护

**约600行纯 C# 实现的 GPT 训练与生成教学项目**

Karpathy microgpt.py 的 C# 移植：零依赖实现标量自动微分引擎（Value.cs）、字符级分词器、Linear/Softmax/RMSNorm 算子与 GPT 模型、训练循环和自回归生成，共约 600 行代码分 4 个文件，附 25 个含数值梯度检查的测试。在人类名字数据集上训练微型模型并生成新名字。作者声明非生产代码、逐数字标量处理、CPU 即可分钟级跑完训练，定位为教学工具并配分步讲解与术语表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零依赖纯 C# 自动微分引擎与 GPT 完整训练/推理流程
- 采用 RMSNorm、无偏置、squared ReLU、pre-norm 等 LLaMA 式设计选择
- 25 个测试含数值梯度检查（同 torch.autograd.gradcheck 思路）
- CLI 可调层数、维度、注意力头数等超参数

## 适用场景

- 逐步理解 GPT 从分词到反向传播与生成的完整机制
- 在 .NET 环境中无需 PyTorch 学习自动微分实现
- 对照源码学习 KV 缓存、残差连接、权重绑定等概念

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: A complete GPT language model (training and inference) in pure C# with zero dependencies.
> L15: It trains a tiny GPT model on a list of human names, then generates new ones that sound real but never existed.

## 星数曲线

```mermaid
xychart-beta
    title "milanm/AutoGrad-Engine 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 400 --> 403
    line [401, 402, 402]
```

2026-10-18 401 → 2026-10-26 402（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `425a8bdc4d2d` · [字段定义](../../DATASET.md)*
