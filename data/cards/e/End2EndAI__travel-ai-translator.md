# End2EndAI/travel-ai-translator

⭐ 14 · HTML · MIT · 推送 2026-10-24 · [GitHub](https://github.com/End2EndAI/travel-ai-translator) · [官网](https://lfontaine.pythonanywhere.com/) · 组织维护

**多语言录音转写翻译 Web 应用模板，供快速构建 OpenAI 应用**

基于 Flask 的 Web 应用代码模板，展示应用 Travel AI Translator：用户录音后经 OpenAI Whisper API 转写为所选语言文本，再经 GPT-4o-mini 翻译为目标语言，并通过 Google Text-to-Speech 返回译文语音，支持 52 种语言、对话模式自动切换语言。运行需 Python 3.9+ 与 OpenAI API key，本地需自签 SSL 证书以启用麦克风，另提供 Vercel 与 Render 部署说明，并有 Android 版上架 Play Store。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 录音→Whisper 转写→GPT 翻译→TTS 语音输出的完整链路模板
- 52 种语言支持与对话模式自动切换
- Vercel/Render 零配置部署说明
- MIT 许可，代码可复用于自有项目

## 适用场景

- 旅行或跨语言对话中做实时语音翻译
- 作为快速搭建 OpenAI（Whisper/GPT）Web 应用的代码模板
- 学习 Flask 调用 OpenAI 语音与文本 API 的工程实践

## 场景标签

`语音识别` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L11: The showcase application, Travel AI Translator, is a multi-language transcription and translation web application. 
> L5: - OpenAI Speech-to-text API (Whisper)

## 星数曲线

```mermaid
xychart-beta
    title "End2EndAI/travel-ai-translator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `be5da474844d` · [字段定义](../../DATASET.md)*
