# Eyalm321/hyperpanes

⭐ 10 · Rust · MIT · 推送 2026-11-25 · [GitHub](https://github.com/Eyalm321/hyperpanes) · 个人维护

**面向 AI agent 的平铺终端工作区：命名彩色窗格监控多个 agent**

用 Rust + Slint 构建的原生跨平台终端工作区：窗口内平铺多个真实终端窗格（Windows 走 ConPTY，Linux/macOS 走 Unix PTY，渲染核心为 alacritty_terminal），每个窗格带锁定标签与独立边框色，支持拖拽拆分到独立窗口、workspace.json 声明式启动与布局预设。面向同时运行多个 AI agent CLI 的开发者：agent 静默时窗格发光提醒，可选的 MCP Control API 让 agent 读取/驱动窗格。安装包未签名，首次启动需绕过系统警告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 原生 GPU 渲染的单二进制终端（无 Electron），窗格可跨标签/窗口拖拽拆分
- Idle-agent glow：claude/aider/codex/gemini 等 agent CLI 静默时窗格发光
- 可选 Ollama 本地 LLM 为每个窗格生成实时一行字幕
- MCP Control API（默认关闭、token 认证）让 agent 读取并驱动窗格

## 适用场景

- 同时运行多个 AI agent CLI，一眼看出哪个在等你回复
- 用 workspace.json 一键恢复固定的多窗格开发布局
- 让 agent 通过 MCP 自动查看终端输出并操作窗格

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: A desktop **terminal workspace**: tabbed windows that tile multiple live terminal panes, where each
> L22: And it's **agent‑first**: AI panes glow when their agent goes quiet, and an opt‑in **Control API /
> L131: ## Install


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `4f317ddf498d` · [字段定义](../../DATASET.md)*
