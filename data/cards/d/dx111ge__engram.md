# dx111ge/engram

⭐ 21 · JavaScript · NOASSERTION · 推送 2026-10-16 · [GitHub](https://github.com/dx111ge/engram) · 个人维护

**自托管 AI 知识引擎：单二进制集成知识图谱+语义搜索+推理**

用 Rust 编写的单二进制自托管知识引擎，数据存储于单个 .brain 文件，内置 mmap 存储、BM25+HNSW 混合搜索、前向/后向链推理、GLiNER2 ONNX NER 摄取管道与矛盾检测。提供 HTTP REST（230+ 端点）、MCP、gRPC、A2A 等 API，可作 AI 管线的后端记忆层，或通过内置 Web UI（3D 图谱、多 agent 辩论、47 工具聊天）作为情报工作台。LLM 需外部提供，任何 OpenAI 兼容端点可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制+单 .brain 文件，无外部数据库与云依赖
- BM25+HNSW 向量+位图过滤的混合搜索
- MCP/REST/gRPC/A2A 多 API 与 MCP 服务器模式
- 置信度生命周期：确认增强、随时间衰减、矛盾纠正

## 适用场景

- 作为 AI 应用的后端记忆/知识层接入（REST/MCP/gRPC）
- 摄取文档构建知识图谱并做多源事实核验
- 通过多 agent 辩论与贝叶斯评估做情报分析

## 场景标签

`知识图谱` `语义搜索` `向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L11: Engram is a self-hosted AI knowledge engine that combines graph storage, semantic search, logical reasoning, and co
> L31: **As a backend memory layer** -- integrate Engram into your AI pipeline via REST, MCP, or gRPC. Use the onboarding 

## 星数曲线

```mermaid
xychart-beta
    title "dx111ge/engram 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d1147ba09334` · [字段定义](../../DATASET.md)*
