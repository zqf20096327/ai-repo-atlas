# yoda-digital/mcp-gitlab-server

⭐ 65 · TypeScript · MIT · 推送 2026-08-12 · [GitHub](https://github.com/yoda-digital/mcp-gitlab-server) · [官网](https://opensource.yoda.digital/en/projects/mcp-gitlab-server/) · 组织维护

**面向 AI agent 的 GitLab MCP 服务器，86 个工具直连 GitLab API**

由 Yoda Digital 维护的 Model Context Protocol 服务器，把 GitLab REST API 以 86 个类型化、分页、schema 校验的工具暴露给 MCP 客户端（Claude Desktop、Cursor、Zed、VS Code 等），覆盖仓库、文件、合并请求、CI/CD、群组、wiki 等操作。支持 gitlab.com 与自托管实例，认证支持 PAT（仅回环）与按连接转发的 OAuth Bearer 两种模式；传输层提供 stdio / SSE / Streamable HTTP 三种。提供 Docker 镜像与带校验守卫的 Helm chart，另有注册期过滤写工具的只读模式。

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

- 86 个 MCP 工具覆盖仓库、文件、MR、CI/CD、群组、wiki 等 GitLab 操作面
- stdio / SSE / Streamable HTTP 三种传输，PAT 与 OAuth 两种认证模式
- 只读模式在工具注册期过滤所有写操作
- 提供 ghcr.io Docker 镜像与含 5 个 fail-loud 守卫的 Helm chart

## 适用场景

- 让 Claude Desktop / Cursor 等 MCP 客户端直接操作 GitLab 项目与流水线
- 团队共享部署一个 MCP 网关供多 agent 接入企业 GitLab
- 在无写权限的安全演示环境中让 agent 浏览 GitLab 资源

## 场景标签

 · 领域:开发运维/LLM 基础设施

## 证据(README 行号)

> L35: GitLab MCP Server lets an AI agent (Claude Desktop, Claude Code, Cursor, Zed, VS Code, or any Model Context Protoco
> L45: A year on the project has 86 tools, working stdio / SSE / Streamable HTTP transports, PAT and OAuth modes, a Docker

## 星数曲线

```mermaid
xychart-beta
    title "yoda-digital/mcp-gitlab-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-29 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cda1cbca9128` · [字段定义](../../DATASET.md)*
