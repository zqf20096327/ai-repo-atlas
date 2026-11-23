# jing-ying-dev/whale-ying-memory

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/jing-ying-dev/whale-ying-memory) · 个人维护

**给 AI agent 提供结构化长期记忆的 Python 工具库**

将对话与长文档提取为四张结构化表（facts/cards/metrics/identities），通过 supersession 链与 folding 机制将过时事实标记失效并折叠到最新值，检索层组合多字段 BM25、all-MiniLM-L6-v2 向量与 RRF 融合，可选 Self-Ask 式迭代实现多跳问答。提取默认走 DeepSeek API，也可配置本地 Ollama 端点；回答模型走 OpenAI 兼容接口。仓库附带预构建的 262k 记忆存储与 CLI，支持 MemoryAgentBench 适配；LoCoMo 结果显示历史类问题为其明确任务边界。

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

- 四表结构化提取与确定性来源校验（引文必须是源文本子串）
- supersession 链与 folding 实现事实版本冲突消解
- BM25 + 向量 + RRF 混合检索，嵌入缓存一次构建
- 多跳问答经 Self-Ask 迭代逐步检索并组装证据链

## 适用场景

- 给需要长期记忆的 agent 存储与更新用户事实
- 处理多版本冲突事实的问答场景
- 在超长上下文文档上做多跳检索问答而不读全文
- 用本地模型部署私有环境下的记忆提取与检索

## 场景标签

`Agent 记忆` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L3: ### Structured long-term memory for AI agents
> L15: WhaleYing Memory turns conversations and long documents into a structured memory store. Instead of treating every r
> L46: |**Answer-model flexibility**|Uses an OpenAI-compatible answer endpoint; tested with DeepSeek, gpt-4o-mini, and a l

## 星数曲线

```mermaid
xychart-beta
    title "jing-ying-dev/whale-ying-memory 星数(近 2 点)"
    x-axis ["2026-11-22", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-22 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `d5d5baeab33a` · [字段定义](../../DATASET.md)*
