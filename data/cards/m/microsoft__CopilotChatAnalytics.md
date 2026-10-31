# microsoft/CopilotChatAnalytics

⭐ 21 · MIT · 推送 2026-10-20 · [GitHub](https://github.com/microsoft/CopilotChatAnalytics) · 组织维护

**Microsoft 提供的 Copilot Chat 与 Agent 使用分析 Power BI 模板**

由 Microsoft 维护的 Power BI 报告模板（.PBIT）：用户从 Microsoft Purview 导出 Copilot 交互审计日志、从 M365 管理中心导出许可用户列表、从 Entra 导出组织数据，将三个 CSV 接入模板后生成使用分析，覆盖提示词/会话/Agent/界面维度的使用可见性、用户参与度分层、Agent 采用趋势与按组织/分位/界面的细分视图。模板内置哈希去标识化处理敏感标识符。需 IT 管理员配合导出数据并具备相应 Graph 权限与 Purview 角色；README 明确声明不作为许可或官方报告的最终依据。

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

- Power BI 模板接入 Purview 审计日志、许可用户列表与 Entra 组织数据三个 CSV
- 提供用户参与度分层、Agent 采用与按组织/分位/界面的细分视图
- 内置哈希字符串对敏感标识符去标识化，便于共享
- 附带向 IT 管理员发送的数据导出前提邮件模板

## 适用场景

- 分析组织中 Copilot Chat 与 Agent 的使用趋势和采用热点
- 基于真实使用信号做 Copilot 许可决策参考
- 识别从轻度到习惯性使用的用户参与度分层

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: ### Purview-powered analytics for Copilot Chat and Agent usage.
> L40: - **Visibility into Copilot Chat usage** across prompts, sessions, agents, and surfaces.

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/CopilotChatAnalytics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6ac836495299` · [字段定义](../../DATASET.md)*
