# mem7ai/mem7

⭐ 40 · Rust · Apache-2.0 · 推送 2026-03-26 · [GitHub](https://github.com/mem7ai/mem7) · [官网](https://mem7.ai/) · 个人维护

**面向 AI Agent 的 Rust 长期记忆引擎，含遗忘曲线与会话感知召回**

受 Mem0 启发并用 Rust 重实现的 Agent 长期记忆层，通过 PyO3/napi-rs 提供 Python、TypeScript、Rust 绑定。写入路径用 LLM 抽取事实声明、实体关系并去重，存入向量库与图数据库（内置 FlatIndex/FlatGraph，支持 Upstash、Neo4j、Kuzu）。特性包括艾宾浩斯遗忘曲线衰减（默认关闭）与按 memory_type/task_type 的会话感知评分（默认关闭）。LLM 与 Embedding 走单一 OpenAI 兼容客户端，FastEmbed 可本地 ONNX 推理。限制：不支持 Anthropic/Gemini/Bedrock 原生接入，向量库仅内置与 Upstash 可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 核心，Python/TypeScript/Rust 三语言绑定
- 艾宾浩斯遗忘曲线：陈旧记忆衰减、频繁回忆增强（默认关闭）
- 会话感知召回：memory_type×task_type 权重矩阵调节相关性
- 向量+图双路并发召回，LLM/Embedding 走 OpenAI 兼容客户端

## 适用场景

- 给 Agent/聊天机器人接入跨会话长期记忆
- 让频繁使用的记忆更稳固、过时信息自动降权
- 用本地 Ollama 与 FastEmbed 搭建无外部 API 依赖的记忆层

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5:  LLM-powered long-term memory engine — Rust core with multi-language bindings.
> L12: mem7 extracts factual statements from conversations, deduplicates them against existing memories, and stores the re
> L25: Python / TypeScript / Rust API

## 星数曲线

```mermaid
xychart-beta
    title "mem7ai/mem7 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-30 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f494c7c1e907` · [字段定义](../../DATASET.md)*
