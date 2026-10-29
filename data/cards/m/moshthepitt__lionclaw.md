# moshthepitt/lionclaw

⭐ 19 · Rust · MIT · 推送 2026-10-01 · [GitHub](https://github.com/moshthepitt/lionclaw) · [官网](https://lionclaw.co.ke) · 个人维护

**本地控制平面：以受限、可审计方式运行 AI 编码 agent CLI**

用 Rust 编写的本地控制平面，将 Codex、OpenCode 等 agent CLI 作为项目助手运行：以 `.lionclaw/` 目录承载项目身份、实例、运行时配置、持久会话、技能、通道与调度任务；通过 Podman 容器沙箱限定 agent 的工作区、挂载、网络与凭证，并记录审计轨迹。提供操作台 TUI、纯文本路径与运行时原生 TUI 三种交互方式；支持通道技能接入外部传输、定时任务投递结果、显式挂载管理与只读诊断命令 doctor。安装需 git clone 后 cargo build 编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Podman 容器为沙箱边界运行 Codex/OpenCode 等 agent CLI
- 项目级 `.lionclaw/` 目录管理实例、运行时配置、技能、通道与任务
- 操作台 TUI / plain / runtime-tui 三种运行路径，均经过统一审计与凭证暂存
- 通道与技能在 Rust 核心之外运行，网络策略限定 on/none

## 适用场景

- 在本地以受限沙箱与显式权限运行 AI 编码 agent
- 为项目保留跨运行时的持久会话与审计记录
- 通过通道和定时任务让 agent 在后台完成并投递结果

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Codex is still Codex. OpenCode is still OpenCode. LionClaw is the local control
> L6: plane around them: project identity, runtime configuration, durable sessions,
> L116: The selected runtime still does the agent work. LionClaw owns the boundary

## 星数曲线

```mermaid
xychart-beta
    title "moshthepitt/lionclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5cf2622aa6cd` · [字段定义](../../DATASET.md)*
