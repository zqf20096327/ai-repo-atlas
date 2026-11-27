# HieuAnh87/sentry-selfhosted-mcp

⭐ 10 · TypeScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/HieuAnh87/sentry-selfhosted-mcp) · [官网](https://hieuanh87.github.io/sentry-selfhosted-mcp/) · 个人维护

**供 AI 编码助手接入自托管 Sentry 的 MCP server**

一个 MCP server，让 AI 编码代理以节省 token 的方式访问自托管 Sentry 实例：提供 28 个工具，覆盖 issue、event、release、用户反馈、org 统计与项目诊断。针对单个 Sentry event 端点可返回超过 100,000 token 的问题，默认返回精简字段，按 50,000 token 预算截断超长响应，raw_sentry_api 在无 grep_pattern 且超预算时拒绝执行。需 Node.js 20+ 与 Sentry auth token，通过 npx 运行，配置 Claude Code/Cursor 客户端使用。

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

- 28 个工具覆盖 issue/event/release/attachment/trace 等查询与写入
- 50,000 token 预算截断与拒绝路径，避免撑爆模型上下文
- SENTRY_READ_ONLY 只读模式与按工具的 token scope 说明
- 字段白/黑名单、grep、栈帧截断等出站过滤

## 适用场景

- 让 AI 编码代理直接查询自托管 Sentry 的生产 issue 与堆栈
- 排查崩溃前的 breadcrumbs 与分组配置
- 只读授权给代理做事件诊断，避免误写 Sentry 数据

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: MCP server that gives AI coding agents **token-efficient** access to a self-hosted Sentry instance.
> L23: Node.js 20+ and a self-hosted Sentry instance (Sentry SaaS also works if the token and org slug are valid).

## 星数曲线

```mermaid
xychart-beta
    title "HieuAnh87/sentry-selfhosted-mcp 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `eaaf7aca0812` · [字段定义](../../DATASET.md)*
