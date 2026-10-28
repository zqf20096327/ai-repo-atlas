# sligter/TurnsApi

⭐ 27 · Go · 推送 2026-04-25 · [GitHub](https://github.com/sligter/TurnsApi) · 个人维护 · 中文 README

**多提供商 LLM API 代理服务，含密钥轮询与监控**

TurnsAPI 是用 Go 编写的多提供商大模型 API 代理：支持 OpenAI、Google Gemini、Anthropic Claude、Azure OpenAI 等上游，对外提供 OpenAI Chat Completions 兼容接口。功能包括 Function Calling、SSE 流式响应、自动故障转移与重试、多种密钥轮询策略、模型别名映射、分组级参数覆盖。附带 Web 管理界面用于密钥状态监控与日志分析，推荐 Docker 部署（含 Postgres），也可本地 Go 1.24+ 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 OpenAI/Gemini/Claude/Azure OpenAI 多上游代理
- 密钥轮询、自动故障转移与重试策略
- 完整 Function Calling 与 SSE 流式响应支持
- Web 管理界面：密钥监控、请求日志与统计分析

## 适用场景

- 统一多个 LLM 提供商为一个兼容 API 入口
- 管理多把 API 密钥并做轮询与故障转移
- 通过 Web 界面监控 API 使用与密钥状态

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: TurnsAPI 是一个高性能多提供商 API 代理服务，支持 OpenAI、Google Gemini、Anthropic Claude、Azure OpenAI 等多个大模型提供商。
> L9: - **智能路由**: 自动故障转移和重试机制，支持多种轮询策略

## 星数曲线

```mermaid
xychart-beta
    title "sligter/TurnsApi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `81b42d98ebfa` · [字段定义](../../DATASET.md)*
