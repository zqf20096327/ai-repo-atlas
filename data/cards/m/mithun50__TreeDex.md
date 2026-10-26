# mithun50/TreeDex

⭐ 42 · TypeScript · MIT · 推送 2026-04-07 · [GitHub](https://github.com/mithun50/TreeDex) · [官网](https://mithun50.github.io/TreeDex/) · 个人维护

**无向量的树结构文档 RAG 框架，支持任意 LLM 接入**

面向开发者的文档 RAG 框架，以 Python 与 Node.js 双语言提供且共享同一 JSON 索引格式。将 PDF/TXT/MD/HTML/DOCX 文档索引为层级树：有 PDF 书签时直接建树（无需 LLM），否则用 LLM 结合字号标题检测抽取层级，查询时由 LLM 选择相关树节点并返回上下文、页码范围与推理说明。预置 Gemini/OpenAI/Claude/Mistral/Ollama 等十余个后端，另有 OpenAI 兼容端点、LiteLLM 与自定义函数封装。无 Agentic 模式下仅返回检索上下文，不直接生成回答。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 树结构检索替代向量数据库与嵌入模型
- PDF ToC 直接建树路径无需 LLM 调用
- 预置 14 个一行式 LLM 后端及 OpenAI 兼容/LiteLLM/自定义后端
- Python 与 Node.js 索引格式互通，可在查询时切换 LLM

## 适用场景

- 在无向量数据库基础设施的条件下对长文档做 RAG 检索
- 需要精确页码溯源的文档问答系统
- 跨 Python/Node.js 技术栈共享同一文档索引

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: Index any document into a navigable tree structure, then retrieve relevant sections using **any LLM**. No vector dat
> L40: ## Supported LLM Providers

## 星数曲线

```mermaid
xychart-beta
    title "mithun50/TreeDex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-26 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7a25c5d185bd` · [字段定义](../../DATASET.md)*
