# Shubhjaiswal408/MeetingRecorder

⭐ 18 · C++ · 推送 2026-06-20 · [GitHub](https://github.com/Shubhjaiswal408/MeetingRecorder) · [官网](https://www.youtube.com/watch?v=FhV9c0Vv3Ng) · 个人维护

**ESP32-S3 自制会议录音机：实时转录、AI 摘要与会议问答**

运行于 Seeed XIAO ESP32-S3 Sense 的独立会议录音硬件项目：按键录音，经 ElevenLabs Scribe 实时转写多说话人语音，GPT-4o-mini 通过 map-reduce 流水线（按 25 KB 分段再合并）生成分节摘要，支持时长不限的会议与会后对话问答。音频、转录与摘要全部存储在 microSD 卡，通过 WiFi 热点配置后由任意浏览器访问 Web 仪表盘。以 Arduino IDE 上传 .ino 工程的方式安装，内置 JSON 解析库，无需 Library Manager。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ElevenLabs Scribe 实时转录，支持多说话人与口音
- GPT-4o-mini 生成 Overview/决议/行动项等多节摘要，map-reduce 支持不限时长
- 会议结束后可就当前或历史会议对话问答（带对话记忆）
- 数据全存 microSD，Web 仪表盘免 App 访问，可一键重新生成摘要

## 适用场景

- 自制口袋设备录制会议并拿到完整转录与结构化摘要
- 会后直接向 AI 询问决议与行动项而不用翻录音
- 断网云端订阅、纯本地存储的会议记录需求

## 场景标签

`语音识别` `文档问答` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L13: Every word from every speaker is transcribed in real time by **ElevenLabs Scribe** — handles multiple voices, accen
> L16: **GPT-4o-mini** generates a rolling summary during the meeting and a polished multi-section final report the moment
> L6: A standalone meeting recorder built on the **Seeed XIAO ESP32-S3 Sense**. Press one button, talk freely, and walk aw

## 星数曲线

```mermaid
xychart-beta
    title "Shubhjaiswal408/MeetingRecorder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `dfeb6aee9f58` · [字段定义](../../DATASET.md)*
