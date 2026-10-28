# tumf/conflux

⭐ 27 · Rust · 推送 2026-09-23 · [GitHub](https://github.com/tumf/conflux) · [官网](https://dev.to/tumf/conflux-release-a-spec-driven-orchestrator-for-parallel-ai-development-2gbc) · 个人维护 · 中文 README

**编排 AI 编码代理做规格驱动自主开发的 Rust 工具**

基于 OpenSpec 规格驱动开发的自主开发编排器：AI 编码代理在无持续人工监督下逐条处理变更，走完申请、验收、归档到最终合并的全流程。机制上用多层 Ralph 循环压缩每次交接的上下文，用 git worktree 为每个变更分配独立工作树实现并行开发，实现与验收角色可分离并组合不同代理（Claude Code、Codex、OpenCode 可替换）。提供 TUI、headless 运行、REST API 与 stdio MCP 服务端，另有 cflx client 委托模式供外部代理向已有 owner 提交控制命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenSpec 规格驱动：变更经申请、验收、归档、合并全流程自动推进
- git worktree 并行：每个变更独立工作树，多个变更并行处理
- 实现与验收代理可分离组合，不绑定特定 AI 供应商
- cflx client 提供 JSON 命令与 stdio MCP 服务端（3 个工具）供外部代理委托

## 适用场景

- 让 AI 编码代理按规格持续自主迭代，逐步累积出成品
- 并行推进多个规格变更并自动验收合并
- 外部 agent 通过 MCP/API 委托已有 Conflux 进程执行变更

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L19: Conflux is a tool that orchestrates autonomous development by AI coding agents based on specification-driven develo
> L33: - **Multi-layer Ralph loops**: Conflux improves through repeated iteration while keeping the context handed off in 

## 星数曲线

```mermaid
xychart-beta
    title "tumf/conflux 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d445681ae341` · [字段定义](../../DATASET.md)*
