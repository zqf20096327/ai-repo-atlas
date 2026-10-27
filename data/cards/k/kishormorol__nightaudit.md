# kishormorol/nightaudit

⭐ 30 · Python · MIT · 推送 2026-09-16 · [GitHub](https://github.com/kishormorol/nightaudit) · [官网](https://nightshift-site-production.up.railway.app/) · 个人维护

**夜间定时调用 Claude Code/Codex 订阅做只读代码审查的工具**

面向已有 Claude Code 或 Codex 订阅的开发者 CLI 工具：由 cron 触发、无守护进程，在用户设定的时段内驱动已安装的 claude/codex CLI 对指定仓库做多项目轮询审查，只读性由 CLI 自身权限层（Claude Code allowlist 或 Codex 内核沙箱）强制执行。按提供方维护每日/每周 token 预算账本，产出按严重度排序、带 file:line 的单一 Markdown 晨间摘要。通过 pipx 安装（PyPI 包名为 nightshift-cli），提供 init/run/status 命令与自建检查任务扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 驱动用户已付费的 claude/codex 订阅进行审查，无需 API key
- 只读性由 Claude Code allowlist 或 Codex 内核沙箱强制执行
- 每提供方按日/周硬性预算记账，多仓库轮询防饿死
- 产出按严重度排序、带 file:line 的晨间 Markdown 摘要

## 适用场景

- 夜间自动审查多个仓库，早上看一份汇总摘要
- 利用闲置的 Claude Code/Codex 订阅额度做定时代码审查
- 按预算控制各提供方的 token 消耗

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: Put your idle Claude Code or Codex subscription to work — read-only reviews of
> L29: It never edits your code. It has no daemon and no server — cron calls it, it
> L38: - **Read-only, and not on the honour system.** Enforced by the AI CLI's own

## 星数曲线

```mermaid
xychart-beta
    title "kishormorol/nightaudit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `23fe7eeb51c6` · [字段定义](../../DATASET.md)*
