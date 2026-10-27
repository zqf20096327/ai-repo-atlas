# uakarsh/latr

⭐ 56 · Python · MIT · 推送 2026-07-22 · [GitHub](https://github.com/uakarsh/latr) · [官网](https://uakarsh.github.io/latr/) · 个人维护

**LaTr 论文的社区 PyTorch 复现：面向场景文本视觉问答**

对论文《LaTr: Layout-aware transformer for scene-text VQA》的非官方 PyTorch 实现（作者未放出官方代码）。LaTr 利用视觉 Transformer 免去外部目标检测器，提升对 OCR 错误的鲁棒性。本仓库提供基于 PyTorch Lightning 的预训练与训练脚本，验证精度 27.42%（论文为 44.03%）；维护者声明因资源限制未提供预训练权重，但提供 gdown 命令下载所用权重。安装依赖包括 transformers、pytesseract 与系统级 tesseract-ocr。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LaTr 架构的 PyTorch 实现，含预训练与 PyTorch Lightning 训练脚本
- 提供 gdown 命令下载实验所用权重
- 验证集精度 27.42%（论文报告 44.03%）已在 README 公示
- MIT 许可，附论文引用条目

## 适用场景

- 复现或研究场景文本视觉问答（STVQA）模型
- 基于代码进一步训练 LaTr 并产出预训练权重
- 学习布局感知 Transformer 的实现方式

## 场景标签

`OCR` `模型训练` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L5: Implementation of LaTr: Layout-aware transformer for scene-text VQA,a novel multimodal architecture for Scene Text V
> L7: LaTr improves robustness towards OCR errors, a common reason for failure cases in STVQA. In addition, by leveraging 

## 星数曲线

```mermaid
xychart-beta
    title "uakarsh/latr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-27 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1e0983bd198a` · [字段定义](../../DATASET.md)*
