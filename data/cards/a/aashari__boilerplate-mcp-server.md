# aashari/boilerplate-mcp-server

⭐ 73 · TypeScript · 推送 2026-03-06 · [GitHub](https://github.com/aashari/boilerplate-mcp-server) · 个人维护

**TypeScript MCP 服务器模板：IP 查询示例 + 分层架构**

面向开发者的 Model Context Protocol 服务器样板工程：以 TypeScript 实现，采用 CLI/工具/资源/prompts/控制器/服务/工具库六层架构，内置完整的 IP 地理位置查询示例（对接 ip-api.com）。支持 STDIO 与 Streamable HTTP 双传输、TOON 省token输出格式、JMESPath 过滤、DNS 重绑定防护与仅本地绑定。附带 MCP Inspector 调试、47 个测试与安全文档，可作为构建任意 API 的 MCP 服务器的起点。需 Node.js >=20.x，通过 git clone 源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- STDIO 与 Streamable HTTP 双传输模式，支持 Claude Desktop 等本地助手接入
- 六层分层架构（CLI/工具/资源/控制器/服务/工具库）可扩展为任意 API 的 MCP 服务器
- TOON 输出格式与 JMESPath 过滤降低 token 消耗
- 内置 ip-api.com 地理位置查询完整示例与 CLI 命令

## 适用场景

- 基于模板快速开发对接外部 API 的自定义 MCP 服务器
- 让 Claude Desktop、Cursor 等 AI 助手通过 MCP 调用 IP 查询工具
- 学习 MCP 工具/资源/prompts 三类原语的实现模式

## 场景标签

 · 领域:AI 基础设施/MCP 服务器开发

## 证据(README 行号)

> L3: A production-ready foundation for developing custom Model Context Protocol (MCP) servers in TypeScript. Provides a c
> L30: Model Context Protocol (MCP) is an open standard for securely connecting AI systems to external tools and data sour

## 星数曲线

```mermaid
xychart-beta
    title "aashari/boilerplate-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 72 --> 74
    line [73, 73]
```

2026-10-18 73 → 2026-10-26 73（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9c366723773a` · [字段定义](../../DATASET.md)*
