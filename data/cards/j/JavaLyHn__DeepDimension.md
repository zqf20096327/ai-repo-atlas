# JavaLyHn/DeepDimension

⭐ 11 · Java · GPL-3.0 · 推送 2026-07-15 · [GitHub](https://github.com/JavaLyHn/DeepDimension) · 个人维护 · 中文 README

**企业级 RAG 知识库系统：文档入库、混合检索与 AI 对话**

基于 Spring Boot 3.4 与 Vue 3 的前后端分离 RAG 知识库系统，覆盖文档上传、解析、向量化存储、检索到 AI 对话的完整流程。检索采用 KNN 向量召回 + BM25 Rescore + Cross-Encoder 重排三阶段混合方案，配合 Dynamic Top-K 动态筛选与基于 LLM 的 Query-Rewrite（指代消解、语义补全）。文档侧支持大文件分片上传、Kafka 异步解析与父子索引分块。权限通过 JWT 认证与组织标签三级控制实现。部署依赖 MySQL、Redis、Elasticsearch（IK 插件）、MinIO、Kafka 等多个组件，需逐一启动配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三阶段混合检索：KNN 召回 + BM25 Rescore + Cross-Encoder 重排
- 基于 LLM 的 Query-Rewrite 模块做指代消解与语义补全
- 父子索引策略：小粒度子块定位检索，回溯父级段落恢复上下文
- 组织标签三级权限控制（私人/组织/公开）与 JWT 自动刷新

## 适用场景

- 在企业内部搭建文档问答知识库
- 按组织层级控制知识库资料的访问权限
- 批量解析 PDF/Word/Excel 等文档并支持检索

## 场景标签

`RAG` `文档问答` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L15: DeepDimension 是一个面向企业场景的 **RAG（Retrieval-Augmented Generation）检索增强生成知识库系统**，采用前后端分离架构。系统实现了从文档上传、智能解析、向量化存储、混合检索到 A
> L122: |DeepSeek API|-|LLM 对话（流式SSE）|

## 星数曲线

```mermaid
xychart-beta
    title "JavaLyHn/DeepDimension 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-13", "2026-11-22"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-11-02 10 → 2026-11-22 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `be6f819d1888` · [字段定义](../../DATASET.md)*
