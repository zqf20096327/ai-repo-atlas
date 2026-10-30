# niyazmft/droid-ai-toolkit

⭐ 24 · Shell · MIT · 推送 2026-10-12 · [GitHub](https://github.com/niyazmft/droid-ai-toolkit) · [官网](https://github.com/niyazmft/droid-ai-toolkit) · 个人维护

**在免 root Android（Termux）上安装运行多个 AI 工具的自动化脚本工具包**

通过 curl 一键脚本在 Termux 中以 TUI 菜单方式安装、修补并管理 OpenClaw、Gemini CLI、n8n、Ollama、Hermes、Nanobot、Pi、Paperclip 等 AI 工具。核心机制是针对 Android 的适配：绕过 renameat2 内核限制、重定向硬编码路径到 Termux 目录、经 PM2 启停监控服务并写开机脚本实现重启后恢复。限制：不支持 armv8l/armv7l 上依赖 Rust 扩展的工具（Hermes、Nanobot），需要约 2GB 存储给 Paperclip，低内存设备更新可能被杀进程（有快照回滚）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TUI 菜单安装 OpenClaw/n8n/Ollama/Hermes 等 9 类工具，含修复/更新/模块化卸载
- Android 专项补丁：renameat2 绕过、路径重定向、插件裁剪以降低内存占用
- PM2 集成与 ~/.termux/boot 开机脚本，重启后恢复服务与 sshd
- 自动检测 RAM 推荐 Node.js/n8n 内存上限，OpenClaw 更新失败自动回滚

## 适用场景

- 用闲置安卓手机本地跑 Ollama 和 AI agent，无需 root
- 在手机上部署 OpenClaw 网关接入 Telegram/Slack/Discord
- 通过 PM2 让 n8n 工作流在 Android 后台持续运行

## 场景标签

`工作流自动化` `推理引擎` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: A high-performance, automated toolkit for running AI tools — OpenClaw, Gemini CLI, n8n, Ollama, Hermes, Nanobot, Pi,
> L26: - 🚀 **PM2 Integration**: Native support for starting, stopping, and monitoring OpenClaw, n8n, Ollama, Paperclip, Pi

## 星数曲线

```mermaid
xychart-beta
    title "niyazmft/droid-ai-toolkit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-30 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9128c39158b4` · [字段定义](../../DATASET.md)*
