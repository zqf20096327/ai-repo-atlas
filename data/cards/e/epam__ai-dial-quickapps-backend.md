# epam/ai-dial-quickapps-backend

⭐ 10 · Python · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/epam/ai-dial-quickapps-backend) · [官网](https://dialx.ai) · 组织维护

**面向开发者的 DIAL 应用组合器：用可复用工具编排 LLM 应用**

Quick Apps (2.0) 是构建 DIAL 应用的组合器：通过 JSON-schema 校验的清单文件，声明式地将 DIAL 原生工具、REST API 与 MCP 服务器同注册在 DIAL Core 中的任意 LLM 编排连接，发布后生成由 Core 管理的 DIAL 应用记录。支持回退、并行工具执行、循环与重试等流程控制。提供 make 脚本本地运行路径，另有 docker-compose 栈与对接既有 Core 的独立运行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 JSON-schema 校验清单声明式组合 DIAL 应用
- DIAL Core 中可用的任意 LLM 作为编排器（Azure OpenAI、Anthropic、Vertex AI 等）
- 支持回退、并行工具执行、循环与重试的流程控制
- 原生 DIAL 工具加外部 REST 与 MCP 集成

## 适用场景

- 把已有 REST API 与 MCP 服务器接入 DIAL 组合成 LLM 应用
- 在 DIAL Core 上编排带工具调用的多步骤应用流程
- 团队需要声明式清单管理 DIAL 应用发布

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: Quick Apps (2.0) is a composer for building DIAL applications from reusable tools and integrations. It lets you
> L18: - Compose applications by wiring tools and an LLM orchestrator via JSON-schema–validated manifests.

## 星数曲线

```mermaid
xychart-beta
    title "epam/ai-dial-quickapps-backend 星数(近 2 点)"
    x-axis ["2026-10-21", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-21 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `abab06f5af81` · [字段定义](../../DATASET.md)*
