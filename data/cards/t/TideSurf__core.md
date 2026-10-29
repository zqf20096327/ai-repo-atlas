# TideSurf/core

⭐ 21 · TypeScript · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/TideSurf/core) · [官网](https://tidesurf.org) · 组织维护

**把 Chromium 网页压缩成 50-200 token 结构文本供 LLM agent 调用**

通过 Chrome DevTools Protocol 连接 Chromium 的工具层：将每个页面的实时 DOM 压缩为 50-200 token 的结构化文本读取结果，并通过统一注册表向 agent CLI、SDK 和 MCP 暴露 20 个工具。以 MCP 服务器、Agent Skill 或 Agent Plugin 形式安装进任意 agent，并可托管用户自己的插件与技能，替代对全能视觉模型的依赖。提供 brew 与 npm 两种安装方式。README 可见信息较短，细节依赖 Docs（行号外）。

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

- 将实时 DOM 压缩为 50-200 token 的结构化文本
- 通过 Chrome DevTools Protocol 连接 Chromium
- 统一工具注册表暴露 20 个工具，覆盖 agent CLI、SDK 与 MCP
- 可作为 MCP 服务器、Agent Skill 或 Agent Plugin 安装，并托管自定义插件/技能

## 适用场景

- 让文本型 LLM agent 浏览网页而不依赖视觉模型
- 以 MCP 形式给 agent 增加浏览器操作工具
- 降低 agent 网页浏览的 token 消耗

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L16:  TideSurf connects Chromium to agents over the
> L19:  and exposes 20 tools through one registry shared by the agent CLI, the SDK, and MCP.
> L20:  Installs into any agent as an MCP server, an Agent Skill, or an Agent Plugin, and hosts your own plugins and skill

## 星数曲线

```mermaid
xychart-beta
    title "TideSurf/core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a92ee729ab06` · [字段定义](../../DATASET.md)*
