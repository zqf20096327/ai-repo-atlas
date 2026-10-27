# cld-maindev/codex-synaptic

⭐ 30 · TypeScript · AGPL-3.0 · 推送 2026-03-07 · [GitHub](https://github.com/cld-maindev/codex-synaptic) · 个人维护

**面向 Codex 工作流的运维编排层：CLI 守护进程、终端面板与 MCP 桥接**

以 TypeScript 编写的 Codex 工作流编排项目：围绕 Codex for macOS（Local/Worktree/Cloud 模式）提供 CLI 守护进程化运行控制、一次性命令模式、实时终端面板，以及 mcp-filesystem、mcp-playwright、mcp-desktop-commander 三个 MCP 外部桥接配置；含运行时权限守卫、沙箱与审批的安全基线、提示结构模板与文档索引。构建依赖 Node 环境与 npm。README 未展示描述中提及的群体智能算法与共识机制的安装或运行细节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Codex App + CLI + MCP 闭环编排 Local/Worktree/Cloud 三种工作流
- 内置三个 MCP 配置（文件系统、浏览器自动化、桌面命令桥）
- 提供沙箱与按需审批的安全基线与提示结构模板
- CLI 默认一次性执行模式，可配置保持前台会话调试

## 适用场景

- 团队以统一 CLI 与守护进程方式运行 Codex 工作流
- 通过 MCP 桥接将 Codex 接入外部编排与浏览器自动化流程
- 为 Codex 任务设定安全沙箱与审批策略

## 场景标签

`浏览器自动化` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: Operator-grade orchestration for Codex workflows: daemon-backed runtime control, live terminal dashboards, and MCP-

## 星数曲线

```mermaid
xychart-beta
    title "cld-maindev/codex-synaptic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `7d67812e7bf9` · [字段定义](../../DATASET.md)*
