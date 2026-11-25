# Open-Less/openless

⭐ 4,157 · Rust · AGPL-3.0 · 推送 2026-11-23 · [GitHub](https://github.com/Open-Less/openless) · [官网](https://openless.top) · 个人维护 · 中文 README

**开源语音输入工具：按住说话，松开得润色文本**

跨平台语音输入应用，覆盖 macOS/Windows/Linux/Android/iOS/HarmonyOS 六端，共享 openless-core 后端。用户按全局快捷键说话，应用录音、转写、按所选风格润色后插入光标处，插入失败时回退到剪贴板。特色是 AI-prompt 模式：将口语整理为可直接粘贴给 ChatGPT/Claude/Cursor 的结构化提示词。支持风格包市场、可学习词典热词、流式插入；需用户自带约 30 家 ASR 与 20 家润色服务凭证，数据本地保存。目前处于稳定性冻结阶段，仅接受修复类贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按住快捷键→语音转写→AI 润色→光标处插入，失败回退剪贴板
- AI-prompt 模式将口语整理为带上下文与约束的结构化提示词
- 自带约 30 家 ASR 与 20 余家润色服务接入（火山、讯飞、阿里百炼、OpenAI 兼容端点等）
- 风格包市场支持自定义系统提示词的创建、一键安装与发布

## 适用场景

- 为 ChatGPT/Claude/Cursor/Gemini 口述并生成结构化提示词
- 起草邮件、规格文档、Slack/微信长消息
- 口述代码注释、commit 信息与 PR 描述
- 任何需要产出文字但不想打字的场景

## 场景标签

`语音识别` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L73: OpenLess is a cross-platform (macOS, Windows, Linux, Android, iOS, and HarmonyOS) voice-input application — a fully
> L77: Place your cursor in any text field — ChatGPT, Claude, Cursor, Notion, an email draft, a chat box — press a single 
> L139: - **Bring your own cloud credentials.** Nearly thirty ASR providers and more than twenty polish providers — Volcen

## 星数曲线

```mermaid
xychart-beta
    title "Open-Less/openless 星数(近 26 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 3913 --> 4179
    line [3935, 3941, 3953, 3965, 3975, 3982, 3989, 3997, 4006, 4015, 4024, 3953, 4062, 4076, 4084, 4090, 4097, 4104, 4114, 4124, 4134, 4139, 4142, 4148, 4157, 4157]
```

2026-10-23 3,935 → 2026-11-25 4,157（+222）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `13497e13e064` · [字段定义](../../DATASET.md)*
