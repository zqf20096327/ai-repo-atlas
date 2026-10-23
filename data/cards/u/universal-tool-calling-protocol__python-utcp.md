# universal-tool-calling-protocol/python-utcp

⭐ 653 · Python · MPL-2.0 · 推送 2026-09-16 · [GitHub](https://github.com/universal-tool-calling-protocol/python-utcp) · [官网](https://www.utcp.io/) · 组织维护

**让 AI agent 直接调用各类 API 的工具调用协议 Python 实现**

UTCP 是一个开放的工具调用协议，此仓库为其官方 Python 实现：通过核心库加协议插件的模块化架构，让 AI agent 经统一接口调用 HTTP/REST、SSE、CLI、本地文件、WebSocket、MCP 等多种协议的工具。核心基于 Pydantic 模型（Tool、CallTemplate、UtcpManual），提供 UtcpClient、可扩展插件系统、内置工具存储与搜索策略，并支持协议白名单安全限制与共享/独占实例两种协议生命周期。1.0.0 引入了多项破坏性变更与迁移指南。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 协议插件架构：HTTP/SSE/CLI/文本/WebSocket/MCP 等插件按需安装
- 基于 Pydantic 的 Tool/CallTemplate/UtcpManual 数据模型与 UtcpClient
- allowed_communication_protocols 提供按 manual 的协议白名单安全限制
- 共享实例与工厂注册两种协议生命周期，实现客户端间状态隔离

## 适用场景

- 为 AI agent 接入 HTTP、CLI、本地文件等多种协议的工具
- 通过 MCP 插件与 Model Context Protocol 服务交互
- 以统一 UTCPManual 格式描述并向 agent 提供工具

## 场景标签

 · 领域:LLM 基础设施/工具调用

## 证据(README 行号)

> L10: The Universal Tool Calling Protocol (UTCP) is a secure, scalable standard for defining and interacting with tools a
> L42: - **Client Interface**: Main `UtcpClient` for tool interaction
> L91: UTCP supports multiple communication protocols through dedicated plugins:

## 星数曲线

```mermaid
xychart-beta
    title "universal-tool-calling-protocol/python-utcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 652 --> 654
    line [653, 653]
```

2026-10-18 653 → 2026-10-23 653（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5e8864013c2f` · [字段定义](../../DATASET.md)*
