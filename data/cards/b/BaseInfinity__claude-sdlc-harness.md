# BaseInfinity/claude-sdlc-harness

⭐ 52 · Shell · 推送 2026-10-04 · [GitHub](https://github.com/BaseInfinity/claude-sdlc-harness) · [官网](https://www.npmjs.com/package/agentic-sdlc-wizard) · 个人维护

**给 Claude Code 用户的 SDLC 强制执行系统：让 AI 编码前先规划、先测试**

面向 Claude Code（Anthropic 的 CLI）的自进化软件开发生命周期（SDLC）强制执行系统：通过 hooks 与 skills 让 AI 代理在编码前规划、上线前测试、不确定时升级到其他模型；自动扫描项目并生成定制的 CLAUDE.md/SDLC.md/TESTING.md/ARCHITECTURE.md。机制包括 pre-tool TDD 钩子、CI 中每个 PR 的 0-10 分 SDLC 合规评分、95% 置信区间的 A/B 基线对比、CUSUM 漂移检测、以及用 OpenAI Codex 做跨模型评审。提供 npx/npm/brew/curl/gh/plugin 六种安装途径，分 Reliable（默认）与 Frontier（实验性）两条 lane。已知缺陷：全新项目上 setup 不会自动触发（#698），需手动运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- pre-tool TDD 钩子 + CI 自动 SDLC 合规评分（0-10 分）
- 跨模型评审：用 OpenAI Codex CLI 复核 Claude 的工作
- A/B 基线对比（95% 置信区间）与 CUSUM 漂移检测
- 五种 AI 编码 lane 配置（Reliable/Frontier/Simple/Saver/Lite）

## 适用场景

- 让 Claude Code 在写代码前自动遵循规划与 TDD 流程
- 高风险变更引入独立模型做跨公司评审
- 在 CI 中检测 SDLC 配置漂移并量化 AI 开发纪律

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: A **self-evolving Software Development Life Cycle (SDLC) enforcement system for AI coding agents**. Makes Claude pla
> L30: **Requires Claude Code** (Anthropic's CLI for Claude). Install it with the native installer — `curl -fsSL https://c

## 星数曲线

```mermaid
xychart-beta
    title "BaseInfinity/claude-sdlc-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 50 --> 53
    line [51, 52]
```

2026-10-18 51 → 2026-10-30 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b36257bdfcf5` · [字段定义](../../DATASET.md)*
