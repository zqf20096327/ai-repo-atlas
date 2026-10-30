# mainza-ai/milimomusic

⭐ 18 · Python · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/mainza-ai/milimomusic) · 个人维护

**开源 AI 音乐生成与多轨 DAW 工作站，面向创作者**

Milimo Music 是基于 FastAPI + React 19 的开源 AI 音乐生成平台与数字音频工作站（DAW）。以 MiniMax Music 3 为默认生成引擎（Apple Silicon MLX 原生推理），提供多轨编曲、钢琴卷帘 MIDI 编辑、MusicXML 曲谱、BS-Roformer 6 轨分离、神经转录（MuScriptor/YourMT3）、歌词强制对齐与卡拉OK、翻唱合成（MuLaCover 3B）与歌声转换。多智能体创作小组负责作词与风格管理，支持 OpenAI/Gemini/Ollama 等多 LLM 提供商。限制：真实神经生成需 Apple Silicon（MLX），Windows/Linux 上生成用占位合成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MiniMax Music 3 默认引擎，Apple Silicon MLX 原生推理
- BS-Roformer 6 轨神经分离与 MuScriptor 复音转录导出 MIDI/MusicXML
- 五智能体创作小组（World-Builder/Songwriter/Stylist 等）多 LLM 接入
- 6 模式 Web Audio DAW：编曲、钢琴卷帘、曲谱、混音、卡拉OK

## 适用场景

- 用自然语言提示词和结构化歌词生成母带级立体声曲目
- 把生成的音频分离为分轨并导出 MIDI 到 Logic/Ableton 等 DAW
- 制作翻唱/混音并导出对齐歌词字幕（.lrc/.srt）

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L29: **Milimo Music** is an open-source AI music generation platform and digital audio workstation (DAW). It bridges the
> L34:     B --> C["🎼 MiniMax Music 3 Engine"]
> L110: - **MiniMax Music 3 Default Engine**: Conditioned on structured multi-section captions (`[Intro]`, `[Verse]`, `[Ch

## 星数曲线

```mermaid
xychart-beta
    title "mainza-ai/milimomusic 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `bdd403e72d7f` · [字段定义](../../DATASET.md)*
