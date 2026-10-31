# Das-rebel/a3m-router

⭐ 17 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Das-rebel/a3m-router) · [官网](https://www.npmjs.com/package/adaptive-memory-multi-model-router) · 个人维护

**自托管多模型 LLM 路由网关：按请求复杂度路由到低价提供商**

以 OpenAI 兼容 API（端口 8787）形式运行的本地 LLM 路由服务：分析 prompt 复杂度，将请求路由到 80+ 提供商中最便宜可用的选项（如 Groq/Mistral/DeepSeek），复杂推理保留高端模型。提供两种路由模式：auto 启发式（约 0.4ms）与 jev-auto ML 决策头（约 2ms warm）。含失败回退（pheromone-trail failover）、语义缓存、提供商健康检查，以及并行集成执行与 MC Dropout 不确定性估计。以 npm 包提供，可用 Docker 或 Python 模块自托管。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 80+ 提供商分层（Free/Budget/Mid/Premium），运行时检查可用性
- auto 启发式与 jev-auto ML 决策头两种路由模式
- OpenAI 兼容 base_url 替换即可接入现有代码
- 并行集成引擎：置信度加权投票、Shapley 归因、来源响应头

## 适用场景

- 我在构建 AI 功能时想控制多提供商调用成本
- 某提供商宕机时自动回退到其他提供商
- 同一 prompt 对比不同提供商的质量

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L99: **Drop-in OpenAI replacement:**
> L102: client = OpenAI(base_url="http://localhost:8787/v1", api_key="not-needed")
> L113: ## Self-Hosted, No Lock-In

## 星数曲线

```mermaid
xychart-beta
    title "Das-rebel/a3m-router 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `86cda8a799a0` · [字段定义](../../DATASET.md)*
