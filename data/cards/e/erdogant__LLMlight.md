# erdogant/LLMlight

⭐ 14 · Jupyter Notebook · MIT · 推送 2026-10-18 · [GitHub](https://github.com/erdogant/LLMlight) · 个人维护

**本地运行 LLM 的轻量 Python 编排框架**

面向开发者的 Python 库，用于以最少依赖在本地运行大语言模型：支持 GGUF 模型与本地 API 端点，提供统一端点连接不同本地模型（如配合 LM Studio）。框架内建提示词精细控制（Query/Instructions/System/温度等参数）、多种嵌入方法（TF-IDF、BOW、BERT、BGE-Small）、Naive RAG 与 RSE 检索、全局推理与分块上下文策略，并支持 PDF 读取与本地记忆数据库存储。由个人维护者 Erdogan Taskesen 开发，通过 PyPI 安装。

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

- 支持 GGUF 模型与本地 API 端点的本地 LLM 运行
- 多嵌入方法（TF-IDF/BOW/BERT/BGE-Small）与 Naive RAG、RSE 检索
- 全局推理与分块两种上下文策略
- PDF 原生读取与本地记忆数据库

## 适用场景

- 在本地搭建带 RAG 检索的问答流程
- 通过统一端点管理和调用多个本地模型
- 对 PDF 文档做检索增强查询

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L16: LLMLight is a Python package for running Large Language Models (LLMs) locally with minimal dependencies. It provide
> L26: |**Local LLM Support**|Run LLMs locally with minimal dependencies.|

## 星数曲线

```mermaid
xychart-beta
    title "erdogant/LLMlight 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c4cdc52f84b0` · [字段定义](../../DATASET.md)*
