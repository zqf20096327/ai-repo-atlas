# aimagelab/multimodal-garment-designer

⭐ 445 · Python · NOASSERTION · 推送 2026-10-12 · [GitHub](https://github.com/aimagelab/multimodal-garment-designer) · 组织维护

**论文官方代码：潜扩散模型做多模态条件时装图像编辑**

ICCV 2023 论文 Multimodal Garment Designer 的官方仓库：基于 latent diffusion 的架构，按文本、人体姿态、服装草图等多模态提示生成以人为中心的时装图像。提供推理脚本与 torch.hub 预训练模型（Dress Code / VITON-HD 两种 checkpoint），并发布了两个数据集的多模态标注扩展；训练代码列为 TODO 尚未放出。安装走 conda 环境 + pip 依赖（Python 3.9、torch 1.12.1、diffusers 0.12.0）。许可为 CC BY-NC 4.0，仅限非商业使用并需引用论文。

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

- 文本/姿态/草图多模态条件的人体时装图像编辑
- 预训练模型与去噪 UNet 经 torch.hub 提供
- Dress Code 与 VITON-HD 的多模态标注数据集扩展
- 内置少量示例图像（assets/data）可直接测试推理

## 适用场景

- 复现论文中的多模态时装图像编辑实验
- 在 Dress Code / VITON-HD 数据集上批量生成编辑图像
- 基于预训练 UNet 与 diffusers pipeline 构建自定义推理流程

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L15: This is the **official repository** for the **paper** "*Multimodal Garment Designer: Human-Centric Latent Diffusion
> L22: > Fashion illustration is used by designers to communicate their vision and to bring the design idea from conceptua
> L71: python src/eval.py --dataset_path <path> --batch_size <int> --mixed_precision fp16 --output_dir <path> --save_name 

## 星数曲线

```mermaid
xychart-beta
    title "aimagelab/multimodal-garment-designer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 444 --> 446
    line [445, 445]
```

2026-10-18 445 → 2026-10-24 445（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `9af74b76e4d1` · [字段定义](../../DATASET.md)*
