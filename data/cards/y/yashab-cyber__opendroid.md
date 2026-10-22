# yashab-cyber/opendroid

⭐ 1,184 · Kotlin · NOASSERTION · 推送 2026-10-18 · [GitHub](https://github.com/yashab-cyber/opendroid) · [官网](https://yashab-cyber.github.io/opendroid/) · 个人维护

**运行在 Android 手机上的自主 AI 代理应用，替用户执行任务**

OpenDroid 是一个 Android 原生应用（Kotlin/Jetpack Compose，Dagger-Hilt 架构），将用户的自然语言指令拆解为带依赖跟踪的多步骤计划并逐步执行：通过 Accessibility API 控制系统设置、WhatsApp/Telegram 消息、通话、闹钟、导航、UPI 支付等；截图喂给视觉 LLM 做屏幕理解。支持 13 个 LLM 提供商（含 Ollama 本地模型与 LiteRT-LM 端侧模型管理），配自动故障切换。需 JDK 21 与 Android SDK 35 从源码构建安装，首启需授予无障碍、录音等多项权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自规划代理引擎：指令拆解为步骤、执行验证、失败重规划
- 通过 Accessibility API 控制通信、系统、导航、支付等手机功能
- 13 个 LLM 提供商接入，含 Ollama 本地运行与 LiteRT-LM 端侧模型管理
- 离线唤醒词 + 语音识别/合成与 4 层个人知识图

## 适用场景

- 用一句话让手机代办多步任务，如查天气并发消息设闹钟
- 本地 Ollama 或端侧模型离线运行代理
- 从日常使用中挖掘重复操作并一键自动化

## 场景标签

 · 领域:移动端 AI 代理/自动化

## 证据(README 行号)

> L26: OpenDroid isn't just another chatbot. It's a **fully autonomous AI agent** that lives on your Android phone and act
> L30: OpenDroid will **plan** this as 3 steps, **execute** each one, **verify** the results, and **adapt** if anything fa
> L135: |🏠 **Ollama**|Any local model (LLaMA, Phi, etc.)|Local|

## 星数曲线

```mermaid
xychart-beta
    title "yashab-cyber/opendroid 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 1158 --> 1186
    line [1160, 1176, 1184]
```

2026-10-18 1,160 → 2026-10-22 1,184（+24）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8800b5a87b49` · [字段定义](../../DATASET.md)*
