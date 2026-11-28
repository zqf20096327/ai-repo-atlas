# LevRa7/remote-harness-mcp

⭐ 12 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/LevRa7/remote-harness-mcp) · 个人维护

**把 Gemini/ChatGPT/Claude 变成远程执行节点的 MCP 服务器**

开源 MCP 服务器，通过 SSE/Streamable HTTP/OAuth 2.1 把 Gemini、ChatGPT、Claude（含免费账户）接入用户自己的电脑、服务器或 Android 设备，使其能运行 shell 命令、读写文件、搜索索引、启动后台任务、读取遥测并回传结果。0.7.0 起无需中继网关，节点经 Tailscale Funnel 自行发布 HTTPS 地址。安全机制包括默认仅回环绑定、强制令牌/OAuth 认证、SSRF 防护、--folder/--no-shell/read_only 模式与 Docker 沙箱。提供 Windows/Linux/macOS 安装器，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 连接 Gemini/ChatGPT/Claude（App & Web，含免费账户）远程执行任务
- 0.7.0 起经 Tailscale Funnel 自发布地址，无需 VPS 中继
- shell/文件/索引/分享/遥测等 MCP 工具集，支持 Termux 运行于 Android
- 强制认证、SSRF 防护、read_only/--no-shell/Docker 沙箱隔离

## 适用场景

- 在手机聊天中远程管理家里的服务器和电脑
- 让 AI 助手拉取代码、跑测试并回报失败原因
- 无公网 IP/端口转发的 NAT 环境下远程访问自己的机器

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: > **An open-source MCP server that turns Gemini, ChatGPT, and Claude (App & Web — including free accounts!) from a c
> L11: **Remote Harness MCP** closes that gap. It is a free, open-source **Model Context Protocol (MCP)** server that conn
> L35: - **Loopback-only bind (`127.0.0.1`)** — the standalone server never listens on `0.0.0.0` by default; public ingres


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `79a45e01716d` · [字段定义](../../DATASET.md)*
