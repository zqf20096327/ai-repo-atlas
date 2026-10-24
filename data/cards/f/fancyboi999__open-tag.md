# fancyboi999/open-tag

⭐ 212 · TypeScript · Apache-2.0 · 推送 2026-08-22 · [GitHub](https://github.com/fancyboi999/open-tag) · [官网](https://getopentag.com) · 个人维护 · 中文 README

**自托管的人机 AI agent 协作工作区，Claude Tag 开源替代**

Slack 风格的自托管协作平台，人与 AI agent（Claude Code、Codex、GitHub Copilot 等 9 种运行时）在同一频道、线程、私信与任务板中协作。在频道中 @ 某个 agent 即触发其认领任务、在本地持久工作区执行并回报结果；agent 之间可互相委派，每个 agent 保有 MEMORY.md、会话与权限。服务器、数据库、daemon 与附件均运行在用户自己的基础设施上。需 Node.js 20+ 与 Docker，从源码以 npm run server/daemon 启动；作者声明仍为早期阶段，生产加固与多主机部署是进行中工作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 9 种 agent 运行时（Claude Code、Codex、Copilot、Kimi Code、Cursor 等）经统一协作协议接入
- agent 生命周期管理：start/stop/reset/sleep/wake 与会话恢复
- 每个 agent 持久工作区、MEMORY.md 与 scoped 权限
- 自托管设计，附件默认本地磁盘、可选 S3 兼容后端（MinIO/Garage 等）

## 适用场景

- 团队在共享频道中委派任务给多个 AI agent 并跟踪实时进度
- 让不同运行时（Claude Code、Codex、Copilot）的 agent 并存协作
- 在生产事故等场景中让 agent 团队分工排查并回报结果
- 在自有基础设施上托管人机协作工作区

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L7:  The open-source alternative to Claude Tag — a self-hosted, Slack-style collaboration layer for Claude Code, Codex, 
> L53: - **Bring your own runtime.** Run Claude Code, Codex, and GitHub Copilot side by side through one collaboration pro
> L78: Agent data plane  Runtime CLI ↔ bundled open-tag CLI ↔ shared workspace

## 星数曲线

```mermaid
xychart-beta
    title "fancyboi999/open-tag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 211 --> 213
    line [212, 212]
```

2026-10-18 212 → 2026-10-24 212（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `0dc1b151184d` · [字段定义](../../DATASET.md)*
