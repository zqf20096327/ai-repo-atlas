# oneir0mancer/stable-diffusion-diffusers-colab-ui

⭐ 21 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/oneir0mancer/stable-diffusion-diffusers-colab-ui) · 个人维护

**在 Google Colab 用 IPython widgets 跑 Stable Diffusion 的 UI**

基于 🤗 diffusers 库的 Colab 笔记本 UI，用原生 Colab 与 IPython widgets 构建图形界面，从而不依赖 gradio WebUI（README 称 gradio 现在在 Colab 上被禁止）。功能包括加载 HuggingFace 模型与 Automatic1111 格式（ckpt/safetensors）模型、更换 VAE 与采样器、加载 textual inversion 与 LoRA、img2img 与 inpainting；支持 SD 1.x/2.x/XL 与 Kandinsky 的 txt2img 和图像混合。限制：SDXL 下加载 A1111 格式可能因内存不足失败，textual inversion 与 LoRA 暂不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 IPython widgets 的原生 Colab UI，不依赖 gradio
- 支持 SD 1.x/2.x/XL 及 Kandinsky txt2img 与图像混合
- 可加载 HuggingFace 模型与 A1111 格式（ckpt/safetensors）
- 支持 VAE/采样器更换、textual inversion、LoRA、img2img、inpainting

## 适用场景

- 在 Colab 上以图形界面运行 Stable Diffusion 而不装 gradio
- 用 Kandinsky 做文生图与图像混合
- 在 Colab 环境加载本地 A1111 格式模型生成图像

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: Colab UI for running Stable Diffusion with 🤗 diffusers library.
> L13:  - [X] UI based on IPython widgets

## 星数曲线

```mermaid
xychart-beta
    title "oneir0mancer/stable-diffusion-diffusers-colab-ui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f3e39c5bc351` · [字段定义](../../DATASET.md)*
