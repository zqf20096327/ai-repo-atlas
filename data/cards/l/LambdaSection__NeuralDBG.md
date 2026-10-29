# LambdaSection/NeuralDBG

⭐ 25 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/LambdaSection/NeuralDBG) · [官网](https://lambdasection.github.io/NeuralDBG/) · 个人维护

**给深度学习研究者的 PyTorch 训练因果诊断库：定位训练失败根因**

以钩子嵌入 PyTorch 训练循环的诊断库：通过前向/反向钩子提取语义事件（梯度健康转变、激活状态偏移、优化器不稳定、数据异常 NaN/Inf/分布漂移），生成排序的因果假设，指明故障发生的层与步，覆盖 MLP/CNN/Transformer/RNN/GNN/MoE 等架构（自报 200 架构、1,200 注入验证）。运行本地，不做云端上报；兼容 torch.compile。限制：仅支持 PyTorch；高级因果推理属于专有许可的 Engine 版（pip 安装 neuraldbg-engine），Core 版 MIT。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 梯度/激活/优化器/数据四类故障的语义事件提取与排序因果假设
- 一行代码包装现有训练循环，无需改代码，兼容 torch.compile
- 本地运行，提供 JSON 诊断导出与零依赖 HTML 因果查看器
- 分 Core（MIT）与 Engine（专有许可）两版发布

## 适用场景

- 训练出现 NaN、梯度消失/爆炸时快速定位根因层与步
- 分析新型架构的学习动态与不稳定传播
- 研究/工程中替代人工曲线排查，自动获得修复方向假设

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: Training failed? NeuralDBG tells you **why**. It hooks into your PyTorch training loop, detects what went wrong (van
> L28: Unlike traditional monitoring tools (TensorBoard, Weights & Biases), NeuralDBG focuses on **causal inference** rath

## 星数曲线

```mermaid
xychart-beta
    title "LambdaSection/NeuralDBG 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-29 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `73d505bc93ce` · [字段定义](../../DATASET.md)*
