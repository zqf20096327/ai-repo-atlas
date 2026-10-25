# qelos-io/qelos

⭐ 54 · TypeScript · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/qelos-io/qelos) · [官网](https://qelos.io) · 组织维护

**AI 优先的应用层网关：为应用提供后端 API、AI agent 与权限管理**

面向应用开发者的后端平台：以 API 网关为核心，通过 blueprints 定义数据模型即获得 CRUD 接口，并内置 AI agent 创建与管理（可配置工具/函数、经 SDK 或 widget 嵌入）、社交登录认证、多租户工作区、资源级权限与事件审计日志。提供 JS/TS 与 Python SDK、针对 Express/Next.js/Nuxt/Fastify/NestJS/FastAPI 的中间件及 CLI 脚手架；依赖 MongoDB，支持 Docker Compose 与 Kubernetes Helm 部署，本地贡献环境需 Node.js v20+ 与 pnpm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- blueprints 定义数据模型自动生成 CRUD + AI + auth 接口
- AI agent 管理：配置工具/函数，SDK 或 widget 嵌入
- 多租户工作区与资源级权限、事件审计日志
- JS/Python SDK、六种框架中间件与 CLI 脚手架

## 适用场景

- 为自己的前端应用快速获得带认证与权限的后端 API
- 创建并嵌入可调用工具的 AI 聊天 agent
- 多租户 SaaS 场景下隔离数据与成员管理

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: Qelos is an **AI-first application layer gateway**. It gives your application a
> L58: - **AI Agents** — create and manage chatbots, configure tools/functions, embed via SDK or widget

## 星数曲线

```mermaid
xychart-beta
    title "qelos-io/qelos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-25 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4cf04daf038a` · [字段定义](../../DATASET.md)*
