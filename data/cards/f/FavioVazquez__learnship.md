# FavioVazquez/learnship

⭐ 62 · Shell · MIT · 推送 2026-05-28 · [GitHub](https://github.com/FavioVazquez/learnship) · [官网](https://faviovazquez.github.io/learnship/) · 个人维护

**给 AI 编程 agent 用户的上下文工程与规范驱动开发脚手架**

learnship 是一个安装在 AI 编程 agent（Claude Code、Cursor、Windsurf、OpenCode、Gemini CLI、Codex CLI）之上的工作流脚手架，npm 发布，npx 一键安装到 6 个平台。它提供 57 个工作流、5 个核心命令（/ls、/next、/new-project、/quick、/help）和 7 步阶段循环（讨论→计划→执行→验证→评审→交付→沉淀），通过 AGENTS.md 持久记忆、渐进式上下文注入与并行子 agent 执行，解决 agent 跨会话遗忘与质量漂移问题；另含学习检查点与 21 条设计系统命令。

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

- 6 平台安装，57 个工作流、5 个核心命令、7 步阶段循环
- AGENTS.md 持久记忆与渐进式上下文注入（progressive disclosure）
- 并行子 agent 执行（每波最多 5 个并发，各 200k 上下文）
- STRIDE + OWASP Top 10 安全验证与两遍评审（spec 合规 + 质量）

## 适用场景

- 让 AI 编程 agent 在长周期项目中跨会话保持决策与上下文对齐
- 以规范驱动的阶段流程把功能从讨论推进到 PR 交付
- 边构建边学习，理解每个阶段实际交付了什么

## 场景标签

`编码 Agent` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L15:  A context engineering and spec-driven development system for Claude Code, Windsurf, Cursor, OpenCode, Gemini CLI, 
> L155: learnship is an **agent harness** — the scaffolding that makes your AI coding agent actually reliable across real 
> L157: Every serious AI coding tool converges on the same architecture: a simple execution loop wraps the model, and the 

## 星数曲线

```mermaid
xychart-beta
    title "FavioVazquez/learnship 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 60 --> 63
    line [61, 62, 62]
```

2026-10-18 61 → 2026-10-30 62（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `810e33fd9480` · [字段定义](../../DATASET.md)*
