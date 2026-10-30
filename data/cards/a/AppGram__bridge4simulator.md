# AppGram/bridge4simulator

⭐ 80 · 推送 2026-01-12 · [GitHub](https://github.com/AppGram/bridge4simulator) · 组织维护

**让 AI 助手控制 iOS 模拟器的 MCP 服务器**

一个 MCP (Model Context Protocol) 服务器，使 AI 助手能够控制 iOS Simulator。通过 JSON-RPC 2.0 over stdio 或 HTTP 提供服务，支持与 Claude Desktop、Cursor、Claude Code 等 MCP 兼容客户端集成；可配置启用 screenshot 等工具。提供 brew 与安装脚本两种安装方式，运行于 macOS。README 提及底层为自研 bridge，商用需联系作者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器，使 AI 助手可控制 iOS Simulator
- JSON-RPC 2.0 over stdio / HTTP 双模式运行
- 提供 Claude Desktop 与 Cursor 的接入配置示例，可按需启用工具（如 screenshot）
- brew tap 与 curl 安装脚本两种安装途径

## 适用场景

- 在 Claude Desktop/Cursor 中通过对话操作 iOS 模拟器
- 让 AI agent 对 iOS 应用做模拟器内的自动化操作与截图
- 为 MCP 兼容客户端扩展 iOS 模拟器控制能力

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: An MCP (Model Context Protocol) server that enables AI assistants to control iOS Simulator. Seamlessly integrates wi
> L74: # Start MCP server (JSON-RPC over stdio)

## 星数曲线

```mermaid
xychart-beta
    title "AppGram/bridge4simulator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-30 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `095c08d84124` · [字段定义](../../DATASET.md)*
