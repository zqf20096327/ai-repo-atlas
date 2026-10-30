# kfastov/tgcli

⭐ 44 · JavaScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/kfastov/tgcli) · 个人维护

**Telegram 个人账号控制台客户端与归档器，带 MCP 服务器**

基于 MTProto（非 bot API）的 Telegram 命令行客户端，面向个人账号：提供认证、后台同步与消息回填归档（messages.db）、消息列表/搜索/发送等命令，输出支持 --json。内置可选 MCP 服务器（默认绑定 127.0.0.1:8080/mcp），供 MCP 客户端/agent 接入读取 Telegram 消息。通过 npm 或 Homebrew 安装，需自行获取 api_id/api_hash 认证，配置与会话存储于系统 app-data 目录，可用 TGCLI_STORE 覆盖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MTProto 个人账号接入，支持后台同步与消息归档到 messages.db
- 可选 MCP 服务器，默认 http://127.0.0.1:8080/mcp
- 命令行消息列表/搜索/发送，支持 --json 机器可读输出

## 适用场景

- 把个人 Telegram 账号的消息归档并可命令行检索
- 让 MCP 客户端或 AI agent 通过 MCP 服务器访问我的 Telegram 消息
- 以脚本方式发送和查询 Telegram 消息

## 场景标签

 · 领域:通讯工具/CLI

## 证据(README 行号)

> L3: Telegram CLI with background sync and an optional MCP server for your personal account (MTProto, not bot API).
> L51: ## MCP (optional)
> L66: Then run `tgcli server` and point your client at the configured address.

## 星数曲线

```mermaid
xychart-beta
    title "kfastov/tgcli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7185ecfbfd55` · [字段定义](../../DATASET.md)*
