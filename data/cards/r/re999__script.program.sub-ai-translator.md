# re999/script.program.sub-ai-translator

⭐ 16 · Python · NOASSERTION · 推送 2026-10-10 · [GitHub](https://github.com/re999/script.program.sub-ai-translator) · [官网](https://github.com/re999/script.program.sub-ai-translator) · 个人维护

**Kodi 字幕翻译插件：用 LLM 翻译 .srt 字幕**

面向 Kodi 媒体中心用户的字幕翻译插件：调用 OpenAI GPT 或 Google Gemini API 将 .srt 字幕文件翻译为指定语言，支持从 MKV 提取字幕（实验性）、逐块校验与重试、限流与瞬态错误重试、并行请求控制（1–10），并在翻译前按各模型 token 单价给出实时费用估算，可中途取消。用户需自备 API key 并承担费用，Gemini 可用免费额度。通过 Kodi 从 zip 文件安装，需 Kodi 20+。作者声明该插件为实验性、按原样提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 OpenAI 与 Gemini API 翻译 .srt 字幕，逐块校验并重试缺失或畸形条目
- 翻译前基于模型输入/输出 token 单价实时估算费用，支持自定义价格覆盖
- 并行请求控制（1–10）、限流重试、进度条与取消功能
- 提供 Mock 后端用于离线测试（不消耗 token）

## 适用场景

- 观看外语影视时把字幕翻译成我的语言
- 从 MKV 文件提取并翻译内嵌字幕
- 在翻译前估算本次字幕翻译的 API 花费

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: **Subtitle AI Translator** is a smart, user-friendly **Kodi add-on** that enables you to **translate subtitle files 
> L12: - 🤖 Uses **OpenAI** (`gpt-5.6-luna`, `gpt-5.6-terra`) and **Gemini** (`gemini-3.5-flash-lite`, `gemini-3.8-flash`) 

## 星数曲线

```mermaid
xychart-beta
    title "re999/script.program.sub-ai-translator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `31c31566be91` · [字段定义](../../DATASET.md)*
