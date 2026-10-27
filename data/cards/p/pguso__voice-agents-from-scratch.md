# pguso/voice-agents-from-scratch

⭐ 49 · Python · MIT · 推送 2026-05-03 · [GitHub](https://github.com/pguso/voice-agents-from-scratch) · 个人维护

**Python 实时语音 agent 从零构建教程：麦克风→STT→LLM→TTS 全链路**

面向学习者的实操教程仓库：以编号章节（音频 IO、语音识别、语音合成、agent 核心、实时系统、工具调用等）讲解并运行端到端实时语音 agent 管线——麦克风→Whisper STT→本地 LLM→Kokoro TTS→扬声器，显式讨论流式行为与延迟。附带小型共享库 src/voice_agents/ 与可运行脚本，模型全部本地运行（Whisper tiny.en、Qwen 2.5 0.5B Q4 GGUF、Kokoro v1.0，约 800 MB）。环境管理统一使用 uv，需麦克风/扬声器与 PortAudio。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端到端语音 agent 管线：麦克风→STT→本地 LLM→TTS，流式播放先于完整回复生成
- 本地模型运行（faster-whisper / Qwen 2.5 0.5B Q4 GGUF / Kokoro ONNX），无需云端 API
- 10 个编号章节覆盖音频 IO、流式 STT/TTS、实时打断、工具路由与项目组合
- 提供 src/voice_agents/ 共享库与交互式脚本启动器

## 适用场景

- 从零学习实时语音 agent 的完整构建流程
- 动手实践流式 STT/TTS 与低延迟管线设计
- 了解本地模型驱动的语音对话系统实现

## 场景标签

`语音 Agent` `教程课程` · 领域:对话与助手

## 证据(README 行号)

> L10: Build **real-time voice agents** from the ground up - microphone → **STT** → **LLM** → **TTS** → speaker - with too
> L93: Each numbered folder is a chapter. Inside lesson folders you typically find a **`.py`** entry script and a **`CODE.

## 星数曲线

```mermaid
xychart-beta
    title "pguso/voice-agents-from-scratch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-27 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5d488a102839` · [字段定义](../../DATASET.md)*
