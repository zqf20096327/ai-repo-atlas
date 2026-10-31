# Phoenix-dev11/Virtual_Try_Off

⭐ 25 · Python · NOASSERTION · 推送 2026-08-19 · [GitHub](https://github.com/Phoenix-dev11/Virtual_Try_Off) · 个人维护

**虚拟试穿/试脱工具包：从图像生成试穿图与服装分割标注**

TEMU-VTOFF 是面向时尚图像的虚拟试穿（Try-On）与理解工具包，包含三个核心组件：基于 Stable Diffusion 3 的推理管线生成试穿图像、基于 Qwen2.5-VL 的服装属性结构化描述生成、基于 SegFormer（mattmdjaga/segformer_b2_clothes）的服装二值/精细分割。支持 DressCode 与 VITON-HD 数据集，可单图或批量处理。安装方式为 git clone 源码加 pip install -r requirements.txt，需自行准备预训练模型路径或 HuggingFace 模型 ID。

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

- Stable Diffusion 3 管线生成虚拟试穿图像
- Qwen2.5-VL 生成服装属性结构化描述（类型/版型/领口等）
- SegFormer 服装分割输出二值掩码与精细掩码
- 支持 DressCode 与 VITON-HD 数据集的单图/批处理

## 适用场景

- 从服装平铺图生成模特试穿效果图
- 批量生成服装属性描述用于数据集预处理
- 提取服装区域掩码用于电商图像处理

## 场景标签

`图像生成` `目标检测` · 领域:内容生成

## 证据(README 行号)

> L8: - **Virtual Try-On**: Generate realistic try-on images using Stable Diffusion 3-based pipelines.
> L9: - **Visual Attribute Captioning**: Extract fine-grained garment attributes using Qwen-VL.
> L10: - **Clothing Segmentation**: Obtain binary and fine masks for garments using SegFormer.
> L68: - **Purpose**: Generates virtual try-on images using a Stable Diffusion 3-based pipeline.

## 星数曲线

```mermaid
xychart-beta
    title "Phoenix-dev11/Virtual_Try_Off 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `ae117d5e733d` · [字段定义](../../DATASET.md)*
