# ankurCES/project_mythara

⭐ 94 · Kotlin · 推送 2026-09-28 · [GitHub](https://github.com/ankurCES/project_mythara) · [官网](https://github.com/ankurCES/project_mythara) · 个人维护

**可旁加载的 Android 本地优先 agentic AI 助手层（BYO 模型）**

用 Kotlin + Jetpack Compose 编写、以单个应用旁加载到 Android 14+ 设备的 agentic AI 层：内置 AgentLoop 与 65+ 工具（通话、短信、日历、Termux、人脸识别等），支持计划分解、技能学习与确认门。本地存储联系人/消息/人格分析数据，可选经自有 GitHub 仓库同步；默认接入 MiniMax API 作为骨干，模型可替换为本地 Gemma/Llama 等。README 顶部声明仓库已停止维护，指向 Mahout 仓库替代。需 Android Studio + JDK 17 自行构建 APK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AgentLoop + 65+ 工具（短信/通话/Termux/人脸识别/文件 I/O 等）
- 本地优先：人格分析、人脸与语音数据留存设备端
- BYO 模型：默认 MiniMax API，可替换本地 Gemma/Llama 运行时
- MobileFaceNet 人脸识别（NNAPI/GPU）、Vosk 唤醒词、通知分诊

## 适用场景

- 在 Android 手机上运行自己控制的本地 agentic 助手
- 把模型换成 Gemma/Llama 本地运行时搭建隐私优先的个人 AI
- 通过 65+ 工具让代理代为操作通话、日历、文件等系统功能

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: > An open-source, local-first, fully-private **agentic AI mobile OS layer** for Android — an alternative to Google's
> L27: Mythara is a phone OS layer **you sideload as one app**, written in Kotlin + Jetpack Compose, that runs an **agenti
> L30: - **Agentic runtime.** A built-in agent loop (`agent/AgentLoop.kt`) with 65+ tools — calls, SMS, WhatsApp, calendar

## 星数曲线

```mermaid
xychart-beta
    title "ankurCES/project_mythara 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 93 --> 95
    line [94, 94]
```

2026-10-18 94 → 2026-10-23 94（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d4a104d26ebd` · [字段定义](../../DATASET.md)*
