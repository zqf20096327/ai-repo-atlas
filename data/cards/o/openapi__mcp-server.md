# openapi/mcp-server

⭐ 22 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/openapi/mcp-server) · [官网](https://console.openapi.com) · 组织维护

**面向 openapi.com API 的官方 Python MCP SDK 与开箱即用服务器**

由 Openapi 团队维护的官方 MCP SDK（openapi-mcp-sdk），以 Python 包形式发布在 PyPI，可一条命令启动 MCP 网关服务器，或作为库导入以构建封装 openapi.com API 的自定义 MCP 服务器。客户端提供的 Bearer Token 被透传代理，不在服务端直接处理敏感凭据。二进制文件（PDF/ZIP 等）通过独立 HTTP 端点下载与分发，存储后端支持本地/GCS/S3，缓存支持 Redis/Memcached，并提供 Docker Compose 与 VS Code 一键远程调试配置。

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

- uvx openapi-mcp-sdk server 单命令启动，无需克隆代码
- 客户端 Bearer Token 透传代理，支持 Authorization 头与 ?token= 查询参数两种认证方式
- 二进制文件本地/GCS/S3 存储后端，独立 HTTP 端点分发
- VS Code + Docker 一键远程调试（debugpy，F5 附加断点）

## 适用场景

- 让 Claude、VS Code Copilot 等 MCP 客户端调用 openapi.com 的 API（如意大利公司官方文件查询）
- 基于 SDK 扩展自定义 MCP 工具与 API 模块
- 通过 Docker Compose 在本地、AWS、GCP 或 Kubernetes 上部署 MCP 网关

## 场景标签

 · 领域:LLM 基础设施/MCP 服务器

## 证据(README 行号)

> L17:  The official Python MCP SDK and ready-to-run MCP server for Openapi®
> L29: Welcome to **`openapi-mcp-sdk`**, this is the official openapi.com MCP SDK.
> L33: - **Ready-to-use server** — run the MCP gateway directly from the package with a

## 星数曲线

```mermaid
xychart-beta
    title "openapi/mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `58fb85405397` · [字段定义](../../DATASET.md)*
