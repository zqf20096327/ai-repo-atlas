# toriihq/claude-review-action

⭐ 33 · Shell · MIT · 推送 2026-10-18 · [GitHub](https://github.com/toriihq/claude-review-action) · 组织维护

**给开发者的 GitHub Action：用 Claude 自动审查 PR 代码**

可复用的 GitHub Action，在 PR 上触发 Claude Code 进行代码审查：支持 label、PR 评论与行内评论 @claude 三种触发方式。通过 context-intro、critical-rules（注入为 BLOCKER 级规则）、review-guide 与仓库根目录 CLAUDE.md 提供项目上下文；审查权限分 comment-only/request-changes/full 三级，full 模式可在阈值条件下批准 PR。提供文件数/行数/diff 截断等 PR 规模限制、复审对账（FIXED/ACCEPTED/STILL OPEN）、成本追踪与可选 Check Run 输出。以纯 bash 实现，无构建步骤；需配置 ANTHROPIC_API_KEY 并安装 Claude GitHub App。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种触发方式：label、PR 评论与行内评论中的 @claude
- 三级审查权限：comment-only / request-changes / full（含阈值受控的 PR 批准）
- 复审对账：历史 HIGH/BLOCKER 发现标记为 FIXED/ACCEPTED/STILL OPEN
- diff 超限时的截断感知：保存缺失文件 diff 供 Claude 读取并核验其执行日志，未读完的批准会被撤回

## 适用场景

- 在 CI 流水线中自动审查 Pull Request 并按严重级拦截问题
- 通过 @claude 评论按需触发补充审查
- 在分支保护中以 Check Run 形式接入审查结论

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3:  Claude Code Review Action
> L5:  AI-powered code review using Claude. Drop this into any repo and get reviews in minutes.

## 星数曲线

```mermaid
xychart-beta
    title "toriihq/claude-review-action 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-29 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a7673d9a6fbe` · [字段定义](../../DATASET.md)*
