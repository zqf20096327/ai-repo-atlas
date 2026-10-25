# Fr0zenCrane/Uni-ViGU

⭐ 35 · Python · Apache-2.0 · 推送 2026-04-15 · [GitHub](https://github.com/Fr0zenCrane/Uni-ViGU) · 组织维护

**统一视频生成与理解的研究框架，基于扩散视频生成器**

以视频生成器为基础扩展出理解能力的研究框架：提出统一流方法（视频连续流匹配+文本离散流匹配）、模态驱动的 MoE 结构增强文本生成，以及两阶段双向训练机制（Knowledge Recall 重建输入提示、Capability Refinement 在详细字幕上微调）。基于 Diffusers 与 Flow Matching 代码库构建，推理依赖 Uni-ViGU 与 Wan2.1 1.3B 检查点，通过 conda 环境、源码安装 flow_matching 并 pip 安装依赖后运行 run.sh。附 arXiv 论文。

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

- 统一流方法：单过程中视频连续流匹配与文本离散流匹配
- 模态驱动 MoE 结构：轻量层增强 Transformer 块的文本生成
- 两阶段双向训练：Knowledge Recall 与 Capability Refinement
- 基于 Diffusers 与 facebookresearch/flow_matching 构建

## 适用场景

- 研究生成中心架构下的统一多模态视频生成与理解
- 复现论文中的视频生成与理解实验
- 作为视频扩散模型的训练/推理代码基础

## 场景标签

`视频生成` `多模态` · 领域:内容生成

## 证据(README 行号)

> L3: Unified multimodal models integrating visual understanding and generation face a fundamental challenge: visual gener
> L5: We introduce a **unified flow method** that performs continuous flow matching for video and discrete flow matching f

## 星数曲线

```mermaid
xychart-beta
    title "Fr0zenCrane/Uni-ViGU 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-25 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `31b8e47adaed` · [字段定义](../../DATASET.md)*
