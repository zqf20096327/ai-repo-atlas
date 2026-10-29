# ljubobratovicrelja/tensor-truth

⭐ 28 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/ljubobratovicrelja/tensor-truth) · 个人维护

**本地优先的技术文档与论文 RAG 问答应用，主打检索质量**

单用户、本地优先的 RAG 应用，面向在自己硬件上运行小模型（8-24GB VRAM）的用户。核心是检索管线：层级分块加自动合并检索、BGE-reranker-v2-m3 交叉编码器重排，并针对 Sphinx/Doxygen API 文档、arXiv 论文、教科书目录分章做格式感知摄取。支持 Ollama、OpenAI 兼容 API（含 vLLM/OpenRouter 等）、llama.cpp 三类 LLM 提供方，具备 Agent 模式（rag_query、web_search、MCP 工具）、项目管理与 YAML 扩展。提供 pip 安装与 Docker 镜像，预构建索引托管于 HuggingFace Hub。无认证、不做多用户服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 层级分块 + 自动合并检索与交叉编码器重排（默认 BGE-reranker-v2-m3）
- Sphinx/Doxygen/arXiv/教科书的格式感知文档摄取
- 三类 LLM 提供方：Ollama、OpenAI 兼容 API、llama.cpp
- Agent 模式（最多 10 轮工具调用）与 YAML 斜杠命令/agent 扩展系统

## 适用场景

- 用自己的本地模型对技术文档和研究论文做问答
- 搭建围绕特定库或论文集合的项目知识库
- 让 agent 结合 RAG 与网络搜索回答技术问题

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L8: A local-first RAG application purpose-built for technical documentation and research papers. While many tools let yo
> L12: TensorTruth is designed as a single-user, local-first application — no authentication, no server deployment. This i
> L48: You need at least one LLM provider. The simplest option is Ollama:

## 星数曲线

```mermaid
xychart-beta
    title "ljubobratovicrelja/tensor-truth 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b7463f59a0ed` · [字段定义](../../DATASET.md)*
