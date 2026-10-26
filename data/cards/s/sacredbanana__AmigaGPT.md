# sacredbanana/AmigaGPT

⭐ 80 · C · NOASSERTION · 推送 2026-10-07 · [GitHub](https://github.com/sacredbanana/AmigaGPT) · 个人维护

**AmigaOS/MorphOS 上的多供应商 AI 聊天与图像生成客户端**

面向复古 Amiga 平台（AmigaOS 3.1/4.1、MorphOS）的本地 AI 客户端，基于 MUI 框架提供原生界面。支持 OpenAI、Google Gemini、SpaceXAI Grok、Anthropic Claude 及 OpenAI 兼容自定义 LLM 服务器进行对话，支持 DALL-E、Gemini 等生成图像并附参考图编辑；提供云 TTS 与离线语音合成（narrator.device/flite.device）、代码解释器、AmigaDOS Shell 工具、Web 搜索与 ARexx 脚本控制。安装依赖 AmiSSL、MUI 3+ 等系统库，需自备 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多供应商聊天：OpenAI、Gemini、Grok、Claude 与 OpenAI 兼容自定义服务器
- AI 图像生成与参考图编辑，可保存 PNG/JPEG
- 云 TTS（OpenAI/ElevenLabs 等）与 OS 原生离线语音合成
- ARexx 脚本化控制：发消息、生成图像、调用语音

## 适用场景

- 在 Amiga 或 MorphOS 机器上直接使用 ChatGPT 等 AI 对话
- 在复古系统上用提示词生成和编辑图像
- 通过 ARexx 脚本把 AI 能力接入其他 Amiga 程序

## 场景标签

`聊天机器人` `图像生成` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L3: AmigaGPT is a versatile multi-provider AI client for AmigaOS 3.x, 4.1 and MorphOS. This powerful tool brings the cap
> L11: **AmigaGPT** supports multiple AI providers for chat: **OpenAI** (o1, o3, o4, GPT-5, GPT-4o, GPT-4 and GPT-3.5), **

## 星数曲线

```mermaid
xychart-beta
    title "sacredbanana/AmigaGPT 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 78 --> 81
    line [79, 80, 80]
```

2026-10-18 79 → 2026-10-26 80（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8694138e7569` · [字段定义](../../DATASET.md)*
