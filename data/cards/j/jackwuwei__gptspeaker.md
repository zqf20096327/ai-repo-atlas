# jackwuwei/gptspeaker

⭐ 101 · Python · BSD-2-Clause · 推送 2026-02-10 · [GitHub](https://github.com/jackwuwei/gptspeaker) · 个人维护 · 中文 README

**树莓派语音助手：用语音与 ChatGPT/DeepSeek 对话**

用 Python 编写的语音助手项目，可在树莓派或桌面（Linux/macOS/Windows）上运行：通过本地唤醒词（默认 "Hey GPT"，可自定义）触发，用 Azure AI Speech 做语音识别与合成，将对话发给 OpenAI 或 DeepSeek API 并语音回复。支持实时逐句播报、连续对话与历史记录（超过 4096 tokens 丢弃早期历史）。需要自备 Azure 与 OpenAI/DeepSeek（或硅基流动）账号与 API key，硬件需 USB 麦克风和音箱。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地唤醒词触发，默认 "Hey GPT"，支持自定义唤醒词模型
- 实时语音回复：每句生成后即播报，无需等待全部回复
- 连续对话并保存历史（超 4096 tokens 丢弃早期记录）
- 支持 OpenAI 官方 API、Azure OpenAI API 与 DeepSeek

## 适用场景

- 把树莓派改造成可对话的智能音箱
- 像 Siri 一样用唤醒词与 ChatGPT/DeepSeek 语音交流
- 搭建智能家居中的语音助手节点

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: * The ChatGPT/DeepSeek Voice Assistant uses a Raspberry Pi (or desktop) to enable spoken conversation with OpenAI or
> L6: * Supports real-time voice dialogue. After ChatGPT/DeepSeek returns a sentence, you can hear the voice instead of wa

## 星数曲线

```mermaid
xychart-beta
    title "jackwuwei/gptspeaker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 100 --> 102
    line [101, 101]
```

2026-10-18 101 → 2026-10-30 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `1cd8db48f520` · [字段定义](../../DATASET.md)*
