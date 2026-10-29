# brucetruth/ml-idea

⭐ 19 · PHP · MIT · 推送 2026-07-08 · [GitHub](https://github.com/brucetruth/ml-idea) · 个人维护

**面向 PHP 开发者的机器学习库：分类/回归/NLP/RAG/Agent**

PHP 8.2+ 的机器学习库，提供分类器（KNN、逻辑回归、朴素贝叶斯、随机森林等）、回归、评估指标、预处理、交叉验证、模型持久化与 Pipeline 等经典 ML 能力；扩展模块覆盖 NLP（分词、NER、BM25、TF-IDF）、视觉取证特征、RAG（多种 embedder 与 LLM 客户端，含 Ollama/OpenAI/Azure）以及工具调用 Agent。面向想在 PHP 技术栈内完成 ML 与 AI 工程的开发者，以 Composer 包分发，附 PHPUnit 测试与 PHPStan 静态分析。神经能力多为后端钩子（Ollama/HuggingFace），核心为经典算法实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 经典 ML 全链路：分类/回归/聚类/降维/校准/超参搜索/模型持久化
- NLP 模块：unicode 分词、规则 POS/NER（104 语言）、BM25、TF-IDF、PII 脱敏
- RAG 栈：多种 embedder（Ollama/OpenAI/Azure/HF）+ LLM 客户端 + 向量存储
- 工具调用 Agent 与路由（OpenAI/Azure/Anthropic/Ollama）

## 适用场景

- 在纯 PHP 技术栈内训练和部署分类/回归模型
- PHP 项目中构建 NLP 特征或 BM25 检索
- 在 PHP 中搭建 RAG 问答与工具调用 Agent

## 场景标签

`RAG` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: `ml-idea` is a modern, production-oriented machine learning library for PHP focused on clean APIs,
> L16:  - `KNearestNeighbors`
> L28: - Regression support (`LinearRegression`, `RegressionMetrics`)

## 星数曲线

```mermaid
xychart-beta
    title "brucetruth/ml-idea 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3d05ee751be1` · [字段定义](../../DATASET.md)*
