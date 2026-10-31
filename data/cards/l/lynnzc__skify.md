# lynnzc/skify

⭐ 41 · TypeScript · Apache-2.0 · 推送 2026-03-08 · [GitHub](https://github.com/lynnzc/skify) · 个人维护

**可私有部署的 AI 编程 agent 技能注册中心**

面向使用 AI 编程 agent 的团队的自托管技能注册平台：通过脚本部署到 Cloudflare Workers（D1+R2）或 Docker，支持技能的发布、版本管理、搜索与安装，并提供 npx skify CLI（add/publish/sync 等）与 Web UI。通过 skify sync 生成 AGENTS.md，使能读取 markdown 并执行 shell 命令的 agent（Cursor、Claude Code、GitHub Copilot 等）调用技能。提供 read/publish/admin 三级 RBAC 令牌，team 模式禁用匿名读取，Docker 方案支持离线部署。

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

- Cloudflare Workers 或 Docker 一键脚本部署的私有技能注册中心
- npx skify CLI 覆盖发布、搜索、安装、同步与令牌管理
- read/publish/admin 三级 RBAC API 令牌，team 模式关闭匿名读取
- skify sync 生成 AGENTS.md，供读取 markdown 的编程 agent 调用技能

## 适用场景

- 团队在内网或自有基础设施上托管私有 agent 技能
- 为 Cursor / Claude Code 等编程 agent 统一分发与更新技能
- 通过 Web UI 或 CLI 浏览、搜索并安装技能

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Deploy your own private skill management platform for AI coding agents
> L11: **skify** is a private skill registry you can deploy in minutes. Host your own skill packages for AI coding agents 
> L292: Works with any AI coding agent that can read markdown and run shell commands:

## 星数曲线

```mermaid
xychart-beta
    title "lynnzc/skify 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-31 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2f6f3a5d452b` · [字段定义](../../DATASET.md)*
