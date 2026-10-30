# nearai/cloud-api

⭐ 15 · Rust · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/nearai/cloud-api) · [官网](https://cloud.near.ai) · 组织维护

**Rust 实现的 AI 推理云 API：模型推理、会话与组织管理**

NEAR AI 平台组件，用 Rust 编写的云 API 服务，提供 AI 模型推理接口、对话管理（Chat API 相关）与组织/工作区/API key 管理功能，描述称支持 OpenAI 兼容接口与 TEE 可验证推理，驱动 cloud.near.ai。本地开发通过 Docker Compose 启动 PostgreSQL 与 API 服务，或用 make dev 直接运行；配置采用 YAML 文件；测试需 PostgreSQL 与 cargo-nextest，含 vLLM 集成测试。采用 PolyForm Strict License 1.0.0（非 OSI 开源许可）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 实现的 AI 推理与组织管理 API 服务
- Docker Compose 一键启动 PostgreSQL 与 API 服务
- vLLM 集成测试与 cargo-audit 安全审计
- 运行时提供 Scalar 交互式 API 文档与 OpenAPI 规范

## 适用场景

- 自托管 NEAR AI 云推理 API 服务
- 作为 NEAR AI 平台的一部分做推理与会话管理
- 基于 OpenAI 兼容接口接入推理服务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: A Rust-based cloud API for AI model inference, conversation management, and organization administration. Part of the
> L101: ### vLLM Integration Tests

## 星数曲线

```mermaid
xychart-beta
    title "nearai/cloud-api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `264eac9452b2` · [字段定义](../../DATASET.md)*
