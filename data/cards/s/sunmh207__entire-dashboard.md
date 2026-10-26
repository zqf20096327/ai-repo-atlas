# sunmh207/entire-dashboard

⭐ 25 · Java · MIT · 推送 2026-06-06 · [GitHub](https://github.com/sunmh207/entire-dashboard) · 个人维护 · 中文 README

**可视化分析 entireio/cli 记录的 AI 辅助开发活动数据**

自托管的 Web 分析与可视化平台，读取 Entire CLI 在本地仓库记录的 AI 编码会话数据（提示与响应、Agent 转录、工具调用、token 用量等 Checkpoints 元数据），提供跨仓库的 AI 活动分析、AI 与人类贡献对比、会话与 Checkpoint 历史浏览、token 与工具调用监控等功能。支持 GitHub/GitLab/Gitee 托管的仓库，需先安装 Entire CLI 采集数据，可经 Docker Compose 一键启动前端、后端与数据库，默认账号 admin/admin。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 Entire CLI 记录的 AI 会话 Checkpoints（提示、转录、工具调用、token）
- AI 与人类贡献对比、跨多仓库聚合分析
- Docker Compose 一键启动，无需本地安装 Java/Node/MySQL
- 支持 GitHub/GitLab/Gitee 托管仓库

## 适用场景

- 工程团队审视 AI 编码工具的使用情况与贡献占比
- 组织对 AI 辅助开发流程做审计与优化
- 开发者回溯代码变更背后的会话与推理上下文

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L11: It provides a self-hosted dashboard that helps teams explore and analyze **AI-assisted development activity** recor
> L29: Entire Dashboard transforms this raw data into an **interactive analytics platform**. It ingests the data generated
> L40: This makes it easier for teams to **understand, audit, and optimize AI-assisted development workflows**.

## 星数曲线

```mermaid
xychart-beta
    title "sunmh207/entire-dashboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-26 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `03ccca89d784` · [字段定义](../../DATASET.md)*
