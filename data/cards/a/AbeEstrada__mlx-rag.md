# AbeEstrada/mlx-rag

⭐ 20 · Python · MIT · 推送 2026-04-17 · [GitHub](https://github.com/AbeEstrada/mlx-rag) · 个人维护

**基于 MLX 的 RAG 示例代码，演示本地检索增强生成**

提供用 Python 编写的检索增强生成（RAG）示例：用 Langchain 做文档加载、Chroma 作向量数据库、Hugging Face sentence-transformers 生成嵌入、MLX 运行本地 LLM 完成生成。README 列出 7 个已在 mlx-community 量化模型上测试过的模型（gemma、Phi-3、Mistral、Mixtral 等 4bit 量化版本），并附一份示例文档。面向想在 MLX 环境中搭建 RAG 流程的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Langchain + Chroma + sentence-transformers + MLX 的完整 RAG 链路示例
- 列出 7 个已测试的 mlx-community 量化模型
- pip 安装依赖后单脚本运行

## 适用场景

- 在 Apple MLX 环境下学习/复现 RAG 流程
- 以量化模型在本地跑通检索问答示例

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: Retrieval Augmented Generation (RAG) example using Langchain (loader), Chroma (vector database), Hugging Face senten
> L5: This example code was tested with these models:

## 星数曲线

```mermaid
xychart-beta
    title "AbeEstrada/mlx-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f32125205cd5` · [字段定义](../../DATASET.md)*
