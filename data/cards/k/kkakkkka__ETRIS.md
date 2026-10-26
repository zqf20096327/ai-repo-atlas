# kkakkkka/ETRIS

⭐ 147 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/kkakkkka/ETRIS) · 个人维护

**ICCV 2023 论文 ETRIS 官方实现：指代图像分割的参数高效微调**

Bridging Vision and Language Encoders 一文（ICCV 2023）的官方 PyTorch 代码，任务为指代图像分割（referring image segmentation）：给定自然语言描述在图像中分割对应目标。方法上冻结预训练的视觉与语言编码器（CLIP 风格 ResNet/ViT 权重），进行参数高效微调，代码基于 CRIS 实现。面向复现论文实验的科研用户：安装指定版本 PyTorch 与依赖、下载数据集与预训练权重后，通过 bash 脚本训练/评测，模型权重发布于 Huggingface。README 提及后续工作 DETRIS（AAAI 2025）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 指代图像分割的参数高效微调实现（冻结视觉/语言编码器）
- 提供训练、评测与可视化脚本，支持多 GPU 训练
- 模型权重开源发布于 Huggingface
- 基于 CRIS 代码实现

## 适用场景

- 复现 ICCV 2023 论文的训练与评测结果
- 在 RefCOCO 等数据集上做指代图像分割实验
- 作为参数高效多模态微调的参考实现

## 场景标签

`科研工具` `微调` `目标检测` `多模态` · 领域:学习与行业

## 证据(README 行号)

> L3: This is an official PyTorch implementation of Bridging Vision and Language Encoders: Parameter-Efficient Tuning for 
> L42: bash run_scripts/train.sh
> L50: bash run_scripts/test.sh

## 星数曲线

```mermaid
xychart-beta
    title "kkakkkka/ETRIS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 146 --> 148
    line [147, 147]
```

2026-10-18 147 → 2026-10-26 147（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f496b16d1a23` · [字段定义](../../DATASET.md)*
