# Aatricks/LightDiffusion-Next

⭐ 51 · Python · GPL-3.0 · 推送 2026-04-29 · [GitHub](https://github.com/Aatricks/LightDiffusion-Next) · [官网](https://aatricks.github.io/LightDiffusion-Next/) · 组织维护

**面向创作者的 AI 图像生成 WebUI，主打性能优化**

基于 PyTorch 的 AI 图像生成 WebUI（含 FastAPI 后端与 React 前端），支持文生图、图生图、放大、LoRA/Textual Inversion、Hires-Fix、ADetailer 与 Flux2 Klein 模型。内置 Xformers、BFloat16、Stable-Fast 编译、SageAttention/SpargeAttn 等加速路径，README 声称可在低至 2GB 显存或无 GPU 的设备上运行，另带 Ollama 提示词增强、Discord 集成与 ZeroGPU/Gradio 入口。安装途径包括下载 release、pip 安装依赖与 Docker 部署（Docker 构建要求 NVIDIA GPU compute 8.0+ 与 CUDA 12.0+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文生图/图生图、放大、LoRA 与 Textual Inversion 支持
- 多种加速路径：Xformers、Stable-Fast、SageAttention、SpargeAttn、AYS 调度器
- 可在 2GB 显存或无 GPU 设备上运行
- Ollama 提示词增强（默认 qwen3:0.6b）与 ZeroGPU/Gradio 入口

## 适用场景

- 本地运行 SD1.5/Flux 模型生成和编辑图像
- 低显存设备上进行图像生成
- 通过 Docker 在自有 GPU 服务器上部署生成服务

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L27: **LightDiffusion-Next** offers a powerful suite of tools to cater to creators at every level. At its core, it suppo
> L31: **LightDiffusion-Next** is fine-tuned for **performance**. Features such as **Xformers** acceleration, **BFloat16**

## 星数曲线

```mermaid
xychart-beta
    title "Aatricks/LightDiffusion-Next 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-26 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9a0e7511a5f5` · [字段定义](../../DATASET.md)*
