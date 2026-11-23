# JansenChang/claude-terminal-translate

⭐ — · [GitHub]() · 个人维护 · 中文 README

**给 Claude Code 终端用户的中文交互翻译插件**

面向 Claude Code 终端（CLI）环境的翻译插件：用户输入中文提问后，插件先调用 DeepSeek（deepseek-chat）将提示译为英文再提交；回答完成后在其英文原文下方附中文翻译，转录保留原文。支持 `/translate on|off` 开关（跨会话持久）、`=` 前缀跳过单次翻译，翻译指令要求保留代码/路径/命令/URL 等技术内容。失败时最多重试 3 次，仍失败则保留原文；未配置 API key 时原样发送。需连接 api.deepseek.com，翻译费用按 DeepSeek 计价。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 中文提问经 DeepSeek 译成英文后提交，回答自动附中文翻译
- `/translate on|off` 开关跨会话持久，`=` 前缀跳过单次翻译
- 翻译失败（连接错误/HTTP 429/5xx）最多重试 3 次，保留原文
- 翻译指令要求保留代码、路径、命令、URL 与 Markdown 格式

## 适用场景

- 习惯用中文描述任务的开发者使用 Claude Code 终端
- 阅读英文回答时需要中文对照翻译
- 处理敏感代码前关闭翻译以避免全文发送到翻译 API

## 场景标签

 · 领域:开发工具/Claude Code 插件

## 证据(README 行号)

> L8:  A Chinese–English translation plugin for Claude Code in the terminal, powered by DeepSeek.
> L103: This project targets Claude Code in the terminal (CLI). It requires a Claude Code environment that can load this p
> L50: The key in the plugin configuration takes precedence over the environment variable. The plugin requires access to `

## 星数曲线

```mermaid
xychart-beta
    title "JansenChang/claude-terminal-translate 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `a69e9f9f8ed7` · [字段定义](../../DATASET.md)*
