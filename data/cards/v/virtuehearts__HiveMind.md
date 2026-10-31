# virtuehearts/HiveMind

⭐ 148 · TypeScript · 推送 2026-03-13 · [GitHub](https://github.com/virtuehearts/HiveMind) · [官网](https://darknet.ca) · 个人维护

**本地优先的 Agentic RAG 架构：可热插拔的记忆胶囊 EMU**

本地优先、隐私保护的 Agentic RAG 协议：将知识封装为可 Git 分享、可热插拔的 EMU（Encapsulated Memory Unit）目录（内含 LanceDB 向量文件与元数据），替代单一大型向量库。三层架构：本地 SLM（Ollama 运行 Qwen2.5 1.5B/Phi-3.5）做意图分类、PII 脱敏与上下文压缩，LanceDB 做本地文件存储，云端 LLM（OpenRouter/Gemini/Claude/GPT）仅做最终推理。基于 LangGraph 构建，含 Node.js 后端与 Vite Web UI，面向消费级 CPU（8-16GB RAM）与 6GB 显存 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- EMU 记忆胶囊：便携、可版本控制、可热插拔挂载
- 本地 SLM 路由 + PII 脱敏 + 上下文压缩后再调云端 LLM
- LanceDB 文件式向量存储，无需独立向量数据库
- 面向 8-16GB RAM 消费级硬件，量化 SLM 达 40-50 tokens/sec

## 适用场景

- 在低配笔记本/旧电脑上本地运行隐私优先的 RAG 问答
- 以 Git/文件方式分享和复用模块化知识库
- 在本地过滤敏感信息后再调用云端 LLM 生成回答

## 场景标签

`RAG` `知识库管理` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L8: HiveMind is a **local-first, edge-augmented RAG protocol** that treats memory as **portable, hot-swappable artifacts
> L142: # 🧩 The HiveMind Pipeline (LangGraph Implementation)
> L188: |Workflow Engine|**LangGraph**|Agentic DAG pipeline|

## 星数曲线

```mermaid
xychart-beta
    title "virtuehearts/HiveMind 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 147 --> 149
    line [148, 148]
```

2026-10-18 148 → 2026-10-31 148（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `25e43697c41a` · [字段定义](../../DATASET.md)*
