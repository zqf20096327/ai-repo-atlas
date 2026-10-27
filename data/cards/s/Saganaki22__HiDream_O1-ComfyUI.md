# Saganaki22/HiDream_O1-ComfyUI

⭐ 69 · Python · MIT · 推送 2026-05-15 · [GitHub](https://github.com/Saganaki22/HiDream_O1-ComfyUI) · [官网](https://github.com/HiDream-ai/HiDream-O1-Image) · 个人维护 · 中文 README

**在 ComfyUI 中本地运行 HiDream O1 图像生成与 LoRA 训练的节点集**

为 ComfyUI 提供的 HiDream O1 图像生成自定义节点集：模型加载器支持 BF16/FP16/FP32/FP8 精度与 FlashAttention/SageAttention/SDPA 注意力后端；采样器支持纯文本与最多 12 张参考图输入、布局条件、进度预览；附带 Dev 模型 patch-grid 平滑节点与 AI Toolkit 对齐的实验性文生图 LoRA 训练节点（数据集制作→训练配置→训练）。模型需自行下载放置到 diffusion_models 目录（FP8 约 10–11 GB 显存，BF16 约 18–20 GB），可通过 ComfyUI Manager 或手动 git clone 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 BF16/FP16/FP32/FP8 E4M3FN/E5M2 精度与三种注意力后端
- 采样器支持纯文本与最多 12 张参考图、JSON bbox 布局条件、进度预览
- Dev 模型 patch-grid 平滑节点用于减少可见拼接缝
- AI Toolkit 对齐的实验性文生图 LoRA 训练节点

## 适用场景

- 在 ComfyUI 工作流中本地生成或编辑 HiDream O1 图像
- 用自有图片/标注数据集训练 HiDream O1 的 LoRA
- 低显存环境（约 10–11 GB）通过 FP8 精度运行模型

## 场景标签

`图像生成` `微调` · 领域:内容生成

## 证据(README 行号)

> L3: **HiDream O1 Image nodes for ComfyUI** — local HiDream O1 generation with text prompts, optional reference images, B
> L14: - HiDream O1 Image generation directly inside ComfyUI
> L174: Experimental text-to-image LoRA training is available directly inside ComfyUI:

## 星数曲线

```mermaid
xychart-beta
    title "Saganaki22/HiDream_O1-ComfyUI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-27 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `bd1d60e376a6` · [字段定义](../../DATASET.md)*
