# oceanix-pr/Memozia

⭐ 4 · Swift · MIT · 推送 2026-11-24 · [GitHub](https://github.com/oceanix-pr/Memozia) · [官网](https://github.com/oceanix-pr/Memozia/wiki) · 个人维护

**macOS 本地优先会议助手：录音转写、说话人分离与 AI 摘要**

面向 macOS 的本地优先会议助手：录制麦克风与系统音频或导入已有音视频，生成带说话人标签的转写文本、结构化摘要与可编辑的行动项，并可写入 macOS 提醒事项。转写基于 WhisperKit 在本机运行；摘要可连接本地 Ollama 或 LM Studio 服务，也可配置云服务，用户选择决定哪些内容离开本机。以 MIT 许可发布源码，当前为 Apple Silicon 预览版，应用未签名公证，模型需另行下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WhisperKit 本地转写与说话人标签文本
- 可接入 Ollama / LM Studio / OpenAI 兼容端点生成摘要
- 截图标注、OCR 与文本图片笔记等多方式记录
- 音频、转写、摘要与任务共享同一可备份的文件工作区

## 适用场景

- 本地记录会议并生成带说话人标签的转写稿
- 自动生成会议结构化摘要与可编辑行动项
- 导入已有音视频文件做转写与摘要

## 场景标签

`语音识别` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L5:  A local-first macOS meeting assistant that turns recordings into transcripts, summaries, and action items.
> L36: 2. **Prepare speech and summary models.** Follow the in-app component preparation when you first transcribe. For lo
> L42: - **Local processing when you choose it.** WhisperKit transcription runs on your Mac. Pair it with a local language


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `6e124e9c7adf` · [字段定义](../../DATASET.md)*
