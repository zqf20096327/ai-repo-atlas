# mmiscool/aiCoder

⭐ 202 · JavaScript · MIT · 推送 2026-05-08 · [GitHub](https://github.com/mmiscool/aiCoder) · [官网](https://www.npmjs.com/package/aicodertool) · 个人维护

**面向 JavaScript 的 AI 编码助手：本地 Web UI 合并 LLM 代码片段**

基于 Node/npm 的命令行工具，在项目目录启动后通过 localhost:3000 提供 Web UI。开发者以自然语言对话请求代码修改，LLM 按指定格式输出片段，工具基于 AST 方式将片段合并进既有 JS 文件，尽量不破坏原代码。支持 OpenAI、GoogleAI、Anthropic、Groq 及 Ollama 本地模型等多种提供商，修改前自动备份，可自定义系统提示与计划文档。仅支持 JavaScript，Windows 支持为实验性，尚不支持多文件同时修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AST 方式合并 LLM 代码片段，尽量不破坏原有代码
- 支持 OpenAI/GoogleAI/Anthropic/Groq/Ollama 等多种 LLM 提供商
- 修改前自动生成带时间戳的文件备份
- 提供计划聊天与方法列表（含未实现桩）等辅助工具

## 适用场景

- 通过自然语言对话修改现有 JavaScript 项目文件
- 先制定项目计划再让 LLM 按计划生成实现
- 使用 Ollama 本地模型进行私有化代码生成

## 场景标签

 · 领域:开发者工具/AI 编码

## 证据(README 行号)

> L4: Tired of manually copying and pasting code snippets from ChatGPT into your editor? **aiCoder** is your solution, str
> L29: 6. Request code changes using natural language prompts.
> L79: Use **New Chat** to interactively modify a selected file. Before starting a conversation, be sure to choose a file 

## 星数曲线

```mermaid
xychart-beta
    title "mmiscool/aiCoder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 201 --> 203
    line [202, 202]
```

2026-10-18 202 → 2026-10-22 202（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8bf148a765a1` · [字段定义](../../DATASET.md)*
