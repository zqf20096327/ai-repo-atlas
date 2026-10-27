# patterns-ai-core/qdrant-ruby

⭐ 62 · Ruby · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/patterns-ai-core/qdrant-ruby) · [官网](https://rubydoc.info/gems/qdrant-ruby) · 组织维护

**Qdrant 向量数据库的 Ruby API 客户端封装**

以 Ruby gem 形式提供 Qdrant 向量数据库 HTTP API 的封装，支持通过 URL 与 API key 实例化客户端，操作集合（collections）、点（points）、快照（snapshots）、集群（clusters）与遥测（telemetry）。属于 Langchain.rb 技术栈的一部分，供 Ruby 开发者在应用中接入 Qdrant。开发流程包含 lint、单测与对真实 Qdrant 部署的端到端冒烟测试；采用 Apache License 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 Qdrant 的 collections/points/snapshots/clusters/telemetry API
- 通过环境变量传入 QDRANT_URL 与 API key 连接托管实例
- 提供对真实 Qdrant 部署的 e2e 冒烟测试 rake 任务

## 适用场景

- Ruby 应用中接入 Qdrant 向量数据库
- 配合 Langchain.rb 技术栈构建向量检索
- 在 Ruby 项目中管理 Qdrant 集合与向量点

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L7: Ruby wrapper for the Qdrant vector search database API.
> L9: Part of the Langchain.rb stack.

## 星数曲线

```mermaid
xychart-beta
    title "patterns-ai-core/qdrant-ruby 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-27 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `521f45f0c7a6` · [字段定义](../../DATASET.md)*
