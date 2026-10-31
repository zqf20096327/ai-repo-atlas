# microsoft/copilot-agent-inventory-samples

⭐ 29 · MIT · 推送 2026-10-27 · [GitHub](https://github.com/microsoft/copilot-agent-inventory-samples) · 组织维护

**Microsoft Graph API 示例集：清点租户内 Copilot agent**

微软提供的示例解决方案集合，演示如何通过 Microsoft Graph Package Management（Inventory）API 以编程方式访问租户中已部署的 Copilot agent 目录，覆盖 Agent Builder、Copilot Studio、Pro Dev Tools 及 1P/3P 来源的 agent。能力包括列出全部 agent、读取元数据、识别重复/孤立/低使用 agent，以及支撑证明与生命周期治理流程。含 5 个面向不同平台的示例（声明式 agent、Power Platform 连接器、Power Automate 流、PowerShell 脚本），均为参考实现而非生产就绪方案；访问 API 需 Microsoft Agent 365 许可证。

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

- 基于 Graph Package Management API（/v1.0/copilot/admin/catalog/packages）获取租户 agent 目录
- 识别重复、孤立或低使用 agent 并支撑治理工作流
- 5 个平台各异的示例：声明式 agent、Power Platform 连接器、Power Automate 流、PowerShell 同步脚本
- README 声明部分示例由 AI 辅助快速构建，需在生产部署前自行审查测试

## 适用场景

- IT 管理员盘点租户内全部 Copilot agent 及其元数据
- 将 agent 清单同步到 SharePoint 便于筛选查看
- 识别重复或孤立 agent 以推进整合与治理

## 场景标签

 · 领域:企业 IT 治理/Microsoft 365

## 证据(README 行号)

> L3: A collection of sample solutions that demonstrate what is possible with the **Microsoft Graph Package Management (In
> L13: All samples in this repository are built on the Microsoft Graph Package Management API (`/v1.0/copilot/admin/catalo

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/copilot-agent-inventory-samples 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-31 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4ad2cd20a2c3` · [字段定义](../../DATASET.md)*
