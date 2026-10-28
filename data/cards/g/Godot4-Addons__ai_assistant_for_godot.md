# Godot4-Addons/ai_assistant_for_godot

⭐ 35 · GDScript · MIT · 推送 2026-07-01 · [GitHub](https://github.com/Godot4-Addons/ai_assistant_for_godot) · 个人维护

**Godot 4 编辑器内的 AI 编程助手插件**

Godot 4 编辑器插件，在编辑器 dock 中提供多工具 Agent 系统：读取/补丁项目文件、语义搜索代码、自动构建项目上下文，并带权限管理器审批 AI 文件操作。支持多会话历史、@file 注入项目文件、流式 Markdown 渲染与多语言语法高亮（GDScript/Python/JS/C#/Bash/C/C++）。可切换 OpenRouter（推荐）、Gemini、HuggingFace、Cohere 四类 provider，需自带 API key；Code/Auto 模式仍在开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多工具 Agent：读文件、打补丁、语义搜索、创建文件，带循环守卫
- Permission Manager 审批 AI 的文件操作，Apply/Undo 可回滚
- 多会话历史与 @file 自动补全注入项目文件上下文
- 支持 OpenRouter/Gemini/HuggingFace/Cohere 四类 provider

## 适用场景

- 在 Godot 编辑器内与 AI 对话式生成和修改 GDScript 代码
- 让 AI Agent 基于项目结构上下文做代码补丁与搜索
- 管理多轮独立对话并回滚已应用的代码块

## 场景标签

`代码生成` `AI 助手` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: **A professional AI coding assistant plugin for Godot 4 with an agentic code system, syntax highlighting, and real-t
> L25: - 🧠 **Full Agentic System** — Multi-tool AI agent with project context, file patching, and semantic search
> L66: |**Multi-Tool Agent**|Reads files, patches code, runs searches, creates files|

## 星数曲线

```mermaid
xychart-beta
    title "Godot4-Addons/ai_assistant_for_godot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b0b08b8de7f8` · [字段定义](../../DATASET.md)*
