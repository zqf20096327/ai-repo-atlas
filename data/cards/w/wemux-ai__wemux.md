# wemux-ai/wemux

⭐ 165 · TypeScript · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/wemux-ai/wemux) · [官网](https://wemux.ai) · 组织维护 · 中文 README

**自托管 AI agent 协作平台：人在环中编排 agent 执行真实编码工作**

Apache-2.0 开源的 agent 协作平台社区版：控制平面负责需求理解、任务规划、路由与审核，实际编码工作始终在用户自有 worker 机器上以隔离 Git worktree 执行，代码不离开本机。支持看板任务、工作区实时协作、群聊、飞书/Slack/钉钉/企微/微信/WhatsApp 渠道接入、多机组网与 Electron/移动端原生客户端。模型采用 BYOK，编排 OpenCode/Claude Code/Codex 运行时，推理发生在用户所选模型提供方。托管模型网关、计费等为独立商业服务，不在此仓库内。

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

- Worker 优先执行：代码在自有机器的隔离 Git worktree 中运行，控制平面不执行代码
- BYOK 模型配置，编排 OpenCode / Claude Code / Codex 运行时
- 飞书/Slack/钉钉/企微/微信/WhatsApp 多渠道接入与多节点组网
- 提供 Electron 桌面端与 React Native Android/iOS 客户端

## 适用场景

- 自建 agent 团队承担编码任务并保留人工 diff 审核环节
- 通过 IM 渠道用自然语言创建并分发任务给 agent
- 让代码在自有机器与凭证上执行，满足数据不出本机的要求

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L15: Wemux is an open-source agent collaboration platform. It orchestrates AI agents that execute real coding work on **
> L31: - **BYOK model config** — agents run on your own model keys via OpenCode/Claude Code/Codex runtimes on the worker.

## 星数曲线

```mermaid
xychart-beta
    title "wemux-ai/wemux 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 162 --> 166
    line [163, 164, 165]
```

2026-10-18 163 → 2026-10-24 165（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `08d78459e5e7` · [字段定义](../../DATASET.md)*
