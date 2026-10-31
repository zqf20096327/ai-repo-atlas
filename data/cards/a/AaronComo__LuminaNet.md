# AaronComo/LuminaNet

⭐ 16 · HTML · NOASSERTION · 推送 2026-01-26 · [GitHub](https://github.com/AaronComo/LuminaNet) · 组织维护

**论文官方仓库：类脑神经网络 LuminaNet 的模型实现**

论文《Rethinking Intelligence: Brain-like Neuron Network》的官方代码库，提出类脑神经网络范式 BNN 并给出首个实例 LuminaNet：不使用卷积或自注意力，可自主修改自身架构并通过动态结构变化实现自进化。README 提供图像识别（CIFAR-10）与文本生成（TinyStories）任务的交互式结构可视化、测试脚本运行方式（conda 环境 + pip 依赖），训练代码标注为即将发布。许可限研究与非商业用途，商业使用需另行获取授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无卷积、无自注意力的网络结构，可自主修改架构
- 通过动态架构变化实现自进化（论文实验）
- 覆盖 CIFAR-10 图像识别与 TinyStories 文本生成两个任务
- 提供不同 d_hidden 规模的交互式结构可视化

## 适用场景

- 复现论文中的 CIFAR-10/TinyStories 实验
- 研究无卷积/无注意力机制的网络范式
- 查看不同规模下 LuminaNet 的结构演化结果

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: > From the perspective of neuroscience, we rethink the formation and evolution of intelligence and proposes a new ne
> L43: python test_<cifar10/tinystories>.py

## 星数曲线

```mermaid
xychart-beta
    title "AaronComo/LuminaNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b96ea1167748` · [字段定义](../../DATASET.md)*
