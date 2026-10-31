# sayantan-2/comfyui_colab_Flux

⭐ 14 · Jupyter Notebook · 推送 2026-01-04 · [GitHub](https://github.com/sayantan-2/comfyui_colab_Flux) · 个人维护

**在 Google Colab 免费版上运行 ComfyUI/Flux 出图的笔记本**

提供单个 Google Colab notebook，在免费档（Tesla T4、约 15GB VRAM）上安装依赖并启动 ComfyUI，通过 LocalTunnel 暴露公开 URL 供网页访问。预配置 Flux 模型：FP8 版本默认可直接使用，Q5/Q4 GGUF 量化模型（来自 ComfyUI-GGUF 与 Hugging Face 仓库）用于支持 LoRA。面向想在免费 Colab 环境跑图像生成工作流的用户，一键打开 notebook 运行全部单元格即可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Colab 免费档（Tesla T4、<15GB VRAM）运行 ComfyUI
- Flux FP8 默认模型与 Q5/Q4 GGUF 量化模型支持 LoRA
- LocalTunnel 提供公开 URL 网页访问
- 模型下载在 notebook 内自动完成

## 适用场景

- 无本地 GPU 时在 Colab 免费额度内跑 Flux 图像生成
- 用量化 Flux 模型搭配 LoRA 出图
- 通过浏览器公开 URL 远程使用 ComfyUI

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: This repository provides a Google Colab notebook to run ComfyUI on the **free Google Colab tier** (under 15 GB VRAM)
> L12: - Runs **ComfyUI** seamlessly on Colab's free tier (Tesla T4 GPU).
> L37: 3. The notebook will start **ComfyUI** on a public URL using **LocalTunnel**.

## 星数曲线

```mermaid
xychart-beta
    title "sayantan-2/comfyui_colab_Flux 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a5711928d7b5` · [字段定义](../../DATASET.md)*
