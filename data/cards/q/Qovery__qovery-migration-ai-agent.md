# Qovery/qovery-migration-ai-agent

⭐ 25 · Go · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Qovery/qovery-migration-ai-agent) · [官网](https://migrate.qovery.com) · 组织维护

**用 AI 自动生成配置、把 Heroku 等应用迁移到 Qovery 的工具**

Qovery 维护的应用迁移代理：通过 Heroku 等 API 读取待迁移应用信息，过滤敏感数据后调用 AWS Bedrock 上的 Claude 模型，生成 Terraform 配置与 Dockerfile 等部署所需文件，将 Heroku/Render 应用迁移到 AWS、GCP、Azure 或 Scaleway（经 Qovery）。提供 CLI（本地运行）与 Web 界面（服务器部署）两部分，需配置 AWS Bedrock 凭证等环境变量。README 声明项目仍在开发中，可能未覆盖全部功能；不存储用户凭证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从 Heroku/Render API 读取应用信息并自动生成 Terraform 配置与 Dockerfile
- 调用 AWS Bedrock 上的 Claude 模型生成迁移配置
- 提供 CLI 与 Web 界面两种使用方式
- 迁移前过滤敏感数据，不存储用户凭证

## 适用场景

- 我想把 Heroku 应用迁移到 AWS/GCP/Azure/Scaleway 上的 Qovery
- 自动生成部署所需的 Terraform 与 Dockerfile，减少手工迁移工作

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: Qovery Migration AI Agent is an app designed to facilitate the migration of applications from various platforms to Q
> L42: The migration agent uses the Heroku (or other provider) API to fetch information about the application to be migrat

## 星数曲线

```mermaid
xychart-beta
    title "Qovery/qovery-migration-ai-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `0506e1dd6d2f` · [字段定义](../../DATASET.md)*
