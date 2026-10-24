# Dicklesworthstone/franken_whisper

⭐ 94 · Rust · NOASSERTION · 推送 2026-10-16 · [GitHub](https://github.com/Dicklesworthstone/franken_whisper) · 个人维护

**Rust ASR 编排工具：统一多 Whisper 后端，agent 友好流式输出**

单一 Rust 二进制，内置纯 Rust 实现的 Whisper 推理引擎（无 FFI/Python/子进程），解析 ggml 模型完成语音转文字，并可编排 whisper.cpp、insanely-fast-whisper、whisper-diarization 等后端，按贝叶斯决策契约自动选路。面向 LLM agent 与开发者：所有命令输出带版本化 schema 的 NDJSON 事件流，13 个结构化错误码，SQLite 持久化运行历史，进程内解码常见音频格式，TTY 音频传输与协作式取消。内置 Sortformer 说话人分离默认最多四路且自称未认证。提供 SHA-256 校验的预编译二进制与一键安装脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 进程内纯 Rust Whisper 引擎（ggml 解析、FrankenTorch CPU 内核、DTW 词级时间戳）
- 贝叶斯后端自动路由与实时 NDJSON 流式事件（schema v1.1.0）
- SQLite 运行历史持久化与 JSONL 回放包
- 进程内解码 MP3/AAC/FLAC/WAV/OGG/ALAC，ffmpeg 仅作视频/特殊编解码回退

## 适用场景

- LLM agent 以机器可读事件流做语音转文字编排
- 批量转录并保留可回放的运行历史
- 带说话人分离的会议转写（四路以内）

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L72: - **A real in-process Whisper engine, in pure Rust.** ggml model parsing, log-mel frontend, encoder/decoder transfo
> L110: franken_whisper transcribe --input meeting.mp3 --json

## 星数曲线

```mermaid
xychart-beta
    title "Dicklesworthstone/franken_whisper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 93 --> 95
    line [94, 94]
```

2026-10-18 94 → 2026-10-24 94（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `c7a1759727fe` · [字段定义](../../DATASET.md)*
