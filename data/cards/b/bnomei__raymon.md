# bnomei/raymon

⭐ 18 · Rust · MIT · 推送 2026-07-01 · [GitHub](https://github.com/bnomei/raymon) · [官网](https://crates.io/crates/raymon) · 个人维护

**本地优先的 Ray 日志接收器：TUI 浏览 + MCP 供 AI 检索**

Rust 实现的 Ray 兼容日志接收服务：通过 HTTP POST / 端点接收 Ray 风格 JSON 日志包，持久化为 JSONL（data/entries.jsonl），并在 Ratatui 终端 UI 中实时浏览、过滤与归档。同时以 Streamable HTTP MCP 服务器形式暴露 raymon.search 与 raymon.get_entries 两个只读工具，供 AI agent 检索日志。默认监听 Ray 默认端口 23517，PHP/JavaScript/Python 等 Ray 客户端库可直接对接；支持远程模式下的 Bearer Token 认证与敏感字段脱敏。提供 Cargo/Homebrew/GitHub Releases/源码四种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HTTP ingest 端点接收 Ray 风格 JSON 日志并合并去重存储
- MCP 服务器暴露 raymon.search 与 raymon.get_entries 只读工具，供 AI agent 检索日志
- Ratatui 键盘优先 TUI：模糊/正则搜索、jq 详情查询、归档管理
- 远程模式支持 Bearer Token 认证与 MCP 结果敏感字段脱敏

## 适用场景

- 在终端实时查看应用通过 Ray 协议发送的调试日志
- 让 AI agent 通过 MCP 检索和读取已存储的日志条目
- 后台无头模式收集日志并保留 JSONL 归档

## 场景标签

 · 领域:开发者工具/日志

## 证据(README 行号)

> L11: Raymon is a local-first Ray-style log receiver with an HTTP ingest endpoint, a Streamable HTTP MCP server, durable 
> L13: Use Raymon when you want Ray-compatible dumps from your app to be visible in a terminal and searchable by AI agents
> L22: |MCP server|Exposes `raymon.search` and `raymon.get_entries` on `POST /mcp`.|

## 星数曲线

```mermaid
xychart-beta
    title "bnomei/raymon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d36e5a7ad6c4` · [字段定义](../../DATASET.md)*
