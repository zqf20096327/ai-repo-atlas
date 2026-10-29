# arjunprabhulal/adk-advanced

⭐ 28 · Jupyter Notebook · 推送 2025-11-10 · [GitHub](https://github.com/arjunprabhulal/adk-advanced) · [官网](https://arjunprabhulal.com) · 个人维护

**Google ADK 高级用法的实现示例与部署模板合集**

收录多个自包含的 Google Agent Development Kit (ADK) agent 实现示例：内置/自定义函数工具、MCP 集成（GitHub、Firecrawl）、以及基于 Agent Starter Pack 的生产级部署模板，目标平台覆盖 Vertex AI Agent Engine、Cloud Run 与 GKE。面向希望在 Google Cloud 上构建、部署智能体的开发者；通过目录化示例与环境变量配置说明（Gemini API Key 本地开发 / Vertex AI 部署）组织内容，每个子目录含独立 README 与安装说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 类目录组织：工具、MCP、Agent Engine/Cloud Run/GKE 部署、Vertex AI Search 与 RAG Engine
- 基于 Agent Starter Pack 的生产级模板（Terraform IaC、CI/CD、可观测性）
- 本地开发用 Gemini API Key，部署走 Vertex AI ADC 认证的切换机制说明
- MCP 示例：GitHub 工具集接入与 Firecrawl 网页抓取客户端

## 适用场景

- 学习 Google ADK 的工具、MCP 与部署进阶用法
- 参考 Agent Engine/Cloud Run/GKE 三种部署方案落地自己的 agent
- 基于 ASP 模板快速生成带 CI/CD 与监控的生产级 agent 工程

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: > **A comprehensive collection of Google Agent Development Kit (Google ADK) implementations**
> L27: Each directory contains **self-contained Google ADK agent implementations**. Navigate to any subdirectory and follo

## 星数曲线

```mermaid
xychart-beta
    title "arjunprabhulal/adk-advanced 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `60585b54e336` · [字段定义](../../DATASET.md)*
