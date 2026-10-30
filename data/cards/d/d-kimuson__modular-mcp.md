# d-kimuson/modular-mcp

⭐ 51 · TypeScript · MIT · 推送 2025-11-21 · [GitHub](https://github.com/d-kimuson/modular-mcp) · 个人维护

**MCP 代理服务器：按需加载多服务器工具 schema，节省 LLM 上下文**

面向使用 MCP 的开发者的代理服务器：作为单一 MCP 端点管理多个上游 MCP 服务器，将工具按服务器分组，启动时仅向 LLM 注册 get-modular-tools 与 call-modular-tool 两个工具，分组信息嵌入工具描述供 LLM 零调用发现，需要时再按组拉取详细 schema 并代理执行。支持标准 MCP 配置格式扩展 description 字段、环境变量插值、内置迁移命令（npx migrate）、实验性 OAuth 客户端与 mcp-remote 回退方案。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 MCP 端点代理多个上游 MCP 服务器，工具按组管理
- 启动仅注册两个工具，分组信息嵌入描述供 LLM 无调用发现
- 内置迁移命令从标准 MCP 配置生成 modular-mcp.json
- 支持配置文件环境变量插值与远程服务器 OAuth 认证（实验性）

## 适用场景

- 工具数量多导致上下文被占满的 MCP 用户按需加载工具
- 把多个 MCP 服务器的工具整合为一个端点统一管理
- 从标准 .mcp.json 配置迁移到分组管理方式

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: A Model Context Protocol (MCP) proxy server that enables efficient management of large tool collections across multi
> L17: - **Proxy Architecture**: Acts as a single MCP endpoint that manages multiple upstream MCP servers

## 星数曲线

```mermaid
xychart-beta
    title "d-kimuson/modular-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-30 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `dfa9bb67aba5` · [字段定义](../../DATASET.md)*
