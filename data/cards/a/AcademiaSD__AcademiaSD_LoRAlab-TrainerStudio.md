# AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio

⭐ 160 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio) · 组织维护

**低显存 GPU 上为多种图像/视频模型训练 LoRA 的工作室**

面向 4–8 GB VRAM 的 NVIDIA GPU 的 LoRA 训练工具：一次安装、一个启动器，提供 Qwen-Image 2.1、FLUX.2 Klein 9B、LTX 2.5、SDXL（Pony/Illustrious/NoobAI）等多个模型的专属训练器，采用 NF4 量化模型并支持 block swap 与 VRAM Profile 降低显存峰值。内置数据集分析、BiRefNet 掩码损失、训练前设置助手、自动挑选最佳 checkpoint、XY 网格预览。支持 Windows、Linux 与 RunPod，产物可在 ComfyUI 中加载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NF4 量化加 block swap/VRAM Profile，支持 4–8 GB VRAM 训练
- 覆盖图像、视频、音视频与编辑（IC-LoRA）多类 LoRA 训练器
- 数据集分析器检查重复/模糊/缺 caption 等问题并一键修复
- 训练结束自动测试 checkpoint 并输出推荐的最佳 LoRA 文件

## 适用场景

- 在消费级低显存显卡上训练人物或风格的 LoRA
- 为 LTX 视频模型训练带音频预览的 LoRA
- 用数据集分析器清理训练图片与 caption

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L34: - **Krea 2 from 8 GB of VRAM** — the block swap and **VRAM Profile** of FLUX.1 and Klein 9B. At 1024² Krea 2 peaked
> L50: - NEW TRAINER **LTX 2.5: image, video, video + audio and edit (IC-LoRA) LoRAs, from 8 GB of VRAM** — images, clips 

## 星数曲线

```mermaid
xychart-beta
    title "AcademiaSD/AcademiaSD_LoRAlab-TrainerStudio 星数(近 22 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-28"]
    y-axis "stars" 108 --> 164
    line [112, 114, 116, 121, 124, 125, 127, 129, 112, 139, 143, 145, 147, 150, 151, 152, 153, 154, 156, 157, 158, 160]
```

2026-10-26 112 → 2026-11-28 160（+48）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `284d52310ef9` · [字段定义](../../DATASET.md)*
