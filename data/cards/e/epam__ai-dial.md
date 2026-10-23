# epam/ai-dial

⭐ 146 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/epam/ai-dial) · [官网](https://docs.dialx.ai/) · 组织维护

**EPAM 开源企业级 AI 平台 DIAL 的文档与示例仓库**

AI DIAL 是 EPAM 维护的开源企业级 AI 平台，核心组件 DIAL Core 以单一 OpenAI 兼容统一 API 接入各厂商的语言与嵌入模型及其上的应用与 agent，并集中管理访问控制、成本限制与可观测性；配套 DIAL Chat（终端用户 Web UI）、DIAL Admin（管理控制台）及面向 OpenAI/AWS Bedrock/Vertex AI 等的模型适配器。本仓库承载官方文档（Docusaurus 构建）、快速启动 Docker Compose 配置、Cookbook 笔记本与 SDK 子模块。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DIAL Core 暴露 OpenAI 兼容统一 API，接入任意厂商模型与应用
- 集中管理访问控制、成本限制与可观测性
- 提供模型适配器（OpenAI/Bedrock/Vertex AI 等）与 Python/TypeScript SDK
- 仓库含快速启动 Docker Compose、进阶生产级栈与 Cookbook 示例

## 适用场景

- 企业统一接入多家模型厂商并集中管控访问与成本
- 在本地用 Docker Compose 快速运行 DIAL Chat 试用平台
- 基于 DIAL SDK 构建 AI 应用、模型适配器与拦截器
- 将 DIAL 部署到 Kubernetes 并接入 n8n、Teams 等工具

## 场景标签

`LLM 可观测性` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L17: **DIAL** (Deterministic Integrator of Applications and Language Models) is an open-source, enterprise-grade AI plat
> L67: |DIAL Core|The central and only required component. An API gateway that exposes the Unified API to models, applicat
> L85: |DIAL Chat|The default web UI: chat with models and applications, and manage conversations, prompts, and files|

## 星数曲线

```mermaid
xychart-beta
    title "epam/ai-dial 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 145 --> 147
    line [146, 146]
```

2026-10-18 146 → 2026-10-23 146（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `262871107e73` · [字段定义](../../DATASET.md)*
