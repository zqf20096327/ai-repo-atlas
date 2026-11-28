# aslahtp/meetmind

⭐ 10 · TypeScript · GPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/aslahtp/meetmind) · [官网](https://aslahtp.github.io/meetmind/) · 个人维护

**开源桌面会议笔记应用：录音转写并用自有 AI key 生成纪要**

Electron 桌面应用（Windows/macOS/Linux），录系统声音与麦克风，无会议机器人加入。转写可选 AssemblyAI、Google Cloud STT、Sarvam AI 或 Groq Whisper；摘要用 Gemini、Groq 或 Claude 生成含发言人标注、决定事项与行动项的纪要。笔记存本地 SQLite，可导出 PDF/Markdown 或同步 Notion。需自备各服务 API key；macOS/Linux 版为 beta，macOS 未签名、无会议自动检测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 系统声音+麦克风同录，无需会议机器人加入
- 转写引擎可选（AssemblyAI/Google STT/Sarvam/Groq），多数支持说话人分离
- 笔记模型可选 Gemini/Groq/Claude，支持回退 provider 与可编辑系统提示词
- 本地 SQLite 存储，支持全库搜索、PDF/Markdown 导出与 Notion 同步

## 适用场景

- 为线上会议自动生成带行动项的会议纪要
- 混合英语与印度语言的会议转写（Sarvam saaras:v3）
- 将已录音频或现有转写文本导入生成纪要
- 会议笔记自动同步到 Notion 页面

## 场景标签

`语音识别` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3:  Open-source AI meeting notes app for Windows, macOS and Linux.
> L35: **MeetMind is a free, open-source (GPL-3.0) desktop app for Windows 10 and 11, macOS 14.2+ (beta) and Linux (beta) 
> L59: - **Choice of note-generation model**: Google Gemini, Groq (Llama 3.3, GPT-OSS) or Anthropic Claude (Sonnet 5.5, Fa


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `b016f8f18687` · [字段定义](../../DATASET.md)*
