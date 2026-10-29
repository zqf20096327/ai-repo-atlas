# yandex-cloud/mcp

⭐ 49 · Apache-2.0 · 推送 2026-04-24 · [GitHub](https://github.com/yandex-cloud/mcp) · 组织维护

**让 AI 助手管理 Yandex Cloud 资源的官方 MCP 服务器集**

Yandex Cloud 官方维护的一组 MCP（Model Context Protocol）服务器，覆盖应用部署（Compute/VPC/IAM/S3/Managed YDB）、文档生成式检索、Yandex 网页搜索、Serverless 函数/容器/触发器/工作流/API 网关及数据目录等场景。用户将所选服务器接入 Cline、Roo Code 或 Claude Desktop 等助手配置后，通过对话管理云基础设施。支持 npm 客户端（stdio，OAuth 或 yc CLI 认证）与 Streamable HTTP（IAM token，12 小时有效期需轮换）两种接入方式，需 Node.js 18+ 与对应的云角色授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按功能分组的多个 MCP 服务器：部署、搜索知识、Serverless、数据平台
- npm 客户端（stdio）与 Streamable HTTP 两种接入方式
- OAuth 浏览器认证或 Yandex Cloud CLI 认证
- 支持对接 Cline、Roo Code、Claude Desktop 等助手配置

## 适用场景

- 通过 AI 助手对话式管理 Yandex Cloud 的 Serverless 函数与容器
- 让助手实时检索 Yandex Cloud 官方文档与网页搜索
- 非技术用户用 AI 快速搭建云上概念验证服务

## 场景标签

 · 领域:云计算/AI 工具集成

## 证据(README 行号)

> L3: Specialized MCP servers for interacting with Yandex Cloud using the MCP protocol.
> L63: To connect your assistant with MCP servers, you have to update your assistant's configuration (e.g. Cline, Roo Code

## 星数曲线

```mermaid
xychart-beta
    title "yandex-cloud/mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-29 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a5ffe0e79b5e` · [字段定义](../../DATASET.md)*
