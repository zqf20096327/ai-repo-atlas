# nexpeakcore/deepseek-harness-pr-review

⭐ 42 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/nexpeakcore/deepseek-harness-pr-review) · [官网](https://nexpeakcore.github.io/deepseek-harness-pr-review/) · 组织维护

**开发者用 DeepSeek/Claude 等 agent 自动审查 PR 的无头工具**

基于 DeepSeek Harness 的无头 PR 审查自动化工具：将 PR 描述拆分为逐条声明并用 file:line 证据对照实际代码核验，比对文档与代码现状（MATCH/STALE/WRONG/FABRICATED），分析业务需求影响（CHANGED/BROKEN/RISK），并审查代码缺陷（第二个 agent 确认 BLOCKER/MAJOR 后内联评论）。支持无描述 PR 的意图重建、自动轮询新 PR 与 Web 仪表盘。agent 后端可切换为 deepseek（默认）、Claude Code CLI、Codex CLI 或 Antigravity CLI。安装需 Python 3.10+ 与已认证的 gh CLI，Claude 后端对不可信 PR 工作区采取锁减工具与预算上限等沙箱措施。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PR 描述逐条声明核验，输出 file:line 证据
- 文档现实性检查 MATCH/STALE/WRONG/FABRICATED 与需求影响 CHANGED/BROKEN/RISK
- 四种 agent 后端（deepseek/claude/codex/agy）一个环境变量切换
- 自动审查轮询器按 diff 变化触发复审，附 Web 仪表盘

## 适用场景

- 团队自动审查每个新 PR 并拦截描述与代码不符的改动
- 核验仓库文档是否与代码脱节或虚构
- 在不确定时收到简短确认问题，人工介入审查流程

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: **AI code review with DeepSeek: headless PR review automation** that verifies
> L115: |`deepseek` (default)|DeepSeek Harness SDK, composed by `cordis/minimal.cordis.yml`|`DEEPSEEK_API_KEY`|

## 星数曲线

```mermaid
xychart-beta
    title "nexpeakcore/deepseek-harness-pr-review 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-27 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2ee654cffe57` · [字段定义](../../DATASET.md)*
