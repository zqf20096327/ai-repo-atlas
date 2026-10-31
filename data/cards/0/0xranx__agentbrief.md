# 0xranx/agentbrief

⭐ 45 · HTML · MIT · 推送 2026-03-28 · [GitHub](https://github.com/0xranx/agentbrief) · [官网](https://0xranx.github.io/agentbrief) · 个人维护 · 中文 README

**给 AI 编程助手注入领域专家角色的可插拔 brief 集合**

面向 Claude Code、Cursor、OpenCode、Codex 等 AI 编程代理的工具：将角色定义（brief = 人格 + 知识 + 技能）编译为各引擎读取的指令文件（CLAUDE.md、.cursorrules、AGENTS.md），并按引擎做内容长度适配；已有文件通过标记注入方式保留，eject 可仅移除 brief 内容。提供 20 余个官方 brief（安全审计、代码评审、QA、Next.js、增长、产品等）与组合包，官方 brief 策展自社区技能仓库；支持 init 脚手架创建自有 brief 并经 GitHub 分发。npm 全局安装使用。

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

- 一条命令将 brief 编译为各代理引擎的指令文件，四种引擎各有内容适配策略
- 20+ 官方 brief 覆盖工程、产品、增长等方向，另有三组组合包
- 标记注入保留已有配置文件，eject 仅移除 brief 内容
- agentbrief init 脚手架 + github: 前缀支持自建 brief 分发

## 适用场景

- 让我的 Claude Code / Cursor 按特定领域专家标准做代码评审或安全审计
- 给编程代理一键装配多种技能（如全栈规范、QA、CI/CD）
- 用脚手架为团队定制专属角色并经 GitHub 共享

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: > One command turns your AI coding agent into a domain specialist.
> L96: AgentBrief compiles a **brief** (role + knowledge + skills) into the instruction files your AI agent reads, with co

## 星数曲线

```mermaid
xychart-beta
    title "0xranx/agentbrief 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-31 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a73ae5bd9205` · [字段定义](../../DATASET.md)*
