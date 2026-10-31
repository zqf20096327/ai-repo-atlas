# microsoft/BC-ALAgents

⭐ 13 · PowerShell · MIT · 推送 2026-10-29 · [GitHub](https://github.com/microsoft/BC-ALAgents) · 组织维护

**Business Central (AL) PR 的 Copilot CLI 自动审查引擎**

由微软维护的开源、可 fork 的 PR 审查引擎：通过工具增强的 GitHub Copilot CLI 对 Business Central (AL) 代码的 PR diff 执行审查，并将结构化发现以行内评论形式发布到 PR。引擎只提供机制，审查知识存放于 microsoft/BCQuality 仓库，消费方通过 bcquality.config.yaml 配置策略（仓库/ref/层级/技能/严重度阈值）。以可复用 GitHub Actions workflow 形式提供，含确定性叶子/根执行 schema 校验与失败即停（fail-closed）机制。

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

- 通过 Copilot CLI 对 AL PR diff 审查并发布行内评论
- 机制与知识分离：审查技能来自 BCQuality 仓库
- 叶子/根两级 findings-report schema 派生与 fail-closed 校验
- 可复用 workflow_call 工作流，消费方仅需薄调用层

## 适用场景

- Business Central 仓库接入自动 PR 代码审查
- 通过自有 BCQuality 策略控制审查范围与严重度阈值
- 在 CI 中以固定引擎版本标签保证审查可复现

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: An open-source, forkable engine that runs a tool-enabled GitHub Copilot CLI
> L21: |`agents/ALReviewAgent/scripts/Invoke-CopilotPRReview.ps1`|Orchestrator: checks out the PR head, builds the BCQuali

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/BC-ALAgents 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7d5ea0144334` · [字段定义](../../DATASET.md)*
