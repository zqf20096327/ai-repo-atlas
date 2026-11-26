# reshaprio/reshapr

⭐ 180 · Java · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/reshaprio/reshapr) · [官网](https://reshapr.io) · 组织维护

**把现有 API 转为 MCP 工具的开源运行时，供开发者接入 LLM**

reShapr 是一个开源运行时，将既有 REST/GraphQL/gRPC 服务转换为受治理、可发现、上下文优化的 MCP 工具，无需重写 API 或为每个 API 搭建专属 MCP 服务器。针对 LLM 上下文窗口问题，提供 Context Control 在载荷进入 LLM 前过滤和精简。通过 npm 全局安装 CLI，本地依赖 Docker 以 `reshapr run` 启动平台容器，导入 OpenAPI 文件后即生成 MCP Server，可用 MCP 客户端连接使用。

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

- 将 REST/GraphQL/gRPC API 自动转换为 LLM 友好的 MCP 工具
- Context Control 在载荷到达 LLM 前过滤与精简上下文
- 导入现有契约即可生成 MCP Server，无需重写
- 提供 CLI、本地 Docker 部署与在线沙箱（try.reshapr.io）

## 适用场景

- 把存量微服务 API 暴露给 AI agent 调用
- 在 LLM 调用前精简 API 响应以节省 token
- 为多个 API 统一生成 MCP 工具而不用逐个写 server

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L17: **reShapr** is the open source runtime that turns your existing APIs AI-Native, without rebuilding them. It bridges
> L39: * Zero Rewrite: Import an existing contract and get working MCP tools in minutes, with no bespoke MCP server per AP
> L58: 3. **Contribute code / launch the Web UI (Developer):** Head to install/README.md to run the `docker-compose` stack

## 星数曲线

```mermaid
xychart-beta
    title "reshaprio/reshapr 星数(近 10 点)"
    x-axis ["2026-10-24", "2026-10-30", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-15", "2026-11-18", "2026-11-19", "2026-11-26"]
    y-axis "stars" 169 --> 181
    line [170, 171, 170, 173, 174, 175, 176, 179, 180, 180]
```

2026-10-24 170 → 2026-11-26 180（+10）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `ed47fe10fafc` · [字段定义](../../DATASET.md)*
