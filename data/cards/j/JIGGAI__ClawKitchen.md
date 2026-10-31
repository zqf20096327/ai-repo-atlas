# JIGGAI/ClawKitchen

⭐ 19 · TypeScript · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/JIGGAI/ClawKitchen) · [官网](https://clawkitchen.ai) · 组织维护

**OpenClaw 多 agent 管理控制台插件（Web 仪表盘）**

面向 OpenClaw 用户的本地优先 Web 控制台插件：作为 @jiggai/kitchen 插件加载进 OpenClaw 网关，以 React/Next.js 仪表盘管理 agent、多 agent 团队、敏捷任务、目标跟踪与定时任务，并含实验性 Workflows（LLM 节点需启用 llm-task 插件）。通过 shell 调用本机 openclaw 命令工作，远程访问建议走 Tailscale 并强制 Basic Auth；停止方式为禁用插件并重启网关。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 以 OpenClaw 插件形式加载，提供浏览器仪表盘（127.0.0.1:7777）
- 管理 agent、多 agent 团队、敏捷任务、目标跟踪与 cron
- 实验性 Workflows，LLM 节点依赖内置可选插件 llm-task
- Tailscale 远程访问方案与 Basic Auth / KITCHEN_AUTH_MODE 三档认证

## 适用场景

- 在统一仪表盘里管理 OpenClaw 的多个 agent 与团队任务
- 通过 Tailscale 安全远程访问本地 OpenClaw 控制台
- 用工作流串联 LLM 任务节点（需启用 llm-task）

## 场景标签

 · 领域:AI agent 管理工具

## 证据(README 行号)

> L17: Local-first UI companion for **ClawRecipes** (OpenClaw Recipes plugin).
> L25: ClawKitchen can be loaded as an OpenClaw plugin so it runs locally on the orchestrator.

## 星数曲线

```mermaid
xychart-beta
    title "JIGGAI/ClawKitchen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `84fb88950c6c` · [字段定义](../../DATASET.md)*
