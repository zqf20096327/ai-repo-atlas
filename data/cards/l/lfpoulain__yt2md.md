# lfpoulain/yt2md

⭐ 3 · TypeScript · MIT · 推送 2026-11-17 · [GitHub](https://github.com/lfpoulain/yt2md) · 个人维护

**全本地转录 YouTube 频道并生成 RAG 语料库的工具**

在本地 PC 上将 YouTube 频道转为文本语料：用 yt-dlp 下载视频，Qwen3-ASR（1.7B BF16）逐词带时间戳转录并强制语言，Silero 剔除静音；Qwen3.5-9B（GGUF Q4_K_M 经 llama.cpp CUDA）每 7 秒描述画面与屏幕文字；导出 Markdown、JSON（schema 2.0）与 JSONL。提供 Web 界面管理按频道组织的库，支持暂停/重启后续跑、SHA-256 校验模型下载。限制：Windows 10/11、需 NVIDIA GPU ≥10GB 空闲 VRAM、模型约占 15GB 磁盘、无说话人分离。

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

- Qwen3-ASR 强制语言转录 + 强制对齐器逐词时间戳（80ms 步长）
- Qwen3.5-9B 每 7 秒做视觉描述，JSON 语法约束输出
- 暂停/重启续跑与按设置粒度的缓存失效机制
- 无 API key、无云服务，全部推理本地执行

## 适用场景

- 把喜欢的频道整站转录，喂给本地 RAG 或搜索引擎
- 离线生成带画面描述的视频字幕与结构化语料
- French 语音视频的确定性转录归档

## 场景标签

`RAG` `语音识别` · 领域:知识与检索

## 证据(README 行号)

> L12: YT2MD télécharge des vidéos YouTube, les transcrit mot à mot avec horodatage, décrit ce qu'on y voit à l'écran, pui
> L31:  Pipeline : YouTube, yt-dlp et FFmpeg, puis Qwen3-ASR pour l’audio et Qwen3.5 pour l’image, fusionnés en Markdown, 
> L133: |Transcription|`Qwen/Qwen3-ASR-1.7B-hf` en BF16, langue imposée, silences écartés par Silero|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `52c38d1a115c` · [字段定义](../../DATASET.md)*
