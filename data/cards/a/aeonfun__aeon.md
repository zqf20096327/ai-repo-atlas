# aeonfun/aeon

⭐ 798 · JavaScript · MIT · 推送 2026-11-24 · [GitHub](https://github.com/aeonfun/aeon) · [官网](https://www.aeon.fun/) · 个人维护

**在 GitHub Actions 无人值守运行技能的 AI agent 框架**

Aeon 是一个以 SKILL.md 文件为技能单元的 agent 框架，通过 run-harness 契约将同一技能文件分发到九种 agent CLI（Claude Code、Grok、Codex、Cursor 等）执行，运行载体为用户自己的 GitHub Actions 仓库。提供浏览器端 Aeon Connect 配置面板与本地 `./aeon` CLI 两种上手方式，内置 93 个技能、六个技能包，含自愈循环（heartbeat/skill-repair/self-improve）、实例派生（spawn-instance）、cron 调度与安全护栏。运行需 Node.js 20+ 与 GitHub CLI。

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

- 93 个技能分布于 9 种 harness，同一 SKILL.md 跨引擎运行
- 无人值守 cron 调度，运行于用户自己的 GitHub Actions
- 自愈循环：模型评分每次运行并自动修复失效技能
- spawn-instance 将单实例派生为带隔离计费的实例集群

## 适用场景

- 定时让 agent 向自己的仓库提交 PR 或部署原型应用
- 批量扫描开源仓库漏洞并私下披露
- 搭建无需人工审批的定时研究与内容聚合流程

## 场景标签

`Agent 框架` `工作流自动化` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L1: AEON - the most autonomous agent framework. 93 skills across 9 harnesses (Claude Code, Grok, Codex, Pi, Vibe, Kimi, 
> L95:  Nine engines, one socket - a SKILL.md flows through run-harness into any of nine agent CLIs: Claude, Grok, Codex, 

## 星数曲线

```mermaid
xychart-beta
    title "aeonfun/aeon 星数(近 18 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-27", "2026-10-28", "2026-10-30", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-26"]
    y-axis "stars" 781 --> 799
    line [783, 782, 783, 784, 785, 787, 782, 789, 792, 791, 792, 793, 794, 793, 795, 796, 797, 798]
```

2026-10-24 783 → 2026-11-26 798（+15）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `b898fc6f733f` · [字段定义](../../DATASET.md)*
