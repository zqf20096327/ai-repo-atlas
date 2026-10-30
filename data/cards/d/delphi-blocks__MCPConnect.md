# delphi-blocks/MCPConnect

⭐ 44 · Pascal · MIT · 推送 2026-10-29 · [GitHub](https://github.com/delphi-blocks/MCPConnect) · [官网](https://mcpconnect.delphiblocks.dev/) · 组织维护

**Delphi 的 MCP 服务器构建框架：属性驱动生成 Tools/Resources/Prompts**

面向 Embarcadero Delphi 开发者的 Model Context Protocol (MCP) 服务器框架：通过在普通 Delphi 类与方法上标注属性（如 [McpTool]），将既有业务逻辑转换为 MCP 协议服务器组件，由框架处理序列化、路由与上下文管理。内置 HTTP（WebBroker、Indy）与 STDIO 传输、有状态会话管理与 OAuth 2.1 认证。提供 Claude Code 插件以辅助脚手架生成。文档外链至官方站点，MCP 规范 2026-07-28 版本支持在分支开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 属性驱动：Delphi 类/记录直接定义为工具参数，框架生成 MCP 端点
- 内置 HTTP（WebBroker/Indy）与 STDIO 传输，支持无状态与持久连接
- 有状态会话管理与自动清理、自定义会话数据
- OAuth 2.1 认证支持（可插拔校验器、JWKS、元数据代理）

## 适用场景

- 用 Delphi 复用现有业务逻辑快速搭建 MCP 服务器
- 为 LLM 客户端暴露工具、资源与提示模板
- 让 Claude Code 通过插件辅助脚手架生成与添加端点

## 场景标签

 · 领域:LLM 基础设施/MCP 框架

## 证据(README 行号)

> L16: The Model Context Protocol (MCP) is an open standard for connecting large language models (LLMs) to external tools 
> L27: **Delphi MCP Connect (MCPConnect)** is a lightweight yet robust framework designed to drastically simplify the crea

## 星数曲线

```mermaid
xychart-beta
    title "delphi-blocks/MCPConnect 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-30 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2f74974ba6ad` · [字段定义](../../DATASET.md)*
