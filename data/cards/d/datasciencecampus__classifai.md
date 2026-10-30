# datasciencecampus/classifai

⭐ 22 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/datasciencecampus/classifai) · [官网](https://datasciencecampus.github.io/classifai/) · 组织维护

**官方统计文本分类 Python 包：用语义搜索与 RAG 标注文本**

英国国家统计局数据科学中心开源的 MIT 协议 Python 包，面向数据专业人员，用于将自由文本（如问卷回答）标注到 SIC、SOC、COICOP 等官方统计分类。机制是在已标注样例构成的知识库上做语义搜索（可选 RAG 增强）：内置 FastEmbed、HuggingFace、Google Cloud、Ollama 等向量化器，支持前后处理钩子，可通过 FastAPI 部署为 REST 服务。无需训练或微调，知识库目前仅支持 CSV 输入，云端向量化器按请求计费。已在 ONS 生产使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于标注知识库的语义搜索分类，无需训练或微调
- 内置 FastEmbed/HuggingFace/Google Cloud/Ollama 向量化器，可自定义
- 前后处理钩子库（拼写检查、结果去重等）可扩展
- 内置 FastAPI 支持，可部署为 REST API 服务

## 适用场景

- 把问卷自由文本回答标注到标准统计分类（SIC/SOC/COICOP）
- 为统计处理流水线提供定时分类组件
- 为 Web 应用提供自由文本编码的后端 REST 接口

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L7: ClassifAI is a free, open-source (MIT Licence) Python package that simplifies semantic search and Retrieval Augmente
> L25: ClassifAI facilitates text classification using semantic search over a knowledgebase (possibly augmented by RAG).

## 星数曲线

```mermaid
xychart-beta
    title "datasciencecampus/classifai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-30 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `037a942d5b0e` · [字段定义](../../DATASET.md)*
