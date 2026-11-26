# koharu-rs/koharu

⭐ 6,830 · Rust · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/koharu-rs/koharu) · [官网](https://koharu.rs) · 个人维护 · 中文 README

**本地运行的 ML 漫画翻译器：检测、OCR、修复与 LLM 翻译**

用 Rust 编写的漫画翻译工作台，将检测、OCR、图像修复与大模型翻译串联为可分步执行的流程。支持对光栅图、压缩包和 PDF 做项目管理，检测面板、气泡、文本与拟声词；OCR 支持日、中、韩、英；修复模型擦除原文并重建画面；翻译可调用本地 GGUF 模型或托管 API。提供 GPU 画布手动编辑、多语言排版与 PNG/CBZ/PDF/PSD 导出，并内置 MCP 服务器供 AI agent 调用。视觉模型与 LLM 均可完全在本地运行以保持数据不出机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检测、OCR、翻译、修复流程可按页或项目范围选择性执行
- 本地 GGUF 推理与托管 LLM 提供商双路径翻译
- 支持 CUDA、ROCm/HIP、Metal、Vulkan 四种 GPU 加速
- MCP 服务器支持 agent 驱动的工作流

## 适用场景

- 汉化/多语言化整本漫画并分层导出供后期编辑
- 完全离线环境下翻译漫画以保护数据隐私
- 手动清理气泡文字、排版竖排 CJK 与 RTL 文本

## 场景标签

`图像视频处理` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L13: Koharu introduces a local-first workflow for manga translation, utilizing the power of ML to automate the process. 
> L29: - Local GGUF inference and hosted providers for LLM translation, including ChatGPT and Grok sign-in
> L39: Koharu supports CUDA on Windows and Linux, ROCm / HIP on x86-64 Windows and Linux, Metal on Apple silicon, and Vulk

## 星数曲线

```mermaid
xychart-beta
    title "koharu-rs/koharu 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 6430 --> 6866
    line [6466, 6477, 6494, 6498, 6510, 6526, 6539, 6545, 6552, 6565, 6477, 6617, 6631, 6642, 6653, 6658, 6667, 6674, 6685, 6694, 6720, 6750, 6755, 6779, 6798, 6812, 6830]
```

2026-10-24 6,466 → 2026-11-26 6,830（+364）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `f10eff5a9b35` · [字段定义](../../DATASET.md)*
