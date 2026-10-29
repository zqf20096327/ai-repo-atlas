# epam/statgpt-admin-frontend

⭐ 18 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/epam/statgpt-admin-frontend) · [官网](https://statgpt.dialx.ai) · 组织维护

**StatGPT 平台的管理前端：管理数据源、数据集、渠道、文档与审计日志**

基于 Next.js 16 App Router、React 19、Nx 22 构建的 StatGPT 管理界面，用于管理数据源、数据集、通道、文档和审计日志，对接 StatGPT Backend API 与 AI DIAL Core API（文档与索引功能）。认证可选，通过 NextAuth.js 接入 Auth0、Azure AD、Google、Keycloak、Cognito、Okta 六种提供方；不设置认证时跳过会话校验直接提供页面。提供 npm 启动与 Docker 镜像两种运行方式。

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

- 管理 StatGPT 数据源、数据集、渠道、文档与审计日志
- 对接 StatGPT Backend API 与 AI DIAL Core API
- NextAuth.js 可选认证，支持 6 种 OIDC 提供方
- 提供 Docker 镜像，构建后以 node 直接运行

## 适用场景

- 运营人员在 Web 界面维护 StatGPT 的数据源与文档索引
- 企业按需启用 SSO 认证部署管理控制台
- 查看 StatGPT 平台的审计日志

## 场景标签

 · 领域:LLM 基础设施/管理界面

## 证据(README 行号)

> L3: StatGPT Admin Frontend is a Next.js application for administering StatGPT data sources, datasets, channels, document
> L123: |`API_URL`|Yes for main admin features|StatGPT Backend API URL. See StatGPT Backend.|`https://statgpt-backend.exam
> L124: |`DIAL_API_URL`|Yes for document and indexing features|AI DIAL Core API URL. See AI DIAL Core dynamic settings.|`h

## 星数曲线

```mermaid
xychart-beta
    title "epam/statgpt-admin-frontend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `5158dfbcf929` · [字段定义](../../DATASET.md)*
