# Caspian-Sun/claude-code-workflow

⭐ 10 · Shell · MIT · 推送 2026-08-31 · [GitHub](https://github.com/Caspian-Sun/claude-code-workflow) · [官网](https://github.com/Caspian-Sun/claude-code-workflow) · 个人维护 · 中文 README

**开发者用的 AI 驱动研发流程框架：8 步 SDLC 与硬门禁**

一个运行在 Claude Code 之上的研发工作流框架，将需求→拆解→实现→验证→评审→交付→发布拆为可追溯的命令、技能、子代理与规则。核心机制包括：8 步 SDLC 命令管线、硬门禁（prd-check/plan-check 阻断占位符与未完成任务）、PRD 锚点→任务 ID→@rules→验证用例的追溯链，以及 Commands/Skills/Subagents/Hooks/Rules 五部分协作结构。框架本体不绑定技术栈与领域，通过替换 workspace/ 与 .claude/rules/ 移植到其他领域；依赖 Claude Code CLI 已安装并登录，框架核心无需额外安装。

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

- 8 步 SDLC 命令管线（/prd→/plan→/code→/test→/review→/build→/deploy→/release）
- 硬门禁与 @rules 追溯链，AI 无法静默跳过检查点
- 五部分架构：Commands + Skills + Subagents + Hooks + Rules
- 跨领域可移植：替换 workspace/ 与 .claude/rules/ 内容即可适配新领域

## 适用场景

- 用 AI 执行从需求到发布的完整研发流程并保留人工审查点
- 为已有项目建立跨会话可追溯的 PRD-任务-验证链
- 将同一套流程框架移植到前端/后端/数据等不同领域

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5:  An AI-driven R&D workflow framework
> L8: AI executes, humans supervise every critical checkpoint · Runs on top of Claude Code
> L43: - **Eight-Step SDLC** — `/prd → /plan → /code → /test → /review → /build → /deploy → /release` as a single pipeline

## 星数曲线

```mermaid
xychart-beta
    title "Caspian-Sun/claude-code-workflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `ef097ba76c44` · [字段定义](../../DATASET.md)*
