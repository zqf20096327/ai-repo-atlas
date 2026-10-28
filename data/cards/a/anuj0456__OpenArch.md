# anuj0456/OpenArch

⭐ 426 · Python · MIT · 推送 2026-09-30 · [GitHub](https://github.com/anuj0456/OpenArch) · 个人维护

**面向学习者的现代 LLM 架构从零 PyTorch 实现集合**

逐一用单个可读的 PyTorch 文件从零实现主流开源 LLM 架构（Llama、Qwen、DeepSeek R1、Gemma、GPT-OSS、Kimi K2 等 16 个已完成、3 个在建），每模型附 README 说明注意力类型、归一化、位置编码与 MoE 路由等结构选择，便于并排比较。目标明确为教学而非生产，README 声称不与 transformers 竞争；完整实现计划对应 Architecture Gallery 的 103 个架构。Apache 2.0 许可，各模型实现遵循原模型许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 16 个架构可运行 forward pass（文本/多模态/图像）
- 每架构单一文件实现，结构选择显式可对比
- 覆盖 MLA、MoE 路由、Multi-Token Prediction、滑动窗口等机制
- 完整目标清单对应 103 个架构，接受社区贡献

## 适用场景

- 对照阅读不同 LLM 架构在注意力与归一化上的差异
- 基于原论文与技术报告学习模型结构实现
- 作为教学参考实现用于深度学习课程或自学

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: This repository contains hand-written PyTorch implementations of the model architectures cataloged in Sebastian Rasc
> L7: The goal is not to compete with `transformers` or other production libraries. The goal is **clarity and learning**: 

## 星数曲线

```mermaid
xychart-beta
    title "anuj0456/OpenArch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 425 --> 427
    line [426, 426]
```

2026-10-18 426 → 2026-10-28 426（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5bb886464b5c` · [字段定义](../../DATASET.md)*
