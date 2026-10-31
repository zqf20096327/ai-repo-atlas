# murillous/LumaBot

⭐ 27 · TypeScript · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/murillous/LumaBot) · 个人维护

**基于 Bridger 的 WhatsApp 个人助理机器人：多模型对话与群聊工具**

用 TypeScript 编写、构建在 Bridger 内核（@usebridger/* npm 包）之上的 WhatsApp 机器人，通过 Baileys 连接、SQLite 存储。核心是带人格的虚拟助理 Luma：支持 Gemini/OpenAI/Claude/DeepSeek 多模型链与 fallback、tool calling，并响应自然语言指令调用工具。功能包括贴纸制作、音频转录、对话摘要、定时提醒、yt-dlp 下载、PDF 处理和群互动排名。自带 Web 仪表盘（默认仅监听环回），可在线配置插件与 AI 密钥（加密存储），并提供审计日志与 AI 消耗/成本指标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型链（Gemini/OpenAI/Claude/DeepSeek）带 fallback 与 tool calling
- 插件化架构：贴纸/转录/摘要/提醒/下载/PDF 等约 20 个插件，多数暴露为 AI 可调用工具
- Web 仪表盘：QR 配对、插件热配置、审计日志、AI 消耗与成本指标
- 首次启动仅需扫码配对 WhatsApp，无强制环境变量

## 适用场景

- 在 WhatsApp 个人聊天或群组中与 AI 助理对话并执行任务
- 把图片/视频/链接做成贴纸，或转录语音消息
- 群聊中生成对话摘要、设置提醒、下载视频音频

## 场景标签

`AI 助手` `聊天机器人` `图像视频处理` `语音识别` · 领域:对话与助手

## 证据(README 行号)

> L10: Bot de WhatsApp com a **Luma**, assistente virtual com personalidade: conversa por IA (Gemini,
> L11: OpenAI, Claude, DeepSeek), faz figurinhas, transcreve áudio, resume a conversa, agenda lembretes e
> L196: |`ai`|Cadeia de modelos (Gemini, OpenAI, Claude, DeepSeek) com fallback, tool calling e busca nativa. Oferece o se

## 星数曲线

```mermaid
xychart-beta
    title "murillous/LumaBot 星数(近 2 点)"
    x-axis ["2026-10-30", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-30 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6b45f0bad8a7` · [字段定义](../../DATASET.md)*
