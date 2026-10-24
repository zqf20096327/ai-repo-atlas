# Icecubesaad/OpenLLM-Studio

⭐ 62 · TypeScript · NOASSERTION · 推送 2026-04-23 · [GitHub](https://github.com/Icecubesaad/OpenLLM-Studio) · [官网](https://openllm-studio.vercel.app/) · 个人维护

**本地运行 LLM 的桌面客户端：GPU 加速、HuggingFace 下载**

基于 Tauri v2 + React + Rust 的桌面应用，用于管理与本地运行 AI 模型：内置模型库管理、HuggingFace GGUF 模型搜索下载、多会话流式聊天界面。推理使用按需下载的 llama.cpp 二进制（CPU/CUDA/Vulkan/Metal 变体，首启时按硬件检测自动选择）。安装包约 5MB，运行时二进制首次运行时再下载约 100-200MB；模型推荐功能通过 OpenRouter API 实现。目前仅提供 Windows 预编译安装包，macOS/Linux 标注 Coming Soon，可从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 使用 llama.cpp 二进制本地推理，支持 CPU/CUDA/Vulkan/Metal 变体按需下载
- HuggingFace 集成：搜索并直接下载 GGUF 模型
- 硬件检测与基于硬件的 AI 模型推荐（OpenRouter API）
- 断点续传与自动重试的模型下载

## 适用场景

- 在本地私密度运行和对话 LLM，不上传数据
- 从 HuggingFace 搜索下载 GGUF 模型并管理模型库
- 根据自己的 GPU/内存获得可运行模型的推荐

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L26: A beautiful, modern desktop application for managing and interacting with local AI models. Run AI entirely on your 
> L151: OpenLLM Studio uses llama.cpp binaries for local inference. These are downloaded on-demand based on your hardware.

## 星数曲线

```mermaid
xychart-beta
    title "Icecubesaad/OpenLLM-Studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-24 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e4ff5b0acd99` · [字段定义](../../DATASET.md)*
