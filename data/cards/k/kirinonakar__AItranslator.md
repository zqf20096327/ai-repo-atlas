# kirinonakar/AItranslator

⭐ 15 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/kirinonakar/AItranslator) · 个人维护

**桌面端文本翻译与摘要应用，接入本地/云端 LLM**

基于 Tauri、Rust 与 React 构建的桌面应用，提供流式文本翻译、文本摘要与 UTF-8 文本文件翻译，支持长文本自动分块、源语言自动检测、温度与分块大小调节、任务停止控制及结果复制保存。模型接入走 OpenAI 兼容 chat completion API，本地支持 LM Studio 与 Ollama，云端支持 Google Gemini、Cerebras、Ollama Cloud 与 Unsloth Desktop，API key 存于 Windows Credential Manager。可从 Releases 页下载安装包，或以 Node.js 20.19+/Rust 1.90+ 环境自行构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式文本翻译与摘要，支持长文本自动分块
- 本地（LM Studio/Ollama）与云端（Gemini/Cerebras 等）多供应商接入
- UTF-8 文本文件批量翻译，输出自动递增命名防覆盖
- Rust 后端负责 API 调用与流式解析，经 Tauri 事件推送给前端

## 适用场景

- 日常翻译或摘要文本与代码类文件
- 使用本地模型离线完成翻译任务
- 翻译长文时自动分块并保留结果到 output 目录

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: AI Universal Translator is a desktop translation and summarization app built with Tauri, Rust, TypeScript, and React
> L11: - Text translation with streaming output
> L15: - Multiple provider support: Local (LM Studio, Ollama) & Cloud (Google Gemini, Cerebras, Ollama Cloud)

## 星数曲线

```mermaid
xychart-beta
    title "kirinonakar/AItranslator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b2e5c26c8856` · [字段定义](../../DATASET.md)*
