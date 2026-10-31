# QwenLM/qwen-code-action

⭐ 43 · Shell · Apache-2.0 · 推送 2026-08-03 · [GitHub](https://github.com/QwenLM/qwen-code-action) · 组织维护 · 中文 README

**将 Qwen Code 集成进 GitHub 工作流的 GitHub Action**

由 QwenLM 团队维护的 GitHub Action，把 Qwen Code CLI 引入 GitHub 仓库工作流：既可作为自主 agent 处理例行编码任务，也可通过在 issue 或 PR 评论中 @qwencoder 按需委派工作（代码审查、issue 分诊、代码分析与修改、写测试等）。提供事件与定时触发的预置工作流、中央调度器，用 QWEN.md 注入项目上下文，凭 DashScope API key 认证，支持 npm 或 pnpm 安装 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 issue/PR 评论中以 @qwencoder 对话式触发任务（/review、/triage 等）
- 预置工作流：PR 审查、issue 分诊、通用助手、事件/定时调度
- QWEN.md 提供项目级指令与上下文定制
- 支持自定义 GitHub App 认证与扩展机制

## 适用场景

- 在 PR 上自动或手动触发 AI 代码审查
- 自动分诊和处理新开的 GitHub issue
- 在 issue 评论中委派 Qwen 写单元测试、调试或解释代码

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: `qwen-code-action` is a GitHub Action that integrates [Qwen Code] into your development workflow. It acts both as an
> L7: Use it to perform GitHub pull request reviews, triage issues, perform code analysis and modification, and more using

## 星数曲线

```mermaid
xychart-beta
    title "QwenLM/qwen-code-action 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-31 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ad78b7c1debd` · [字段定义](../../DATASET.md)*
