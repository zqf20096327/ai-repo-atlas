# nohairblingbling/Interview-Assistant

⭐ 44 · TypeScript · MIT · 推送 2026-06-16 · [GitHub](https://github.com/nohairblingbling/Interview-Assistant) · 个人维护 · 中文 README

**实时转录面试音频并用 GPT 生成回答建议的桌面应用**

基于 Electron 与 React 的桌面应用，捕获系统音频（如在线会议），经 Deepgram 或 60db 两种可切换引擎实时转文字，再调用 OpenAI GPT 基于转写内容生成回答建议，支持带转发地址的第三方 API。用户可上传文本/图片/PDF 与自定义提示词构建个性化上下文，60db 密钥可选提供 TTS 朗读回答。需自行配置各服务 API 密钥，提供 Windows/macOS 安装包与源码开发流程，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Deepgram/60db 双引擎实时语音转文字，设置页可切换
- GPT 回答建议，支持上传文本/图片/PDF 与自定义提示词
- 60db TTS 朗读回答（手动或自动播放）
- Electron 跨平台，Windows/macOS 安装包

## 适用场景

- 在线面试中实时获取问题的回答建议
- 基于简历等个人文档获得个性化回答
- 通过语音播报收听建议（搭配耳机）

## 场景标签

`语音识别` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: Interview Assistant 是一款基于 Electron 的应用，可以捕获系统音频，并提供面试中回答建议。
> L9: 1. **实时语音转文字**: 支持 **Deepgram** 和 **60db** 两种实时语音识别引擎，可在设置页面自由切换。
> L11: 3. **智能 GPT 回答**: 集成 OpenAI 的 GPT 模型，为面试问题提供即时、智能的回答建议。(支持带转发地址的第三方API)

## 星数曲线

```mermaid
xychart-beta
    title "nohairblingbling/Interview-Assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-26 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f5d33c1fff28` · [字段定义](../../DATASET.md)*
