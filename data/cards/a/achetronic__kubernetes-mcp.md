# achetronic/kubernetes-mcp

⭐ 42 · Go · Apache-2.0 · 推送 2026-06-30 · [GitHub](https://github.com/achetronic/kubernetes-mcp) · 个人维护

**面向 AI 助手的 Kubernetes MCP 服务器，带过滤与细粒度 RBAC**

用 Go 编写的 MCP 服务器，向 AI 助手暴露 25 个 Kubernetes 工具（读、改、扩缩、调试、多集群上下文切换、指标等），支持 stdio 与 streamable-http 传输。关键机制：所有工具支持 yq 表达式过滤响应以节省上下文窗口；基于 CEL 的规则型 RBAC（按工具/上下文/API 组/资源/命名空间/名称，默认拒绝、拒绝优先）；OAuth 2.1/JWKS JWT 校验与静态 API key 认证。提供本地二进制、Docker 与 Helm 三种部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 25 个 Kubernetes 工具覆盖读写、扩缩、调试、多集群管理
- yq 表达式过滤响应，节省 AI 上下文窗口
- CEL 规则型细粒度 RBAC：默认拒绝、拒绝优先、支持通配符
- OAuth 2.1 (RFC 8414/9728)、JWT+JWKS、API key 认证，可安全对外暴露

## 适用场景

- 让 Claude 等 AI 助手通过自然语言管理 Kubernetes 集群
- 在受限 RBAC 策略下让 AI 安全操作生产集群
- 通过一个端点管理多个集群并按上下文切换

## 场景标签

 · 领域:云原生/DevOps 工具

## 证据(README 行号)

> L21:  🎯 25 Kubernetes Tools
> L141: The MCP server exposes the protocol under `/mcp` (POST, JSON-RPC) and OAuth

## 星数曲线

```mermaid
xychart-beta
    title "achetronic/kubernetes-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9ec1f71a53e8` · [字段定义](../../DATASET.md)*
