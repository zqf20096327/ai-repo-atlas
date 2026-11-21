# vitali-sialedchyk/stability-first-ai

⭐ 10 · Python · NOASSERTION · 推送 2026-01-11 · [GitHub](https://github.com/vitali-sialedchyk/stability-first-ai) · [官网](https://recursive-time.com/) · 个人维护

**研究持续性学习与遗忘恢复的实验代码集合**

作者 Vitali Sialedchyk 的一系列神经网络记忆与灾难性遗忘实验，围绕 Recursive Time、Active Sleep（生成式回放）、Temporal LoRA 等机制展开，含 8 个子项目（MNIST/GPT-2/CIFAR-10/ImageNet/Mistral-7B）。README 给出 Quick Start 运行 GPT-2 Temporal LoRA 实验的步骤，依赖 torch/transformers 等 Python 库。采用 CC BY-NC 4.0 许可，商用需另行联系作者获取商业授权。

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

- Temporal LoRA：GPT-2 与 Mistral-7B 上的时间模块路由实验
- Lazarus Project：无训练数据条件下从噪声损伤与剪枝中恢复精度
- Project 10：基于递归深度停止准则，声称 5-7x 加速
- 提供完整 bibtex 引用与 DOI 标注

## 适用场景

- 复现生成式回放与持续学习实验
- 研究 LoRA 适配器的动态切换机制
- 实验受损模型的零数据恢复流程

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: A collection of experiments exploring memory, catastrophic forgetting, and temporal modularity in neural networks.
> L63: If you want to run just one experiment, choose **Temporal LoRA**. It demonstrates dynamic context switching in GPT-

## 星数曲线

```mermaid
xychart-beta
    title "vitali-sialedchyk/stability-first-ai 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-19 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `718007914df9` · [字段定义](../../DATASET.md)*
