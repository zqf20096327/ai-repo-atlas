# neuralnet-cpp-dev/neuralnet.cpp

⭐ 16 · C++ · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/neuralnet-cpp-dev/neuralnet.cpp) · 个人维护 · 中文 README

**从零实现的 C++26 神经网络库：CPU/GPU 双后端训练推理**

LGPL-3.0 许可的 C++ 神经网络框架，以 nn:: 命名空间提供矩阵、层（Linear/Attention/LayerNorm 等）、损失、优化器（SGD/Adam/AdamW/Muon）组件，支持 MLP/Transformer/CNN 架构，可训练 MNIST 分类与 GPT 语言模型并推理。GPU 后端基于 Vulkan 计算着色器，支持 f16/混合精度与多精度类型系统。另带 CustomTkinter GUI 覆盖训练/推理/分词器操作，以及 BPE 分词器、.nnpkg 训练包、REINFORCE/PPO/GRPO 强化学习组件。需 C++26 编译器与 CMake 从源码构建，部分代码由 AI 工具辅助生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CPU/Vulkan GPU 双后端，支持多层 Transformer 与 GPT 训练推理
- f16/混合精度、RLA/RAPT 线性注意力、算子融合等机制
- CustomTkinter GUI 覆盖 MNIST/GPT 训练推理与手写板识别
- 提供 REINFORCE/PPO/GRPO 强化学习与 BPE 分词器组件

## 适用场景

- 从源码层面理解神经网络训练、推理与部署流程
- 在嵌入式或资源受限场景运行轻量级模型训练与推理
- 用自己的语料训练小型 GPT 语言模型并多轮对话生成文本

## 场景标签

`模型训练` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: 一个从零实现的 C++26 神经网络库，支持 CPU/GPU 双后端、多层 Transformer、GPT 语言模型训练与推理。
> L105: # 从头开始训练 MLP（默认: 10轮, 学习率0.001, 批大小64, Adam优化器）
> L141: |💬 **GPT 推理**|GPT 文本生成：温度 / top-k / top-p / 重复惩罚 / 种子、**多轮对话（上下文不丢）**、单次生成、Token ID 调试输出|

## 星数曲线

```mermaid
xychart-beta
    title "neuralnet-cpp-dev/neuralnet.cpp 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-26 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `96bbeca397fb` · [字段定义](../../DATASET.md)*
