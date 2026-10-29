# akougkas/zulipchat-mcp

⭐ 33 · Python · MIT · 推送 2026-10-09 · [GitHub](https://github.com/akougkas/zulipchat-mcp) · [官网](https://pypi.org/project/zulipchat-mcp/) · 个人维护

**连接 MCP 客户端与 Zulip 聊天的 MCP 服务器**

基于 FastMCP 的 Model Context Protocol 服务器，将 Claude Code、Gemini CLI、Cursor、Copilot 等 MCP 客户端接入 Zulip 工作区，使助手可收发消息、全文搜索、按人名解析收件人、双身份（用户/机器人）切换、绑定会话到 Zulip topic、在 topic 内请求审批等。工具分两层：默认 20 个核心工具，扩展模式 60 个。支持 stdio 与带 Bearer 认证的 HTTP 传输；AI 分析类工具调用服务端 Anthropic LLM，无 API key 时返回结构化摘要。通过 uvx/PyPI 安装，也提供各客户端的配置导出命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 核心 / 60 扩展双层工具架构，含消息、搜索、会话绑定与审批
- 用户与机器人双身份切换，同一会话内以不同身份发帖
- stdio 与带 Bearer 认证、Host/Origin 校验的 HTTP 远程传输
- 服务端 Anthropic LLM 驱动的分析工具（无 key 时降级为结构化摘要）

## 适用场景

- 让 Claude Code/Gemini CLI 等助手直接读写我的 Zulip 消息
- 把长期运行的 agent 会话绑定到固定 Zulip topic 并做 in-topic 审批
- 让助手总结某 stream 今日动态或按条件检索历史消息

## 场景标签

 · 领域:AI 工具集成/即时通讯

## 证据(README 行号)

> L3:  Model Context Protocol server for Zulip Chat. Connect Claude Code, Codex, Clio Coder, OpenCode, Copilot, Antigravit
> L36: ZulipChat MCP bridges any MCP-compatible AI assistant (Claude Code, Gemini CLI, Cursor, Windsurf, etc.) to your Zul

## 星数曲线

```mermaid
xychart-beta
    title "akougkas/zulipchat-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-29 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `92789350892f` · [字段定义](../../DATASET.md)*
