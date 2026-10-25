# hydropix/AutoDescribe-Images

⭐ 38 · Python · 推送 2025-12-14 · [GitHub](https://github.com/hydropix/AutoDescribe-Images) · 个人维护

**用 Ollama 视觉模型批量为图片生成描述文本的工具**

通过本地运行的 Ollama 视觉模型（Qwen3-VL、LLaVA、Llama Vision）为图片批量生成文字描述，以 Web 界面或 CLI 两种方式运行。面向 LoRA 训练数据集准备场景：为每张图生成配套 .txt 描述文件。系统提示词完全可自定义，内置针对 Stable Diffusion（括号权重语法）、Z-Image 等模型的预设。依赖 Git、uv 与单独安装的 Ollama 服务，从源码克隆运行，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Web 界面与 CLI 两种运行方式
- 系统提示词完全自定义，支持自定义预设
- 内置 Stable Diffusion（权重语法）与 Z-Image 等预设
- 支持前缀/后缀追加与覆盖控制等批处理选项

## 适用场景

- 为 LoRA 训练数据集批量生成图片描述文件
- 按 Stable Diffusion 或 Flux 等目标模型定制输出格式
- 本地离线批量给图片写说明文字

## 场景标签

 · 领域:图像描述/生成式 AI 数据准备

## 证据(README 行号)

> L3: Tool to automatically generate text descriptions (captions) for images using Ollama vision models (LLaVA, Qwen3-VL, 
> L9: **Perfect for AI image generation training!** This tool is designed to help you create caption files for training Lo
> L11: When training a LoRA, each image in your dataset needs an accompanying `.txt` file with a description. This tool au

## 星数曲线

```mermaid
xychart-beta
    title "hydropix/AutoDescribe-Images 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-25 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c7cfb59dda7c` · [字段定义](../../DATASET.md)*
