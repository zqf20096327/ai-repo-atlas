# TU-Wien-dataLAB/aqueduct

⭐ 30 · Python · BSD-3-Clause · 推送 2026-10-23 · [GitHub](https://github.com/TU-Wien-dataLAB/aqueduct) · [官网](https://tu-wien-datalab.github.io/aqueduct/) · 组织维护

**基于 LiteLLM Router SDK 与 Django 的自托管 AI 网关**

面向需要自托管 LLM 网关的开发者与组织，构建在 LiteLLM Router SDK 之上，用 Django 实现管理端。提供 OpenAI 兼容 API（补全、流式、嵌入、Batch、文件、语音合成与转录、图像生成）、Django API token 与 OIDC 认证、分级模型访问控制（组织/团队/用户）、多级限流与用量跟踪、Apache Tika 文本抽取，以及 MCP server 管理与 HTTP 代理。本地运行通过 Docker Compose 启动 Django、PostgreSQL、Celery/Redis、Tika 与 Dex；项目自述处于 WIP 阶段，尚无面向公众的稳定发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI 兼容 API：补全/嵌入/Batch/文件/语音/图像生成
- 分级模型访问控制与多级限流（请求/输入/输出 token 每分钟）
- MCP server 管理、HTTP 代理端点与会话式 MCP 协议支持
- Docker Compose 一键启动 Django+PostgreSQL+Celery/Redis+Tika+Dex

## 适用场景

- 自托管统一的 LLM API 网关并对接 OpenAI SDK 客户端
- 为组织/团队/用户分级管控模型访问与限流
- 跟踪 LLM 请求用量并做文件文本抽取接入

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13: **Aqueduct AI Gateway** aims to provide a **simple yet fully-featured** AI gateway you can self-host with **MCP ser
> L23: - Building on top of the **LiteLLM Router SDK** to provide enhanced control and routing capabilities, while avoidin

## 星数曲线

```mermaid
xychart-beta
    title "TU-Wien-dataLAB/aqueduct 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-27 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `9944e7a7ed40` · [字段定义](../../DATASET.md)*
