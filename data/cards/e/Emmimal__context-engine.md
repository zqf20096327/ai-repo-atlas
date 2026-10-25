# Emmimal/context-engine

⭐ 198 · Python · MIT · 推送 2026-05-18 · [GitHub](https://github.com/Emmimal/context-engine) · 个人维护

**纯 Python 的 LLM 上下文管理管道：检索、重排、记忆衰减与 token 预算**

面向 LLM 系统的上下文管理层库，将检索（关键词/TF-IDF/混合）、标签加权重排、带指数衰减与自动重要性评分的记忆、三种抽取式压缩，以及槽位式 token 预算控制组织为一条 build() 管道。核心仅依赖 Python 标准库与 numpy，sentence-transformers 为可选依赖，未安装时混合检索回退到随机嵌入。限制：token 估算按 1 token≈4 字符、记忆无跨会话持久化。附 7 个可运行 demo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五组件一体化管道：Retriever/Re-ranker/Memory/Compressor/TokenBudget
- 混合检索（embedding + TF-IDF）与查询感知的抽取式压缩
- 槽位式 token 预算：system → history → docs
- 核心仅依赖标准库 + numpy，CPU 可运行

## 适用场景

- 多轮对话中控制累积上下文的规模与顺序
- 大知识库下降低检索噪声并按 token 预算组装上下文
- 在延迟要求不严格的 CPU 环境做原型与实验

## 场景标签

`RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L2: A pure-Python context management layer for LLM systems — retrieval, re-ranking, memory decay, and token-budget enfor
> L21: Documents → Retriever → Re-ranker → Compressor → TokenBudget → ContextPacket → LLM

## 星数曲线

```mermaid
xychart-beta
    title "Emmimal/context-engine 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 196 --> 199
    line [197, 198, 198]
```

2026-10-18 197 → 2026-10-25 198（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `c0e5e0e26127` · [字段定义](../../DATASET.md)*
