# chojs23/lazyagent

⭐ 79 · Go · MIT · 推送 2026-05-23 · [GitHub](https://github.com/chojs23/lazyagent) · 个人维护

**观测 Claude/Codex/OpenCode 编码 agent 会话的 TUI/Web 工具**

面向日常可观测性的终端 TUI 与只读 Web 仪表盘：通过 runtime hooks 与插件从 Claude、Codex、OpenCode 三种编码 agent 采集事件，存入 SQLite，以五窗格界面展示项目、会话、agent/subagent 树、事件流与事件详情。支持事件类型过滤与全文搜索、代码与 diff 语法高亮、按会话的 token 用量审计（模型调用、缓存读/写、工具与 shell 命令统计）。提供 npm、Homebrew、go install、Nix、安装脚本与源码构建等安装方式。README 声明仍处早期开发，可能有不兼容变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多 runtime 支持：Claude、Codex、OpenCode 会话统一观测
- subagent 层级以可视化树呈现，事件按类型过滤并可全文搜索
- token 用量 overlay：模型调用、缓存读/写、工具与 shell 命令统计
- 只读 Web 仪表盘与 TUI 共享同一 SQLite 存储

## 适用场景

- 在一个界面查看多个项目的 AI 编码 agent 会话与工具调用
- 核对各 agent 是否在履行其角色、发现跑偏的运行
- 按会话审计 token 成本与缓存节省情况

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L7: `lazyagent` is a tui/web app for watching what ai agents are doing. You can inspect projects, sessions, agents, suba
> L19: - **Multi-runtime support** -- Support Claude, Codex, and OpenCode sessions

## 星数曲线

```mermaid
xychart-beta
    title "chojs23/lazyagent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-31 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `53cc3f516337` · [字段定义](../../DATASET.md)*
