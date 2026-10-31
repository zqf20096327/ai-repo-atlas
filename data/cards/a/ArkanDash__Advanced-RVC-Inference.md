# ArkanDash/Advanced-RVC-Inference

⭐ 91 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/ArkanDash/Advanced-RVC-Inference) · 个人维护

**RVC 语音转换的 Web UI：模型下载、推理、训练与实时变声**

基于 Retrieval-based Voice Conversion 的推理工具，提供 Gradio Web UI 与 CLI 两种使用方式：支持从 HuggingFace 等下载 RVC 模型、音轨分离、批量推理、训练流水线与实时变声。训练环节支持 HiFi-GAN NSF、BigVGAN 等 4 种声码器和 AdamW、Prodigy 等 8 种优化器。安装方式为 git clone + pip 安装或直接从 PyPI 安装，支持 CUDA 与 ZLUDA（AMD GPU），另提供 Google Colab 笔记本。使用条款禁止出售语音模型及冒充原声等用途。

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

- Web UI（rvc-gui）与 CLI（rvc-cli）双入口，含批量推理与实时转换
- 内置训练流水线，支持 4 种声码器与 8 种优化器
- 支持 CUDA 与 ZLUDA（AMD GPU 自动检测）
- 提供 Google Colab 笔记本（完整 UI 与轻量 CLI 两种）

## 适用场景

- 下载 RVC 模型并批量转换语音
- 在本地或 Colab 上训练自己的 RVC 语音模型
- 实时变声与音轨分离

## 场景标签

 · 领域:语音转换/音频 AI

## 证据(README 行号)

> L3: **A state-of-the-art web UI crafted to streamline rapid and effortless RVC inference — featuring a model downloader,
> L82: # Voice conversion
> L83: rvc-cli infer -m model.pth -i input.wav -o output.wav

## 星数曲线

```mermaid
xychart-beta
    title "ArkanDash/Advanced-RVC-Inference 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27", "2026-10-31"]
    y-axis "stars" 88 --> 92
    line [89, 90, 91, 91]
```

2026-10-18 89 → 2026-10-31 91（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b1bfa069e8b9` · [字段定义](../../DATASET.md)*
