# hqn21/protocols-io-mcp-server

⭐ 15 · Python · MIT · 推送 2026-01-14 · [GitHub](https://github.com/hqn21/protocols-io-mcp-server) · [官网](https://pypi.org/project/protocols-io-mcp) · 个人维护

**让 MCP 客户端操作 protocols.io 科学实验方案的 MCP 服务器**

以 Python 编写的 Model Context Protocol 服务器，将 protocols.io 平台的 API 暴露给 Claude Desktop 等 MCP 客户端：提供公开方案关键词检索、按 ID 获取方案信息与步骤、创建和更新方案、增删步骤等 11 个工具。支持 STDIO 与 HTTP/SSE 两种传输方式，认证可选 Client Access Token 或 OAuth 2.0。安装途径包括 pip 与 Docker 镜像，需 Python 3.10+ 与 protocols.io API 凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个工具覆盖检索、方案创建与步骤管理
- 支持 STDIO 本地与 HTTP/SSE 远程两种传输
- 支持 Access Token 与 OAuth 2.0 两种认证方式
- 提供 pip 安装与 Docker 镜像（ghcr.io）

## 适用场景

- 在 Claude Desktop 中检索和阅读 protocols.io 上的实验方案
- 通过对话创建并编辑实验方案及其步骤
- 把 protocols.io 账号内的方案接入 MCP 客户端工作流

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that enables MCP clients like Claude Desktop to interact with protocols.io, a 
> L7: The server provides the following tools that can be used by MCP clients:

## 星数曲线

```mermaid
xychart-beta
    title "hqn21/protocols-io-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `eb3e147b5c4d` · [字段定义](../../DATASET.md)*
