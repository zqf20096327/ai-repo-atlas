# rhodey/hecate

⭐ 23 · JavaScript · MIT · 推送 2026-03-23 · [GitHub](https://github.com/rhodey/hecate) · [官网](https://hecate.video) · 个人维护

**可通过 Signal 视频通话对话的 AI 助手**

通过 Signal 私密通话接入的 AI 助手：在模拟器/容器中运行 Signal Desktop 接听电话，语音经 STT（whisper-large-v3-turbo 或 voxtral-small-24b）转写，LLM（llama3-3-70b、kimi-k2-5、deepseek-r1-0528 等）生成回答，由 Pocket TTS 本地合成语音回复；视频通话借助 OBS Studio 浏览器源加载 three-vrm 虚拟形象，推理走 Tinfoil.sh 私有推理。Linux 支持语音+视频，Mac 仅语音。安装涉及 Android 模拟器、Signal 注册、Docker 容器与 just 命令，配置第二手机号，步骤较多。AI 无跨通话记忆，安全号码变更会警告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Signal 私密通话接入，Linux 支持语音与视频、Mac 仅语音
- STT/LLM/TTS 可配置：whisper/voxtral 转写、多 LLM 选项、Pocket TTS 本地合成
- three-vrm 虚拟形象 + OBS Studio 实现视频通话画面
- Tinfoil.sh 私有推理，Signal Desktop 隔离在容器中运行

## 适用场景

- 通过 Signal 打电话与 AI 助手语音或视频对话
- 搭建带 VR 虚拟形象的私密 AI 通话助手
- 在本地/私有推理环境下运行对话式 AI 语音助手

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L2: AI Assistant you can video call.
> L55: + stt_model = `whisper-large-v3-turbo`, `voxtral-small-24b`
> L56: + llm_model = `llama3-3-70b`, `kimi-k2-5`, `deepseek-r1-0528`

## 星数曲线

```mermaid
xychart-beta
    title "rhodey/hecate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `308d7c0b6613` · [字段定义](../../DATASET.md)*
