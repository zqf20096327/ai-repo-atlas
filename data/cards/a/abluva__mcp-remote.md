# abluva/mcp-remote

⭐ 54 · TypeScript · MIT · 推送 2026-09-22 · [GitHub](https://github.com/abluva/mcp-remote) · 组织维护

**为 stdio MCP 客户端连接远程 MCP 服务器的 OAuth 桥接代理**

Abluva 维护的 mcp-remote 分支：以 stdio 代理形式让仅支持本地 stdio 的 MCP 客户端（Claude Desktop、Cursor 等）连接带 OAuth 认证的远程 MCP 服务器。基于上游 geelen/mcp-remote v0.1.38，合并了未合入的 PR #213（会话中重认证）等多个上游 PR，并加入回调服务器生命周期、自动端口、并发 OAuth、SSE 重连等修复。支持 legacy 与 2026-07-28 两种协议模式、SSE/HTTP 传输策略选择、静态 OAuth 客户端信息注入。通过 npx 免安装使用，也可从源码构建。上游文档标注其为实验性概念验证。

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

- stdio 客户端到远程 OAuth MCP 服务器的代理桥接
- 修复会话中 token 过期重认证、localhost 回调拒绝连接、并发 OAuth 等问题
- 支持 legacy / 2026-07-28 协议模式与 SSE/HTTP 传输策略
- 支持静态 OAuth 客户端元数据与凭据注入、--ignore-tool 工具过滤

## 适用场景

- 让 Claude Desktop、Cursor 等 stdio 客户端接入远程 MCP 服务器
- MCP 网关场景下规避 OAuth 回调与端口冲突问题
- 按名称模式过滤远程服务器暴露的工具

## 场景标签

 · 领域:MCP/LLM 基础设施

## 证据(README 行号)

> L7: **Abluva-maintained fork** of `mcp-remote` — a stdio proxy that connects MCP clients (Claude Desktop, Cursor, etc.) 
> L108: Connect an MCP Client that only supports local (stdio) servers to a Remote MCP Server, with auth support:
> L118: With the latest MCP Authorization specification, we now have a secure way of sharing our MCP servers with the worl

## 星数曲线

```mermaid
xychart-beta
    title "abluva/mcp-remote 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-28 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1fbb5dd00f4f` · [字段定义](../../DATASET.md)*
