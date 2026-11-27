# jaykwok/jav-sub

⭐ 59 · Python · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/jaykwok/jav-sub) · [官网](https://github.com/jaykwok/jav-sub/releases/latest) · 个人维护 · 中文 README

**给 Windows + NVIDIA 用户本地一键生成日语视频字幕的工具**

Windows 桌面工具，选定视频后自动完成日语语音识别（Qwen3-ASR）、CTC 字词级时间轴对齐、翻译与 SRT 导出。翻译默认使用内置本地模型（Hy-MT3-7B Q4 经 CUDA llama.cpp 运行，自动下载部署，离线免费），也可切换 OpenAI 兼容 API（默认 OpenRouter，需支持 /responses 接口）。输出仅日文/仅译文/双语三种模式，按 Netflix 字幕规范排版。要求 Windows 10/11 与 ≥8 GB 显存的 NVIDIA 显卡，不回退 CPU。发布包双击运行，首次启动自动安装 Python/PyTorch 依赖并下载模型（共约 12 GB 以上，磁盘需预留约 17 GB），支持在线一键升级与缓存续跑。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地翻译默认路径：Hy-MT3-7B Q4 经自动部署的 CUDA llama-server 离线运行，无需手动配置
- Qwen3-ASR 识别与 CTC 字词级时间轴对齐，三种字幕输出共用同一条日文时间轴
- 支持 OpenAI 兼容 API 翻译（默认 OpenRouter，需 Responses 接口）与自定义术语表
- 发布包双击启动，依赖与模型自动下载续传，支持在线一键升级

## 适用场景

- 为本机日语视频批量生成中文或双语 SRT 字幕
- 离线环境下不依赖 API 完成识别与翻译
- 需要字词级对齐时间轴或按 Netflix 规范排版字幕

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: **为日语视频一键生成日文、中文或双语 SRT 字幕。** 在本机桌面窗口选好视频，自动完成日语识别、时间轴对齐、翻译（本地或 API）与字幕排版导出。
> L7: > **适用环境**：Windows 10/11 + NVIDIA 显卡（≥ 8 GB 显存）。字幕默认保存到视频所在目录。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `62febe1f58a6` · [字段定义](../../DATASET.md)*
