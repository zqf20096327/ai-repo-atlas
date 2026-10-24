# NVIDIA-AI-Blueprints/rag

⭐ 798 · Python · Apache-2.0 · 推送 2026-09-03 · [GitHub](https://github.com/NVIDIA-AI-Blueprints/rag) · [官网](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline) · 组织维护

**企业级 RAG 参考方案：基于 NIM 微服务搭建检索增强问答管线**

NVIDIA 发布的 RAG 蓝图，作为构建检索增强生成管线的参考方案与起点：集成 NIM 推理/嵌入/重排/OCR 等微服务、NeMo Retriever 模型、可插拔向量库（默认 Elasticsearch，可选 Milvus）与护栏服务；含多模态文档摄取、混合检索、Agentic RAG（LangGraph plan-and-execute）、RAGAS 评测脚本与参考 UI。部署方式覆盖 Docker Compose、Kubernetes 与 OpenShift Helm，另以 Python 库模式与 OpenAI 兼容 API 提供。面向需要自有数据问答能力的企业开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agentic RAG：LangGraph plan-and-execute 管线，支持多跳与跨文档查询
- 多模态摄取（文本/表格/图表/信息图/音频）与混合检索+重排
- GPU 加速的 cuVS 向量库索引与搜索，向量库可插拔
- 附带 RAGAS 评测脚本与 agent skill（部署/评测/性能三类）

## 适用场景

- 基于自有企业数据搭建带引用的问答系统
- 对比与扩展参考 RAG 管线（本地 Docker 或 Kubernetes 部署）
- 运行 RAGAS 质量评测与检索性能基准测试

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L10: The NVIDIA RAG Blueprint is a reference solution and foundational starting point
> L11: for building Retrieval-Augmented Generation (RAG) pipelines with NVIDIA NIM microservices.
> L17: it serves as a flexible starting point that developers can adapt and extend to their specific needs.

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA-AI-Blueprints/rag 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 793 --> 799
    line [794, 796, 798]
```

2026-10-18 794 → 2026-10-24 798（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `324415e67e1d` · [字段定义](../../DATASET.md)*
