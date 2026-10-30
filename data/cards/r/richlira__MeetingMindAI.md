# richlira/MeetingMindAI

⭐ 15 · Swift · 推送 2026-02-16 · [GitHub](https://github.com/richlira/MeetingMindAI) · [官网](https://github.com/richlira/MeetingMindAI#readme) · 个人维护

**iPhone 会议助手：实时转录、AI 追问与会议摘要**

运行于 iPhone 的会议辅助应用：录制音频并实时转录（云端 Whisper 或端侧 SpeechAnalyzer），在说话过程中每约 50 词生成指向矛盾、缺失数据或风险的追问，录音结束后自动产出结构化摘要（要点、行动项、参会人），并支持基于完整转写文本的事后对话。转录与 AI 均抽象为可替换的 Provider，共四种云端/端侧组合可切换，端侧出错时自动回退云端。要求 iOS 26+、Xcode 26+，端侧 AI 需 iPhone 15 Pro（A17 Pro）及以上并启用 Apple Intelligence。零第三方依赖，App Store 版本尚未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时转录 + 每 ~50 词生成 AI 追问 + 录音结束自动摘要
- 转录与 AI 的 Provider 可替换，四种云端/端侧组合（含完全离线模式）
- 零第三方依赖，纯 Apple 框架 + 直接 REST 调用
- 端侧模式下数据不出设备，API key 存 Keychain

## 适用场景

- 开会时实时看到转写文字并获得 AI 追问提示
- 录音结束后自动得到要点、行动项与参会人摘要
- 就会议转写文本向 AI 提后续问题
- 在无网络或注重隐私时用完全离线模式处理会议

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L21: - **Records audio and transcribes in real-time** — see words appear as they're spoken, with cloud (Whisper) or on-d
> L22: - **Generates intelligent questions while the speaker is still talking** — every ~50 words, AI surfaces contradicti
> L23: - **Produces a structured meeting summary** — key points, action items, and detected participants, generated automa

## 星数曲线

```mermaid
xychart-beta
    title "richlira/MeetingMindAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9f1c921151a9` · [字段定义](../../DATASET.md)*
