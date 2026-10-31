# microsoft/GitHubCopilotLicenseAssignment

⭐ 29 · HTML · MIT · 推送 2026-10-28 · [GitHub](https://github.com/microsoft/GitHubCopilotLicenseAssignment) · [官网](https://github.com/DevExpGbb/GitHubCopilotLicenseAssignment) · 组织维护

**自助分配 GitHub Copilot 许可证的仓库模板（Issue+Actions 自动化）**

微软提供的仓库模板，含 Issue 模板与 GitHub Actions 工作流，用于在组织内自动化分配或移除 GitHub Copilot 许可证：用户通过 Issue 模板发起请求，打上 copilot-request/copilot-remove 标签触发工作流，经 GitHub App 与 octokit 调用 GitHub API 完成许可操作并在 Issue 上评论、关闭。适用于 Copilot for Business 与 Enterprise。可选配置 Environment 必需审批人实现审批流程。需自行创建标签、GitHub App、存储密钥。

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

- Issue 模板 + Actions 工作流自动分配/移除 Copilot 许可证
- 支持配置审批流程（Environment 必需审批人，最多 6 人）
- 工作流执行耗时少于 1 分钟，失败时保留 Issue 并评论通知
- 附 index.html 信息网页，可自行删除或定制

## 适用场景

- 组织内让成员自助申请 Copilot 许可证，替代手工管理
- 为许可证发放与回收增加审批环节
- 标准化许可证请求与移除流程并留存 Issue 记录

## 场景标签

 · 领域:开发者工具/IT管理

## 证据(README 行号)

> L3: This repository contains **Issue Templates** and a **GitHub Actions Workflow** that automates the management of GitH
> L9: The main goal of this solution is to automate the process of assigning or removing GitHub Copilot licenses. Instead 

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/GitHubCopilotLicenseAssignment 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-31 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `66a4b3b44b3a` · [字段定义](../../DATASET.md)*
