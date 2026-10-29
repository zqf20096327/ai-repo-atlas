# LeoYeAI/openclaw-guardian

⭐ 568 · Shell · MIT · 推送 2026-07-14 · [GitHub](https://github.com/LeoYeAI/openclaw-guardian) · [官网](https://myclaw.ai) · 组织维护 · 中文 README

**OpenClaw Gateway 的看护脚本：监控健康并自愈回滚**

源自 MyClaw.ai 生产基础设施的 Bash 看护工具：每 30 秒检查 OpenClaw Gateway 健康状态，失败时自动运行 `openclaw doctor --fix`（最多 3 次），修复失败则回滚工作区到最近一次稳定的 git 提交；另提供每日 git 快照与可选的 Discord webhook 告警。以 Bash 脚本形式运行，可经 git 初始化后安装，或通过 clawhub 以 OpenClaw Skill 方式安装。面向运行 OpenClaw 网关的用户，README 附有与 gw-watchdog 的功能对照表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30 秒间隔健康检查与最多 3 次 doctor --fix 自动修复
- 修复失败时回滚到最近稳定 git 提交
- 工作区每日自动 git 快照
- 可选 Discord webhook 失败/恢复告警

## 适用场景

- 我运行 OpenClaw Gateway，希望宕机时自动修复与回滚
- 我想为 AI agent 工作区保留每日快照备份
- 故障发生时我想在 Discord 收到通知

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L14: OpenClaw Guardian is an open-source project born from MyClaw.ai's production infrastructure. We run thousands of AI
> L21: - **Auto-repair** — runs `openclaw doctor --fix` on failure (up to 3 attempts)

## 星数曲线

```mermaid
xychart-beta
    title "LeoYeAI/openclaw-guardian 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28", "2026-10-29"]
    y-axis "stars" 566 --> 569
    line [568, 567, 568, 568]
```

2026-10-18 568 → 2026-10-29 568（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8c0a4e505db2` · [字段定义](../../DATASET.md)*
