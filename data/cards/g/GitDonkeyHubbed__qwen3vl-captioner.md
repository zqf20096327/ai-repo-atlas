# GitDonkeyHubbed/qwen3vl-captioner

⭐ 23 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/GitDonkeyHubbed/qwen3vl-captioner) · 个人维护

**用 Qwen3-VL GGUF/MLX 模型批量生成图像描述的桌面 GUI 应用**

基于 PyQt6 的图像描述（captioning）桌面应用，面向为训练数据集批量标注图像的用户。支持 llama-cpp-python（GGUF，Windows CUDA 与 macOS Metal）与 MLX 两种引擎，内置模型下拉列表一键下载 Qwen3-VL 系列量化模型及匹配 mmproj 视觉编码器，也可浏览加载任意本地 GGUF。提供拖放导入、批量生成、.txt 旁车自动保存、前缀/后缀模板、VRAM 感知的量化选择、下载进度与诊断脚本。Windows 需另行安装 CUDA Toolkit 才能启用 GPU；以 zip 下载加 setup 脚本方式安装，非打包安装器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双引擎：GGUF（llama.cpp CUDA/Metal）与 Apple Silicon MLX
- 模型下拉列表一键下载，自动配对 mmproj 视觉编码器
- VRAM 感知的量化选择与批量 .txt 旁车保存
- diagnose.bat 诊断脚本与 371 个测试的 CI 流程

## 适用场景

- 为图像训练集批量生成描述文本
- 在 Mac 上用 MLX 或 llama.cpp Metal 引擎做 GPU 加速标注
- 加载任意本地 Qwen3-VL 兼容 GGUF 模型并手动编辑描述

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L4:  Professional GPU-Accelerated Image Captioning for Datasets
> L120: - **llama.cpp Metal engine** — the same GGUF models (including the abliterated default) now run GPU-accelerated on

## 星数曲线

```mermaid
xychart-beta
    title "GitDonkeyHubbed/qwen3vl-captioner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `e7d08f08d1da` · [字段定义](../../DATASET.md)*
