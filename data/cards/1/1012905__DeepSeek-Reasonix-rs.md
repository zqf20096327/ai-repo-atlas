# 1012905/DeepSeek-Reasonix-rs

⭐ 8 · Go · GPL-3.0 · 推送 2026-11-23 · [GitHub](https://github.com/1012905/DeepSeek-Reasonix-rs) · 个人维护 · 中文 README

**本地运行的 AI 编码代理，提供桌面、CLI、网页与编辑器四种入口**

以 Go 编写核心、Rust+Vue+Tauri 作为桌面外壳的开源 AI 编码助手，是上游 Reasonix 的重写延续。程序本地运行，模型由用户自行配置（内置 DeepSeek 预设，任何 OpenAI 兼容端点一条配置即可接入）。它读取项目代码、编辑文件、运行命令与测试，支持权限分级、计划模式与按会话轮次回滚被编辑文件的变更。同一引擎提供桌面应用 Studio、终端 TUI、本机网页界面与 VS Code/ACP 编辑器接入四种使用方式；通过 MCP 与 Extension Protocol 支持插件。上游 1.x 经 npm/Homebrew 分发，2.x 目前以 release 归档与源码构建提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取代码、编辑文件、运行命令与测试，带权限分级与 plan 模式
- 按会话轮次回滚其编辑工具改动的文件
- DeepSeek 内置预设，OpenAI 兼容端点为一条配置项
- MCP 服务器与 Extension Protocol 插件扩展工具与 UI

## 适用场景

- 在终端里用自然语言描述任务让代理改代码、跑测试
- 在 VS Code 或支持 ACP 的编辑器中接入本地编码代理
- 在脚本中通过 reasonix run 执行编码任务
- 自托管网页界面在本机浏览器中使用

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L19:  An open-source coding agent for your terminal, desktop, browser and editor.
> L25: Reasonix is an open-source AI coding assistant. The program runs on your computer; the AI model is a service you co
> L31: - **Read, edit, run.** It reads code, edits files and runs tests and commands, all inside your project folder.

## 星数曲线

```mermaid
xychart-beta
    title "1012905/DeepSeek-Reasonix-rs 星数(近 2 点)"
    x-axis ["2026-11-20", "2026-11-24"]
    y-axis "stars" 7 --> 9
    line [8, 8]
```

2026-11-20 8 → 2026-11-24 8（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `8f3a8071ccb1` · [字段定义](../../DATASET.md)*
