# MatheusKindrazki/clauderc

⭐ 15 · JavaScript · 推送 2026-04-06 · [GitHub](https://github.com/MatheusKindrazki/clauderc) · 个人维护

**为 Claude Code 生成最佳实践配置的 CLI 初始化工具**

面向 Claude Code 用户的配置脚手架：通过 npx 命令将 agents、skills、commands、templates 安装到全局 ~/.claude/ 或项目级 .claude/ 与 CLAUDE.md。项目模式提供交互式向导，自动检测 11+ 语言技术栈（Node/Python/Go/Rust/Java 等）及 monorepo、CI 配置，生成相应的 CLAUDE.md、权限 settings.json 和项目命令。另提供更新（带备份与 changelog）、列表查看等子命令，并附使用建议清单。跨 macOS/Linux/Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全局与项目两级配置（agents/skills/commands/templates）
- 自动检测 11+ 语言技术栈与 monorepo/CI 配置
- 交互式项目向导生成 CLAUDE.md 与权限 settings.json
- 更新时自动备份并展示版本间 changelog

## 适用场景

- 快速初始化 Claude Code 的全局与项目配置
- 为不同技术栈项目生成合适的 CLAUDE.md 上下文
- 团队统一维护和更新 Claude Code 配置组件

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3:  Setup Claude Code with best practices - agents, skills, commands, and templates.
> L34: Shared components available to all projects:
> L105: - Auto-detects stack, package manager, framework

## 星数曲线

```mermaid
xychart-beta
    title "MatheusKindrazki/clauderc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `290e6aa6735c` · [字段定义](../../DATASET.md)*
