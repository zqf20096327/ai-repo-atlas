# spotozkin/threepio

⭐ 31 · Python · 推送 2026-04-28 · [GitHub](https://github.com/spotozkin/threepio) · [官网](https://www.youtube.com/watch?v=wB2CJm4sHcM) · 个人维护

**运行于树莓派的实时语音对话机器人：麦克风到扬声器全链路**

将 AI 对话从屏幕转移到实体设备的对话机器人项目：音频链路为麦克风输入 → Whisper 语音识别 → LLM（OpenAI）→ C-3PO 人格层 → TTS（ElevenLabs/OpenAI）→ 扬声器输出。从源码运行，默认使用 mock 的 STT/LLM/TTS，通过 .env 指向真实服务商；支持文本进出模式、pytest 测试与 profile 数据配置。面向希望在嵌入式硬件上搭建语音 AI 交互的机器人爱好者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 麦克风→Whisper STT→LLM→TTS→扬声器的实时语音对话链路
- C-3PO 人格行为塑造层
- 默认 mock STT/LLM/TTS，无需 API key 即可运行，通过 .env 切换真实服务商
- 支持文本输入输出模式与 profile 配置文件

## 适用场景

- 在树莓派上搭建可对话的实体机器人
- 体验从打字到语音的 AI 交互方式
- 无需 API key 先用 mock 后端跑通全流程再接入真实服务商

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L6: A real-time, AI-powered conversational droid that you can actually talk to.
> L24: Speech-to-Text (Whisper)

## 星数曲线

```mermaid
xychart-beta
    title "spotozkin/threepio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fb75f63a9967` · [字段定义](../../DATASET.md)*
