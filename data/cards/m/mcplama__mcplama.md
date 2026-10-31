# mcplama/mcplama

⭐ 14 · JavaScript · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/mcplama/mcplama) · [官网](https://mcplama.com) · 组织维护

**自托管 MCP 网关：集中管理团队 MCP 服务器的凭证、权限与审计**

面向开发者和团队的开源自托管 MCP 网关与控制平面：在统一位置管理多个 MCP 服务器的生命周期、OAuth/API 凭证、用户与服务访问策略、连接与审计事件。AI 客户端通过受控的连接 URL 接入，网关解析令牌、校验来源、注入凭证、写审计日志后代理请求。MCP 容器由独立的 broker 进程启动，网关自身不持有 Docker socket。以 Docker 镜像方式部署，成员门户使团队成员可连接服务器而不接触底层凭证。生产部署需自备密钥并置于 HTTPS 反向代理之后。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每用户×服务器独立连接令牌，底层凭证保留在网关端
- MCP 调用活动日志与管理变更审计日志分离，不记录密钥值
- broker 进程隔离执行 MCP 容器，网关自身无 Docker 访问权
- 兼容 Claude Desktop、VS Code + GitHub Copilot、Cursor 等 MCP 客户端

## 适用场景

- 团队统一托管多个 MCP 服务器，避免凭证分散在各开发机
- 为 AI 客户端统一发放和撤销 MCP 服务器访问权限
- 审计成员的 MCP 调用与凭证、策略等管理变更

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L12: MCPlama is a self-hosted MCP gateway and control plane for developers and teams who want to run multiple MCP server
> L128: When an AI client connects through MCPlama, the gateway:

## 星数曲线

```mermaid
xychart-beta
    title "mcplama/mcplama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a7564c37fe5f` · [字段定义](../../DATASET.md)*
