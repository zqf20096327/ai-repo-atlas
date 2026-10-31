# djtelicloud/grok-mcp-server

⭐ 25 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/djtelicloud/grok-mcp-server) · [官网](https://grokmcp.org/) · 个人维护

**本地 Grok MCP 服务器/网关：让各 IDE 共用一个 Grok 智能体**

UniGrok 是以 Docker Compose 运行的本地 MCP 服务与网关，在 4765 端口提供单一端点，供 Cursor、Claude Code、VS Code、Codex 等 MCP 客户端通过 @grok 调用 Grok。推理路由有三条：Docker Model Runner 本地 Gemma 模型（免 key）、Grok Build 登录、可选 xAI API key，服务自动发现可用路由并返回成本回执。面向使用 AI 编码代理的开发者；限制是 Core 仅包含本仓库与服务，私有运营基础设施不属于公开部分，云端能力需 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三条推理路由：本地 Gemma、Grok Build 登录、xAI API key，自动发现与切换
- 单一 MCP 端点供多个 IDE 共用，key 仅存于服务端
- 回答附带 plane/cost/route 回执，支持 level 从 minimal 到 ultra 并行评审群
- 本地 bearer 认证、密钥脱敏后入 SQLite、CLI 运行于隔离一次性工作区

## 适用场景

- 在多个 IDE 中共用一个本地 Grok agent 而不向每个项目复制配置
- 无付费 key 时用 Docker Model Runner 本地模型获得文本辅助
- 对 PR 评论 @grok review 获得只读评审
- 跨重启的多步任务（Mission V2）凭 continue_token 续跑

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: Install UniGrok Core once, connect every MCP-capable IDE, and use `@grok` from any
> L155: Paste this into Cursor, Claude Code, VS Code, Codex, Antigravity, or any MCP-capable

## 星数曲线

```mermaid
xychart-beta
    title "djtelicloud/grok-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-31 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `293995a18e83` · [字段定义](../../DATASET.md)*
