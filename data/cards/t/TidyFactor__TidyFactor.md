# TidyFactor/TidyFactor

⭐ 15 · JavaScript · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/TidyFactor/TidyFactor) · [官网](https://tidyfactor.com/) · 个人维护

**面向 AI 辅助软件生产的技能/规则控制平面 CLI**

TidyFactor 是一个以 `tf` CLI 为核心的工具体系，用于在 Cursor、Claude Code、Windsurf、GitHub Copilot 等 18+ 编码 agent/IDE 间统一挂载、同步和管理架构规则与技能。它自称‘AI 辅助软件生产的操作系统’，包含 4 层记忆分类（Global/Tech/Project/Session）、50+ 条 Anti-Slop 规则、7 轴代码评审、`.tidyfactor/skills.lock` 状态锁定文件，以及覆盖 Next.js、PHP、HTMX 等的 14 个能力引擎。通过 npx、curl 脚本、PowerShell 与 Homebrew 安装，要求 Node.js >= 16，声明零外部依赖。附带双语（阿拉伯语/英语）交互式 TUI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一命令在 18+ IDE/agent 目录间挂载与同步技能
- 4 层知识记忆（Global/Tech/Project/Session）与上下文防火墙
- 50+ Anti-Slop 规则与 7 轴代码评审章
- Sovereign Lockfile（skills.lock）跟踪项目内技能状态

## 适用场景

- 在多个 AI 编码工具间统一架构规则与技能配置
- 为 AI 生成代码加确定性质量门禁，避免架构漂移
- 按技术栈（Next.js/PHP/HTMX 等）挂载对应的技能引擎

## 场景标签

`提示工程` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L41: > The **TidyFactor CLI (`tf`)** is not merely an npm installer for skills — it is the **Developer Control Plane** o
> L114: ### Layer 5: The Agent Interoperability Fabric (18+ IDEs)

## 星数曲线

```mermaid
xychart-beta
    title "TidyFactor/TidyFactor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0ea121971771` · [字段定义](../../DATASET.md)*
