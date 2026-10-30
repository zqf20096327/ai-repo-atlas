# appautomaton/automaton

⭐ 24 · JavaScript · MIT · 推送 2026-09-13 · [GitHub](https://github.com/appautomaton/automaton) · [官网](https://appautomaton.com/automaton/) · 个人维护 · 中文 README

**给 Claude Code/Codex/OpenCode 装上阶段化工作流的 AI 编码 harness**

面向 LLM 驱动编码工具（Claude Code、Codex、OpenCode）的便携式、阶段门控 harness：通过 npx 安装 markdown 技能、启动集成与 `.agent/` 持久状态目录到目标项目，使跨会话、跨上下文窗口的长任务通过 frame→plan→execute→verify 显式阶段推进并保留交接状态。安装为本地明文 markdown 拷贝，重装时从源刷新；提供 status/validate/uninstall 命令，并可检测安装副本与 CLI 源的漂移。MIT 许可。

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

- 同一工作流覆盖 Claude Code、Codex、OpenCode 三个宿主
- frame→plan→execute→verify 阶段门控，SPEC.md 由用户审批作为产品评审
- `.agent/` 持久状态：current.json/SPEC.md/PLAN.md/ROADMAP.md
- copy-based 安装，技能为可检视的本地明文 markdown

## 适用场景

- 让编码 agent 的长任务在会话重启和上下文耗尽后可续接
- 跨多个 AI 编码工具复用同一套结构化工作流
- 对 agent 变更实施先定规格再执行验证的流程

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: Portable, stage-gated agentic-AI harness for Claude Code, Codex, and OpenCode.
> L10: An AI coding agent framework that gives LLM-powered development tools structured workflows for long-running tasks. 
> L16: - Use the same workflow across Claude Code, Codex, and OpenCode.

## 星数曲线

```mermaid
xychart-beta
    title "appautomaton/automaton 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-30 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `674f28066f18` · [字段定义](../../DATASET.md)*
