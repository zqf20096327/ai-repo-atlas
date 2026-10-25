# imgompanda/fireauto

⭐ 140 · JavaScript · MIT · 推送 2026-04-09 · [GitHub](https://github.com/imgompanda/fireauto) · 个人维护

**Claude Code 插件：为 AI 编程提供项目管理与知识自动积累的 harness**

面向 Claude Code 用户的插件，通过 SessionStart/PostToolUse/Stop 等 Hook 与 MCP 工具实现：PRD 自动分解为里程碑与任务、开发知识自动积累到 Wiki（FTS4 全文检索）、用 Haiku 检测失误并自动追加 CLAUDE.md 规则、重复 3 次的模式自动生成技能、会话结束自动复盘。另提供多 AI 并行协作（git worktree 隔离）、SEO/安全/UIUX 审计、Reddit 需求调研等命令。通过 Claude Code 插件市场或 git clone 安装，/freainer 一键配置 MCP 与 LSP，无需 API key。

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

- Hook 驱动的自动化：失误检测、自动 lint、模式识别、会话复盘
- 知识自动积累为 Wiki + FTS4 全文检索，支持跨项目技能复用
- /team 多 AI 并行协作，git worktree 隔离避免代码冲突
- /freainer 一键安装推荐 MCP（Context7/Playwright/Draw.io）与 LSP

## 适用场景

- 让 Claude Code 自动管理项目计划与每日任务
- 自动积累开发经验并在后续会话中复用
- 对现有项目做 SEO 与安全审计
- 多个 AI 并行处理大规模开发任务

## 场景标签

`编码 Agent` `知识库管理` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L21: fireauto는 Claude Code를 위한 **AI 개발 하네스**예요.
> L38: |시점|자동 동작|기술|

## 星数曲线

```mermaid
xychart-beta
    title "imgompanda/fireauto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 139 --> 141
    line [140, 140]
```

2026-10-18 140 → 2026-10-25 140（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5a9a0f099fe2` · [字段定义](../../DATASET.md)*
