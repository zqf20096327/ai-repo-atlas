# Damecek/salesforce-mcp-lib

⭐ 19 · Apex · MIT · 推送 2026-10-29 · [GitHub](https://github.com/Damecek/salesforce-mcp-lib) · [官网](https://context7.com/damecek/salesforce-mcp-lib) · 个人维护

**连接 AI agent 与 Salesforce 的 MCP 桥接与 Apex 框架库**

由 Apex 框架（Salesforce 2GP 解锁包，54 个类）与 npm stdio 代理两部分组成：Apex 端在 org 内原生实现 JSON-RPC 2.0 的 MCP 服务器，分发 tools/resources/prompts 三类能力；npm 代理负责 OAuth 2.0 生命周期（client credentials 或 per-user PKCE 登录）、token 缓存刷新与 stdio-to-HTTPS 转发。面向需要在 Claude、ChatGPT 等 MCP 客户端中调用 Salesforce 工具的开发者。若客户端可自行管理 Salesforce OAuth，可跳过代理直连 Apex 端点。两端均零外部依赖。

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

- Apex 框架在 Salesforce org 内原生运行 MCP 服务器（JSON-RPC 2.0，全部 11 个 MCP 方法）
- npm 代理提供 OAuth token 获取/缓存/刷新与 stdio-to-HTTPS 桥接
- 支持 client credentials 与 per-user（PKCE）两种认证模式，自动检测
- 可扩展 Tool/Resource/Resource Template/Prompt 四类基类

## 适用场景

- 让 Claude 等 MCP 客户端调用我定义的 Salesforce 工具与资源
- 在 Apex 中构建运行于 org 内、受平台权限保护的 MCP 端点
- 桌面 MCP 客户端场景下由代理托管 OAuth token 生命周期

## 场景标签

 · 领域:企业软件集成/开发工具

## 证据(README 行号)

> L6: Open-source bridge connecting AI agents to Salesforce via Model Context Protocol.
> L14: |**Apex framework** (2GP unlocked)|JSON-RPC 2.0 core + MCP server running natively in your Salesforce org|`sf packa
> L19: 1. **MCP Client** (Claude, ChatGPT, any MCP host) sends JSON-RPC 2.0 messages over **stdio**

## 星数曲线

```mermaid
xychart-beta
    title "Damecek/salesforce-mcp-lib 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f674a49d1321` · [字段定义](../../DATASET.md)*
