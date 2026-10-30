# strands-agents/devtools

⭐ 18 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/strands-agents/devtools) · [官网](https://strandsagents.com) · 组织维护

**Strands Agents 组织共享的 CI/CD 工作流与工具仓库**

汇集 Strands Agents 组织各仓库共用的 GitHub Actions 与工作流：可复用的构建、测试、发布 CI/CD 流程，以及跨仓库共享的脚本工具。包含三个 Action：issue-labeler 用 LLM 对 issue 分类并按白名单打标签；authorization-check 校验工作流触发者的授权；strands-command 在 GitHub Actions 中运行 Strands agent。面向维护或贡献 Strands Agents 项目的开发者，采用 Apache-2.0 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可复用的构建/测试/发布 CI/CD 工作流
- issue-labeler：LLM 驱动的 issue 分类与白名单打标
- strands-command：在 GitHub Actions 中运行 Strands agent
- 跨仓库共享的脚本与工具集

## 适用场景

- 为 Strands Agents 各仓库复用统一 CI/CD 流程
- 自动分类和标注 GitHub issue
- 在 CI 中运行 Strands agent 执行任务

## 场景标签

 · 领域:开发者工具/CI-CD

## 证据(README 行号)

> L11: This repository contains common GitHub workflows, actions, and shared tooling used across the Strands Agents organi
> L17: - **GitHub Actions & Workflows**: Reusable CI/CD workflows for building, testing, and releasing Strands Agents proj
> L26: |`strands-command`|Run a Strands agent in GitHub Actions|

## 星数曲线

```mermaid
xychart-beta
    title "strands-agents/devtools 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `86e2029645c9` · [字段定义](../../DATASET.md)*
