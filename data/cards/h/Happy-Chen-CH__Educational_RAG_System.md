# Happy-Chen-CH/Educational_RAG_System

⭐ 34 · Python · 推送 2026-06-22 · [GitHub](https://github.com/Happy-Chen-CH/Educational_RAG_System) · 个人维护 · 中文 README

**教育场景的中文 RAG 智能问答系统，双引擎检索加流式生成**

面向教育问答场景的端到端 RAG 系统：BM25 关键词匹配命中已有问答对时直接返回，置信度不足则进入 Milvus 混合向量检索，配合微调 BERT 查询分类、LLM 自动选择直接检索/HyDE/子查询/回溯四种策略、BGE-Reranker 精排与父子块切分，经 DashScope（兼容 OpenAI API）流式生成答案。依赖 MySQL、Redis、Milvus 等基础服务，可仅运行 RAG 子系统以脱离 MySQL/Redis；首次运行需自动下载多个模型（约 5GB）并可能本地训练 BERT 分类器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两级检索：BM25 问答对匹配 + Milvus 稠密/稀疏混合检索
- 四种检索策略由 LLM Few-Shot 自动选择（直接/HyDE/子查询/回溯）
- BGE-M3 嵌入 + BGE-Reranker Cross-Encoder 精排
- 支持 PDF/DOCX/PPT/图片 OCR/Markdown 等多格式文档与多轮对话

## 适用场景

- 为教育机构搭建学科知识库问答服务
- 基于已有问答对快速响应高频咨询
- 按学科目录导入文档构建可检索知识库

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3:  一个面向教育场景的 RAG (检索增强生成) 智能问答系统，融合关键词匹配与语义检索双引擎，
> L4:  支持多种文档格式、自动查询分类、智能策略选择与流式 LLM 答案生成。
> L34: |🔍 **两级检索**|BM25 关键词匹配（快速）+ Milvus 混合向量检索（深度语义）|

## 星数曲线

```mermaid
xychart-beta
    title "Happy-Chen-CH/Educational_RAG_System 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-25 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `539342bed6c7` · [字段定义](../../DATASET.md)*
