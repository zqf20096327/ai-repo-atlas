# openaudr/audr

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/openaudr/audr) · [官网](https://openaudr.dev/) · 组织维护

**记录与核算 Agent 运行成本的开放 JSON 标准（AUDR）**

定义一种开放 JSON 记录标准：每个计量操作一条 AUDR 记录，携带发起者身份与归因信息（run_id/span_id/record_id），使 harness、router、provider 各层发出的记录可去重、可按运行连接，解决跨系统场景下客户 Agent 成本无法归集的问题。定价在下游完成，不属于标准范畴。仓库含规范（SPEC.md、JSON Schema、conformance fixtures）、Python/TypeScript 核心 SDK、Litellm/OpenRouter/Vercel AI 等适配器与 Chargebee/Lago 计费 sink。由 Chargebee 起草并管理，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个计量操作一条 JSON 记录，跨系统按 (run_id, span_id) 连接去重
- 提供 JSON Schema（Draft 2020-12）与语言无关的一致性测试夹具
- Python/TypeScript SDK 与 Litellm、OpenRouter、Vercel AI、Mastra 等适配器
- sink 对接 Chargebee、Lago 等计费目的地

## 适用场景

- 跨 harness/router/provider 的 Agent 运行成本归集与客户归因
- Agent 服务按用量计费时向计费系统交付用量记录
- 实现并验证符合 AUDR 规范的记录生产方或消费方

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L20: AUDR is one JSON record per metered operation, carrying enough identity and
> L57: |`adapters/`|Things that produce records — the Python and TypeScript SDKs and runtime adapters|
> L75: `Client`; a **sink** delivers each batch to a destination. Install the core and a sink, wrap

## 星数曲线

```mermaid
xychart-beta
    title "openaudr/audr 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b8cb72c456e4` · [字段定义](../../DATASET.md)*
