# ajac-zero/example-rag-app

⭐ 165 · TypeScript · MIT · 推送 2026-01-15 · [GitHub](https://github.com/ajac-zero/example-rag-app) · 个人维护

**Python RAG 参考应用：FastAPI/CLI 暴露检索问答管线**

提供通过 REST API 与交互式 CLI 使用的 RAG 管线 Python 程序，定位为遵循最佳实践的 AI 应用参考实现。不使用 LLM 框架，直接调用 OpenAI API，经 LiteLLM 代理支持 100+ 提供商；检索用 Qdrant 向量库（语义/关键词/混合），Redis 做语义缓存，Langfuse 提供本地可运行的 LLM 可观测性界面。内置读取 HuggingFace Wikipedia 数据集的摄入管线（分块、过滤、嵌入、索引）。运行需 UV 与 Docker，通过 just 命令管理脚手架、测试与 CI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- REST API 与 CLI 双入口的 RAG 管线，不依赖 LLM 框架、直接调用 OpenAI API
- LiteLLM 代理支持 100+ LLM 提供商
- 本地 Docker Compose 运行 Qdrant/Langfuse/Redis 等基础设施
- Marimo notebook 形式的摄入管线：HuggingFace Wikipedia → 分块 → 嵌入 → Qdrant 索引

## 适用场景

- 作为构建生产级 RAG 应用的参考实现学习
- 在本地快速跑通带可观测性的检索问答服务
- 替换摄入管线后接入自有数据源做问答

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L6: This repository contains a Python program that
> L7: exposes a RAG pipeline through a REST API or interactive CLI.
> L8: It is designed to serve as a reference implementation

## 星数曲线

```mermaid
xychart-beta
    title "ajac-zero/example-rag-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 164 --> 166
    line [165, 165]
```

2026-10-18 165 → 2026-10-28 165（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6ef92a9e5482` · [字段定义](../../DATASET.md)*
