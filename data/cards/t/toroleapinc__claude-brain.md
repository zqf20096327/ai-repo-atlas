# toroleapinc/claude-brain

⭐ 91 · Shell · MIT · 推送 2026-06-09 · [GitHub](https://github.com/toroleapinc/claude-brain) · [官网](https://toroleapinc.github.io/claude-brain/) · 组织维护 · 中文 README

**跨机器同步 Claude Code 记忆/技能/规则等配置的插件，带语义合并**

Claude Code 插件，通过 Git 远端仓库在多台机器间同步 CLAUDE.md、规则、技能、agents、记忆与设置。核心机制：结构化数据用确定性 JSON 深合并，非结构化内容（记忆、CLAUDE.md）用 claude -p 做 LLM 语义合并（去重、消解矛盾）；通过 SessionStart/SessionEnd 钩子自动同步。支持 N 方合并、可选 age 加密、团队共享技能/规则、自动将稳定记忆模式提升为配置。安全上不导出 OAuth token、API key、环境变量，要求私有仓库。限制：不支持 Windows 原生（需 WSL）与 Claude Code Cloud；语义合并产生 API 费用（月约 $0.50–2.00）。

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

- 跨机器同步 Claude Code 记忆、技能、agents、规则、设置等
- 结构化数据 JSON 深合并 + 非结构化内容 LLM 语义合并
- SessionStart/SessionEnd 钩子自动同步，无中心服务器，Git 负责传输
- 可选 age 加密、团队共享命名空间、密钥与环境变量不导出

## 适用场景

- 在办公本、台式机、云 VM 之间保持 Claude Code 配置一致
- 把稳定出现的记忆模式自动提升为持久配置
- 向团队成员共享技能、agents 和规则

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7:  claude-brain is a Claude Code plugin for brain sync — sync Claude Code memory, skills, agents, rules, and settings 
> L176: claude-brain runs as a local plugin that hooks `SessionStart`/`SessionEnd` to shell out to `git` and read/write `~

## 星数曲线

```mermaid
xychart-beta
    title "toroleapinc/claude-brain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 90 --> 92
    line [91, 91]
```

2026-10-18 91 → 2026-10-25 91（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e22906edd5d6` · [字段定义](../../DATASET.md)*
