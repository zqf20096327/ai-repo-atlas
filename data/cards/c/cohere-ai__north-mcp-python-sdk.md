# cohere-ai/north-mcp-python-sdk

⭐ 15 · Python · MIT · 推送 2026-07-29 · [GitHub](https://github.com/cohere-ai/north-mcp-python-sdk) · 组织维护

**Cohere North 平台的 MCP 服务器 Python SDK，含认证扩展**

基于原 MCP Python SDK 的扩展，用于构建接入 North 平台的 MCP 服务器：通过 North ID Token 验证用户身份，可用 trusted_issuers 限定身份提供方，获取用户 OAuth token 以代理访问第三方服务；仅支持 StreamableHTTP 传输（sse 已弃用仅为兼容保留）。另提供内置 /health 健康检查端点、认证调试模式与 OpenTelemetry 可观测性辅助（不捆绑 exporter）。需 Python 3.11+，通过 uv 从 GitHub 源码安装，支持用 MCP Inspector 本地测试。

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

- North ID Token 用户身份验证与 trusted_issuers 白名单
- 代理访问第三方服务的用户 OAuth token
- 内置 /health 健康检查端点（默认启用）
- OpenTelemetry 辅助（自定义 span、日志/trace 关联、隐私感知错误记录）

## 适用场景

- 为 North 平台开发带认证的 MCP 工具服务器
- 让 MCP 工具代表用户访问 Google Drive、Slack 等第三方服务
- 在 Kubernetes 中部署带存活探针的 MCP 服务器

## 场景标签

 · 领域:开发者工具/Agent 基础设施

## 证据(README 行号)

> L3: This SDK builds on top of the original SDK. Please refer to the original repository's README for general information
> L11: ## Why this repository
> L12: This repository provides code to enable your server to use authentication with North, a custom extension to the ori

## 星数曲线

```mermaid
xychart-beta
    title "cohere-ai/north-mcp-python-sdk 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `cd8ea524054a` · [字段定义](../../DATASET.md)*
