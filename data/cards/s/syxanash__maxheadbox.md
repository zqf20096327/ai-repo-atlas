# syxanash/maxheadbox

⭐ 355 · JavaScript · GPL-3.0 · 推送 2026-08-03 · [GitHub](https://github.com/syxanash/maxheadbox) · 个人维护

**树莓派上完全本地运行的语音激活 LLM Agent**

面向 Raspberry Pi 5 的开源语音激活 LLM agent，100% 在设备本地运行，不依赖云端 AI 提供商。语音链路使用 Vosk 做唤醒词检测、faster-whisper 做转录，LLM 通过 Ollama 运行（gemma3:1b 等模型）。前端为 React 应用承载 agent 逻辑，Express.js + Python 后端负责麦克风与 Pi 硬件交互。支持以 JavaScript 模块形式自定义工具，工具可标记 dangerous 属性在执行前要求确认。需约 6GB 空间运行模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 100% 本地运行，消除对云端 AI 提供商的依赖
- Vosk 唤醒词 + faster-whisper 本地语音转录
- JavaScript 模块方式自定义工具，dangerous 工具执行前需确认
- 带动画面部 UI（思考/使用工具/睡眠状态）

## 适用场景

- 在树莓派上搭建本地语音助手控制硬件与执行任务
- 通过语音命令让 agent 调用自定义工具自动化操作
- 为桌面盒子形态设备添加本地对话 agent

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L9: Max Headbox is an open-source voice-activated LLM agent built for Raspberry Pi. It operates 100% locally on-device, 
> L145: * The voice activation was achieved using Vosk.
> L146: * faster-whisper: Used for efficient and accurate voice transcription. For a detailed guide on setting it up local

## 星数曲线

```mermaid
xychart-beta
    title "syxanash/maxheadbox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 354 --> 356
    line [355, 355]
```

2026-10-18 355 → 2026-10-27 355（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `59d72fcf5082` · [字段定义](../../DATASET.md)*
