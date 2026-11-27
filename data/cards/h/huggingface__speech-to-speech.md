# huggingface/speech-to-speech

⭐ 13,796 · Python · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/huggingface/speech-to-speech) · 组织维护

**本地运行的开源模型语音代理，一条命令开始对话**

基于开源模型级联的低延迟语音代理：Silero VAD 检测语音边界、Parakeet TDT 转写、Qwen3.5-4B 生成回复、Qwen3-TTS 合成语音，四个阶段各自独立线程并通过队列连接，每个阶段可通过 CLI 标志替换为多种后端。服务器实现 OpenAI Realtime 协议（WebSocket/WebRTC），面向 OpenAI Realtime API 构建的客户端可指向本地实例。默认安装无需 API key 与云服务，首次运行下载模型后可完全离线工作；README 另说明 Ubuntu 需安装音频库、默认 TTS wheel 针对 CUDA 12.8 与 Ubuntu 24.04。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.4 天,年发版 5,65 位贡献者
- 涨星:近 1 天 **+12**(自 20261016 起算)
- 安装:pypi 包 `speech-to-speech` 月下载 2,270
- 平台:WINDOWS / MACOS / LINUX · 协议:OPENAI-API

## 能力要点

- 四阶段可替换流水线：VAD→STT→LLM→TTS，每阶段多后端可选
- 实现 OpenAI Realtime 协议，兼容 OpenAI Realtime 客户端
- 本地运行，首次下载模型后可离线使用
- 支持 viseme 提取与流式说话人分离等可选功能

## 适用场景

- 在本机搭建可对话的语音助手
- 将现有 OpenAI Realtime 客户端切换到自托管服务器
- 为机器人（如 Reachy Mini）提供对话后端
- 按平台与硬件选择不同的 STT/TTS/LLM 后端组合

## 场景标签

`语音 Agent` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L11: A low-latency voice agent built from open models that **runs entirely on your computer**. One command starts a conv
> L13: The default pipeline is **Silero VAD → Parakeet TDT → Qwen3.5-4B → Qwen3-TTS**, and every stage is swappable. The s

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/speech-to-speech 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 13521 --> 13821
    line [13546, 13555, 13565, 13581, 13586, 13601, 13600, 13610, 13615, 13546, 13656, 13670, 13679, 13685, 13691, 13693, 13697, 13704, 13707, 13737, 13753, 13758, 13763, 13767, 13776, 13788, 13796]
```

2026-10-25 13,546 → 2026-11-27 13,796（+250）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `fded8513e21a` · [字段定义](../../DATASET.md)*
