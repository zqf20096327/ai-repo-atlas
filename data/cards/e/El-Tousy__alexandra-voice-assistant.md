# El-Tousy/alexandra-voice-assistant

⭐ 16 · Kotlin · MIT · 推送 2026-10-26 · [GitHub](https://github.com/El-Tousy/alexandra-voice-assistant) · 个人维护

**Android 语音助手：语音识别接入 OpenAI 生成回答并朗读**

以 Kotlin/Java 开发的原生 Android 语音助手（PFE 毕业项目）：设备端 SpeechRecognizer 转写用户语音，文本发送 OpenAI API 生成回答，再以 Android TextToSpeech 朗读；支持按用户保存对话历史、语音创建提醒与任务。Firebase 负责认证与数据存储，另含静态 Web 管理面板。需自备 Firebase 项目与 OpenAI API Key，已知限制：密钥嵌入客户端可被提取，公开 APK 不含真实密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备端语音转写（SpeechRecognizer）+ OpenAI 生成 + TTS 朗读的完整链路
- Firebase 认证与按用户的对话历史、提醒任务存储
- 附静态 Web 管理面板（用户管理、使用统计、活动日志）
- GitHub Actions CI/CD：签名 APK 发布并附 SHA-256 校验

## 适用场景

- 在 Android 手机上用语音对话获取 AI 回答并朗读
- 用语音创建和管理提醒与任务
- 管理员通过 Web 面板管理用户与查看使用统计

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L26: Alexandra ist ein Sprachassistent von Anfang bis Ende. Ein Benutzer spricht mit der Android-App, die Sprache wird a
> L53: - **Spracherkennung** — freihändige Interaktion mit dem `SpeechRecognizer` von Android
> L54: - **KI-Konversation** — Antworten, die über die OpenAI-API generiert werden

## 星数曲线

```mermaid
xychart-beta
    title "El-Tousy/alexandra-voice-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `bfd72176e6de` · [字段定义](../../DATASET.md)*
