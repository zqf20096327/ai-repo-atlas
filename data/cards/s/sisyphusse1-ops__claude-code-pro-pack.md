# sisyphusse1-ops/claude-code-pro-pack

⭐ 35 · HTML · MIT · 推送 2026-05-10 · [GitHub](https://github.com/sisyphusse1-ops/claude-code-pro-pack) · [官网](https://sisyphusse1-ops.github.io/claude-code-pro-pack/) · 个人维护

**面向 AI 编码 agent 的 12 条行为规则 CLAUDE.md/AGENTS.md 文件包**

提供可直接复制到项目根目录的 CLAUDE.md 与 AGENTS.md 行为规则文件及 5 个示例技能模板，覆盖 Claude Code、Codex、Cursor、Hermes Agent 等编码 agent。规则源自 30+ 代码库中的 agent 失败模式整理，共 12 条（含 token 预算、可见失败、外科手术式修改等），总计约 700 token。在 Karpathy 原 4 规则基础上扩展 8 条。安装方式为复制文件并提交到仓库，无框架依赖，MIT 许可。

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

- 12 条规则文件（CLAUDE.md / AGENTS.md 两种变体），约 700 token
- 附 5 个示例技能模板，可复制到 .claude/skills/
- 规则与 30+ 代码库中的 agent 失败模式对应
- 提供 cc-audit Python 检查器可在 CI 中给 CLAUDE.md 打分

## 适用场景

- 给 Claude Code/Codex 等 agent 加一层行为约束，减少编码失误
- 在 CI 中用 cc-audit 审计团队现有 CLAUDE.md 规则覆盖
- 作为项目内 agent 行为基线，与领域技能库分层配合

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Battle-tested behavior rules, prompts, and reusable skill templates for AI coding agents — Claude Code, Codex, Curso
> L13: ├── CLAUDE.md                          # 12-rule behavior file — drop in project root
> L20: 1. Copy `CLAUDE.md` (or `AGENTS.md` for Codex) into your project root.

## 星数曲线

```mermaid
xychart-beta
    title "sisyphusse1-ops/claude-code-pro-pack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-25 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `df9146d1c024` · [字段定义](../../DATASET.md)*
