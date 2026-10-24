# google/mcp-security

⭐ 534 · Python · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/google/mcp-security) · 组织维护

**让 MCP 客户端接入 Google 安全产品（SecOps/GTI/SOAR/SCC）的服务器**

Google 官方的 Model Context Protocol 服务器集合，包含远程托管的 Google SecOps MCP Server 与四个可独立启用的本地服务器：Chronicle 威胁检测调查、SOAR 编排响应、Threat Intelligence 威胁情报、Security Command Center 云安全管理。通过 stdio transport 供 Claude Desktop、Cline 等 MCP 客户端调用，认证依赖 ADC 或 gcloud 登录；另含基于 Google ADK v2 的预构建 SOC Agent，可本地 REPL 或 Cloud Run 部署。提供 uv/pip 安装包与多客户端配置说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个 MCP 服务器覆盖 SecOps、SOAR、GTI、SCC，可分别独立启用
- 预构建基于 Google ADK v2 的 Autonomous SOC Agent（CLI REPL / Cloud Run）
- 提供 Claude Desktop、Cline、Cursor、VS Code 等多客户端配置位置参考
- 支持 uv 与 pip 两种安装运行方式，含 .env 环境变量加载

## 适用场景

- 让 Claude/Cline 等客户端直接查询 Google SecOps 与 GTI 数据做威胁调查
- 构建安全编排与事件响应的自动化 agent 工作流
- 用预置 SOC Agent 在本地或 Cloud Run 跑自主安全运营流程

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains Model Context Protocol (MCP) servers that enable MCP clients (like Claude Desktop or the cl
> L5: 1. **Remote MCP Server for Google SecOps** - Fully managed, enterprise-ready MCP server (Recommended)
> L104: The MCP servers from this repo can be used with the following clients

## 星数曲线

```mermaid
xychart-beta
    title "google/mcp-security 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 534 --> 536
    line [535, 535]
```

2026-10-18 535 → 2026-10-24 535（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b1217b7e0879` · [字段定义](../../DATASET.md)*
