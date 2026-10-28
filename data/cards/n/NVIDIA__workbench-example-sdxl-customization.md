# NVIDIA/workbench-example-sdxl-customization

⭐ 65 · Python · Apache-2.0 · 推送 2025-11-04 · [GitHub](https://github.com/NVIDIA/workbench-example-sdxl-customization) · 组织维护

**AI Workbench 示例工程：用 DreamBooth 微调 SDXL 生成自定义图像**

NVIDIA 官方 AI Workbench 示例工程，演示如何基于 Hugging Face Stable Diffusion XL 与 DreamBooth 方法，用少量照片（示例为 Toy Jensen）微调模型，使其生成包含特定人物的新图像；用户也可导入自己的图像数据微调。工程以 Notebook（FineTuning-SDXL.ipynb）形式提供，需先安装 NVIDIA AI Workbench，通过 nvwb 命令克隆并打开。系统要求 Ubuntu 22.04、NVIDIA 训练 GPU（测试于 A100-80GB 与 RTX A6000）、40GB 存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 SDXL 与 DreamBooth 的少样本图像微调流程
- 支持导入用户自己的图像数据集进行微调
- 以 JupyterLab Notebook 形式在 AI Workbench 内运行
- Apache 2.0 许可

## 适用场景

- 学习如何在 AI Workbench 中微调 SDXL 模型
- 用自己的人物照片微调模型生成定制图像
- 作为 AI Workbench 工程结构与工作流的参考模板

## 场景标签

`微调` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L2: This is an NVIDIA AI Workbench example Project that demonstrates how to customize a Stable Diffusion XL (SDXL) model
> L11: From there, you'll see how you can fine-tune the model using DreamBooth. We'll use a small number of photos of Toy 

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/workbench-example-sdxl-customization 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-28 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `896fd70c0b69` · [字段定义](../../DATASET.md)*
