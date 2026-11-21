# tigusigalpa/nebula-go

⭐ 13 · Go · MIT · 推送 2026-11-15 · [GitHub](https://github.com/tigusigalpa/nebula-go) · 个人维护

**为 Go 开发者提供的 Nebula 公共 API 客户端 SDK（41 个操作）**

该 SDK 是 Nebula Public API 的 Go 客户端，覆盖固定 OpenAPI 1.0.2 契约中的全部 41 个操作，服务按 Discovery/Lookup/Social/Forecasts/MarketSentiment/MarketData/Intelligence/Clusters/Predictions/Agent/Account 分组。请求用普通 Go 结构体、响应带具体字段类型，SDK 处理认证、查询编码、响应解码与重试，并支持请求级校验、本地化与可选 x402 按次付费适配器。核心包仅依赖 Go 标准库，需 Go 1.24+，使用需自备 API key。

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

- 覆盖 41 个 API 操作的强类型请求与响应
- Agent 服务支持 OpenAI 兼容的完整与流式（SSE）对话
- 请求前置校验、可配置重试/超时与本地化
- 核心包仅用 Go 标准库，含离线 OpenAPI 生成器

## 适用场景

- 在 Go 后端接入 Nebula 查询资产情绪与预测市场数据
- 构建监控任务跟踪社区情绪与趋势对话
- 让 Go 应用通过 Agent 服务流式生成数据解读文本

## 场景标签

`数据分析` `金融量化` · 领域:效率与自动化

## 证据(README 行号)

> L14: **Explore market conversations with Go.** `nebula-go` is a client for the Nebula Public API: find an asset, follow 
> L18: The client covers all **41 operations** in the pinned OpenAPI 1.0.2 contract. The core package uses the Go standard
> L30: ## Install


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `d8258ff3b2e2` · [字段定义](../../DATASET.md)*
