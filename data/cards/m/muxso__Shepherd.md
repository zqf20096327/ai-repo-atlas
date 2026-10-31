# muxso/Shepherd

⭐ 14 · Rust · GPL-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/muxso/Shepherd) · 组织维护 · 中文 README

**监督 AI 开发全流程的工程平台：需求拆解、人工审批门与验证**

面向团队治理 AI 驱动软件交付的平台：将需求分解为任务 DAG，由内部 executors 主动认领执行（agent-runtime 以 shell 方式调用 Claude Code / Codex / OpenCode 等），在设计门与验证门两处强制人工审批，未过门不进主分支。提供 AI/人工交付占比、一次通过率等以人工验证为口径的度量，附测试管理套件与飞书/钉钉/企微通知。Rust 实现，Docker Compose 一键起全栈；自述 v0.0.4 实验阶段、未达生产可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 需求→设计→任务 DAG→执行→验证门的全流程监督，人工审批为硬性步骤
- executors 通过长轮询主动认领任务，支持 Redis Streams 的单机/多机队列
- 以人工验证为口径的 AI 交付度量（AI 占比、一次通过率、贡献日历）
- MCP server 暴露 shepherd_* 工具供 agent 驱动需求→验证生命周期

## 适用场景

- 团队在引入 AI 编码后仍需对交付结果做审批与验证把关
- 度量各项目中 AI 实际交付并经人工验证的占比
- 在无公网入站的内网机器上调度多个 AI 编码执行器

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L13: Shepherd is a platform for supervising AI-driven development. AI can write code, but it won't judge whether it actu
> L107: **vs. agent harnesses — Claude Code, Codex, OpenCode, OpenHands, Aider.** A harness wraps an LLM and runs the agen

## 星数曲线

```mermaid
xychart-beta
    title "muxso/Shepherd 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `87b56ad7feab` · [字段定义](../../DATASET.md)*
