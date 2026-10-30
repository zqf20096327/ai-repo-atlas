# altaidevorg/letsearch

⭐ 24 · Rust · Apache-2.0 · 推送 2026-04-01 · [GitHub](https://github.com/altaidevorg/letsearch) · [官网](https://altai.dev/open-source/letsearch/) · 组织维护

**单二进制向量数据库：导入 JSONL/Parquet 即完成嵌入、索引与检索**

以单一可执行文件形式提供的 RAG 原生向量数据库，面向不希望编写向量运算与基础设施代码的开发者：一条 CLI 命令即可从 JSONL、Parquet 或 HuggingFace Hub 数据集导入文档，自动下载 ONNX 嵌入模型、构建向量索引；再用同一二进制 serve 启动检索服务，配合 letsearch-client 发起搜索请求。支持从 HF Hub 列出与自带模型。项目自述处于早期阶段，API 可能快速变动；llama.cpp/GGUF、PDF 导入、MCP 支持在路线图中未实现。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单二进制覆盖导入→嵌入→索引→检索服务全流程
- 支持 JSONL/Parquet/HuggingFace 数据集导入与 glob 路径
- 内置 ONNX 推理，自动从 HF Hub 下载嵌入模型
- 支持转换并自带模型（letsearch-client）

## 适用场景

- 快速搭建 RAG 或语义搜索的向量索引后端
- 从 HuggingFace 数据集一键构建可检索集合
- 无代码方式为本地或 serverless 场景准备文档向量库

## 场景标签

`向量数据库` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L9: letsearch is a single executable binary to easily embed, index and search your documents without writing a single li
> L28: Building RAG (Retrieval-Augmented Generation) or semantic search applications often involves dealing with the compl
> L44: By combining these advantages with built-in support for ONNX models and plans for multimodal / multibackend capabil

## 星数曲线

```mermaid
xychart-beta
    title "altaidevorg/letsearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a2cf733ce586` · [字段定义](../../DATASET.md)*
