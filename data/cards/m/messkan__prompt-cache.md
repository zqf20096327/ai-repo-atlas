# messkan/prompt-cache

⭐ 426 · Go · MIT · 推送 2026-08-18 · [GitHub](https://github.com/messkan/prompt-cache) · [官网](https://messkan.github.io/prompt-cache) · 个人维护

**自托管 LLM 语义缓存代理：相似提示词直接返回缓存回答**

用 Go 编写的轻量自托管语义缓存，部署在应用与 LLM 提供商之间，检测相似提示词并返回缓存回答以减少上游调用与延迟。采用双阈值语义匹配（高相似直接命中、低相似未命中、中间灰区可用小模型做意图验证），兼容 OpenAI 客户端 SDK，支持 SSE 流式、运行时阈值调整、缓存预热、Bearer 认证与 Prometheus 指标。数据持久化于 BadgerDB（默认 TTL 24 小时）。README 明确语义匹配不构成授权机制，无租户隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双阈值语义匹配策略，灰区可选用小模型做意图验证
- OpenAI 兼容 chat-completions 端点与 SSE 流式支持
- OpenAI / Mistral / Anthropic(Claude) 三类嵌入与验证提供商
- BadgerDB 持久化、运行时阈值配置与缓存预热端点

## 适用场景

- RAG 应用中重复的内部问题减少上游模型调用
- 客服机器人收到相似问题时降低延迟与费用
- 为 LLM 流量加缓存层并监控命中率（Prometheus 指标）

## 场景标签

 · 领域:LLM 基础设施/中间件

## 证据(README 行号)

> L5: PromptCache is a lightweight, self-hosted semantic cache for GenAI workloads. It sits between your application and a
> L243: - OpenAI-compatible chat-completions endpoint

## 星数曲线

```mermaid
xychart-beta
    title "messkan/prompt-cache 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 425 --> 429
    line [428, 426, 426]
```

2026-10-18 428 → 2026-10-22 426（-2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8f4bc279c3f4` · [字段定义](../../DATASET.md)*
