# senweaver/SenWeaverCoding

⭐ 18 · Rust · MIT · 推送 2026-09-02 · [GitHub](https://github.com/senweaver/SenWeaverCoding) · 个人维护 · 中文 README

**桌面 AI 代码编辑器与自主编码 agent 运行时（Rust+Tauri）**

单体安装即含桌面 IDE 与 sen CLI 的 AI 代码编辑器：Rust agent 运行时以库形式嵌入 Tauri 2 壳内，React 前端经本机回环 WebSocket/HTTP 网关通信，无独立守护进程。提供 Auto 意图路由与 14 种可固定编码模式（Agent/Vibe/Spec/Plan/TDD/Debug 等）、130+ 工具（tree-sitter 代码智能、PTY shell、Git、浏览器、SQLite+向量记忆、MCP、子代理）、多提供商接入与按会话模型路由，支持检查点回滚、cron 自动化、Slack/Telegram 等多通道适配及 TypeScript/Python SDK（JSON-RPC 2.0）。仓库内无测试文件，验证依赖 cargo check/clippy 与手工冒烟测试。

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

- 单一安装器同时提供桌面 GUI 与终端 sen CLI（Windows/macOS/Linux 预构建包）
- Auto 意图路由 + 14 种编码模式（Agent/Vibe/Spec/TDD/Debug/Designer 等）
- 130+ 工具：tree-sitter 代码智能、PTY shell、嵌入式浏览器、SQLite+向量记忆、MCP、子代理
- 多提供商支持（OpenAI 兼容/Anthropic/OpenRouter/Copilot/Ollama/Bedrock 等）与 JSON-RPC 2.0 + TS/Python SDK

## 适用场景

- 在桌面应用内让 agent 自主完成探索、重构、测试与调试
- 以 TDD/Spec/Plan 等模式约束 agent 的写入行为
- 通过 sen CLI 或 JSON-RPC/SDK 在程序中调用 agent 运行时
- 接入 Slack/Telegram 等通道远程使用编码 agent

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: SenWeaverCoding is a desktop AI code editor that ships the entire agent
> L21: |**Intent-routed coding modes**|`Auto` routes each turn to the best fit; or pin any of the 14 modes explicitly — **
> L58: |**Agent** *(default)*|yes|Fully autonomous orchestrator. Full tool surface, auto-approved tool calls, decomposes t

## 星数曲线

```mermaid
xychart-beta
    title "senweaver/SenWeaverCoding 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f489e0342920` · [字段定义](../../DATASET.md)*
