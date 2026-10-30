# einToast/openai_stt_ha

⭐ 35 · Python · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/einToast/openai_stt_ha) · 个人维护

**Home Assistant 自定义组件：经 OpenAI API 接入 Whisper 语音转文字**

面向 Home Assistant 用户的自定义集成，将 OpenAI Speech-to-Text（Whisper）通过 OpenAI API 接入 Assist 语音管线，提供 STT 平台。支持 gpt-4o-mini-transcribe、gpt-4o-transcribe、whisper-1 三种模型，可选 Realtime API（测试版）与自定义兼容 API URL，可配置 temperature、prompt、噪声抑制等参数。经 HACS 或手动放置文件安装，需 OpenAI API key，按分钟音频计费。已知 HA ≥2023.7 存在一条日志报错但不影响功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 STT 平台形式接入 Home Assistant Assist 管线
- 支持 gpt-4o-mini-transcribe / gpt-4o-transcribe / whisper-1 三种模型
- 可选 OpenAI Realtime API（beta）及兼容 API URL
- 提供 temperature、prompt、噪声抑制等参数配置

## 适用场景

- 在 Home Assistant Assist 语音助手中用 OpenAI Whisper 做语音识别
- 将家庭语音指令转文字后交给 Assist 处理
- 通过自定义 API URL 接入兼容 OpenAI 接口的服务

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: This custom component integrates OpenAI Speech-to-Text, also known as Whisper, into Home Assistant via the OpenAI AP
> L27:   - platform: openai_stt

## 星数曲线

```mermaid
xychart-beta
    title "einToast/openai_stt_ha 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `24ba517d9a0b` · [字段定义](../../DATASET.md)*
