# Soumya-Chakraborty/VL-JEPA

⭐ 23 · Python · 推送 2026-02-20 · [GitHub](https://github.com/Soumya-Chakraborty/VL-JEPA) · 个人维护

**VL-JEPA 视觉-语言联合嵌入预测架构的论文复现实现**

对 arXiv:2512.10942v2 论文的完整实现：包含 X-Encoder、query 条件化 Predictor、Y-Encoder 构成的 VL-JEPA 模型，采用双向 InfoNCE 目标与两阶段训练流程（预训练+SFT），支持字幕生成、判别式 VQA、选择性解码及嵌入检索/分类。提供 CPU tiny 离线冒烟测试路径（无需下载外部模型）与 GPU/CUDA 路径，交互式 chat 的回复从提供的文本库中选取而非自由生成。面向运行视觉-语言表征学习实验的研究与开发人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- X-Encoder/条件化 Predictor/Y-Encoder 与双向 InfoNCE 训练目标
- 两阶段训练流程（预训练+SFT）及字幕生成/VQA/选择性解码推理
- CPU tiny 离线冒烟测试路径，无需外部模型下载
- 确定性训练（set_seed、deterministic 模式）与 YAML 配置、run 元数据记录

## 适用场景

- 复现论文中的 VL-JEPA 训练与推理流程
- 在自有图像/视频数据集上训练视觉-语言嵌入模型
- 通过嵌入相似度做检索、分类与判别式 VQA
- 离线小规模配置下验证端到端执行

## 场景标签

`模型训练` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository contains a full implementation of the architecture described in:
> L10: - Inference for captioning, discriminative VQA, and selective decoding
> L151: - Frozen visual encoder + trainable predictor + trainable text target encoder.

## 星数曲线

```mermaid
xychart-beta
    title "Soumya-Chakraborty/VL-JEPA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e01095a3c8c0` · [字段定义](../../DATASET.md)*
