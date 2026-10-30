# ninjahuttjr/hal-answering-service

⭐ 20 · Python · MIT · 推送 2026-03-06 · [GitHub](https://github.com/ninjahuttjr/hal-answering-service) · 个人维护

**本地 GPU 接听并筛查来电的 AI 电话应答服务**

面向个人用户的完全本地 AI 电话接线员：以 HAL 9000 人设接听来电，通过 SignalWire 接入电话线路，本地完成语音识别（Faster-Whisper）、LLM 对话（LM Studio/Ollama 等本地 LLM）、带声音克隆的语音合成（Chatterbox Turbo），支持打断、通话录音、ntfy 推送摘要与全文转写，端到端延迟实测最低 649ms。无电话线路时自动进入浏览器演示模式。需 Python 3.12+，GPU 可选但推荐 16GB+ VRAM，生产使用需 SignalWire 账号与公网 HTTPS 端点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全本地流水线：Faster-Whisper STT + 本地 LLM + Chatterbox Turbo TTS 声音克隆（5 秒样本）
- 端到端延迟实测 649ms–1.5s，句级流式合成与 barge-in 打断
- 通话录音 WAV + JSON 元数据 + ntfy 摘要推送
- 无 SignalWire 时自动进入浏览器演示模式，交互式首次配置向导

## 适用场景

- 让 AI 代替语音信箱接听未接来电并筛查骚扰电话
- 把不想接的电话转给 AI 拖延时间（如诈骗推销）
- 自定义人设与克隆声音，打造个人电话助理
- 在浏览器演示模式下先试用对话效果再接真实线路

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: **A fully local AI phone screener.** Answers your calls as HAL 9000, screens callers, records conversations, and sen
> L5: Zero cloud AI. Zero per-minute billing. Your GPU handles everything: local LLM for conversation, local speech-to-tex
> L18: - **Fully local:** No cloud AI APIs, everything on your GPU.

## 星数曲线

```mermaid
xychart-beta
    title "ninjahuttjr/hal-answering-service 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29", "2026-10-30"]
    y-axis "stars" 17 --> 21
    line [18, 19, 20, 20]
```

2026-10-18 18 → 2026-10-30 20（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7e5634f0dc58` · [字段定义](../../DATASET.md)*
