# ArchAngelAries/TagScribeR

⭐ 38 · Python · GPL-3.0 · 推送 2026-10-19 · [GitHub](https://github.com/ArchAngelAries/TagScribeR) · 个人维护

**本地 GPU 加速的 AI 图像数据集工作室：打标、清洗并训练 LoRA**

面向 AI 图像训练数据准备的桌面应用：在共享工作区中浏览数千张图片，用本地视觉语言模型（Qwen3-VL、JoyCaption 等）或 WD booru 打标器生成字幕与标签，带词级 diff 审核队列、批量编辑、数据集健康检查、隐私审计与元数据工具，并内置基于 Fizgig 引擎的 LoRA 训练（十个模型家族、fp8/INT8/4-bit 自动选择）。原生支持 AMD ROCm 与 NVIDIA CUDA，数据默认不离开本机。在 Windows 11 + RX 7900 XT 上测试，NVIDIA/Linux/CPU 路径有自动化测试但作者无 NVIDIA 硬件实测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 VLM 与 WD 打标器生成字幕，含词级 diff 审核队列
- 内置 Fizgig 引擎的 LoRA 训练，支持 fp8/INT8/4-bit 与显存自动规划
- AMD ROCm / NVIDIA CUDA 原生运行，无需单独安装 ROCm SDK
- 原子保存、每日备份、回收站删除与系统钥匙串存 API key

## 适用场景

- 为图像生成模型准备和清洗 LoRA 训练数据集
- 批量给图片生成自然语言字幕或 booru 风格标签
- 在同一应用内完成打标、审核、导出到训练并直接训练 LoRA

## 场景标签

`图像生成` `图像视频处理` `微调` · 领域:内容生成

## 证据(README 行号)

> L5: **TagScribeR** is a local, GPU-accelerated studio for building AI training datasets and training LoRAs on them. Brow
> L86: - **Local vision models** through Hugging Face Transformers: Qwen3-VL, Qwen3.5, Gemma 4, JoyCaption and other image
> L87: - **Any OpenAI-compatible server:** LM Studio, llama.cpp, Ollama or a cloud API (use this for GGUF models).

## 星数曲线

```mermaid
xychart-beta
    title "ArchAngelAries/TagScribeR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-30 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `21dcbe3b46cd` · [字段定义](../../DATASET.md)*
