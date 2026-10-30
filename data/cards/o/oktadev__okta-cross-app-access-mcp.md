# oktadev/okta-cross-app-access-mcp

⭐ 25 · TypeScript · Apache-2.0 · 推送 2026-07-30 · [GitHub](https://github.com/oktadev/okta-cross-app-access-mcp) · [官网](https://www.okta.com/integrations/cross-app-access/) · 组织维护

**概念验证：MCP 客户端经 Identity Assertion 授权访问跨应用资源**

由 oktadev 维护的 Node.js 概念验证项目，演示 MCP（Model Context Protocol）利用 Identity Assertion Authorization Grant 规范，在企业现有身份基础设施下实现 MCP 客户端的安全互操作授权。场景为 AI agent 应用（Agent0）经授权访问独立 Todo 应用（Todo0）的资源，无需用户分别登录。运行依赖 Docker Desktop、VS Code Dev Containers，需配置 Okta OIDC 凭据与 AWS 密钥，通过 yarn 命令安装依赖、初始化数据库并并行启动前后端服务。

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

- 基于 Identity Assertion Authorization Grant 规范的 MCP 授权演示
- Agent0 经授权访问 Todo0 资源，无需用户分别认证
- 提供 VS Code Dev Containers 与 GitHub Codespaces 两种运行方式
- yarn 命令一键安装依赖、重置种子数据库并并行启动服务

## 适用场景

- 了解 MCP 客户端在企业身份基础设施下的授权集成模式
- 参考 OAuth2 跨应用访问（Cross App Access）的实现方式
- 在本地或 Codespaces 中运行并验证 agent 跨应用访问流程

## 场景标签

 · 领域:身份认证/AI 基础设施

## 证据(README 行号)

> L9: A proof-of-concept demonstrating how a Model Context Protocol (MCP) can leverage the Identity Assertion Authorizatio
> L7: # Okta Cross App Access MCP - Node Example

## 星数曲线

```mermaid
xychart-beta
    title "oktadev/okta-cross-app-access-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a82f98dd5a27` · [字段定义](../../DATASET.md)*
