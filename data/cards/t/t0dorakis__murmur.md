# t0dorakis/murmur

⭐ 32 · TypeScript · MIT · 推送 2026-02-10 · [GitHub](https://github.com/t0dorakis/murmur) · 个人维护

**定时调度 Claude/Codex/Pi agent 会话的 cron 守护进程**

基于 Bun/TypeScript/Effect-TS 编写的本地守护进程，按 interval 或 cron 表达式周期性以全新 CLI 调用运行 AI agent 会话。任务由工作区中的 HEARTBEAT.md 提示文件定义，支持 YAML frontmatter 配置调度、模型、超时与 agent 类型；支持 Claude Code（默认）、OpenAI Codex CLI 与 pi 三种 agent harness。守护进程以 TUI 前台或后台运行，结果追加记录到 heartbeats.jsonl。默认以 --dangerously-skip-permissions 运行但内置破坏性命令黑名单，建议容器/VM 中运行以求安全。

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

- HEARTBEAT.md 提示文件定义任务，frontmatter 覆盖 config.json 配置
- 支持 claude-code/codex/pi 三种 agent harness
- interval 与 cron 双调度方式，多 heartbeat 独立调度共存于一个仓库
- 结果以 ok/attention/error 三态记录到 heartbeats.jsonl

## 适用场景

- 定时让 agent 巡查 GitHub issues 并汇总提醒
- 每日自动检索 arXiv 论文并写入笔记
- 周期性抓取竞品 changelog 做变更监控

## 场景标签

`科研工具` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L10: The agent cron daemon. Schedule automated Claude/Codex/Pi sessions that run on intervals or cron expressions — each
> L178: ## Agent Harnesses
> L180: Murmur supports multiple AI agent harnesses, allowing you to choose the best tool for each heartbeat:

## 星数曲线

```mermaid
xychart-beta
    title "t0dorakis/murmur 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `424827754d73` · [字段定义](../../DATASET.md)*
