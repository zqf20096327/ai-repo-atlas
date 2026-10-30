# marc-ing/langchain-advanced-rag

⭐ 18 · Python · MIT · 推送 2026-08-26 · [GitHub](https://github.com/marc-ing/langchain-advanced-rag) · 个人维护 · 中文 README

**HR 政策问答 RAG 应用：LangChain 编排、FAISS 检索与拒答分支**

由 Notebook 教学案例整理的 HR 政策问答项目：上传 UTF-8 Markdown 员工手册，按 H1/H2 标题切分，经 OpenAI 兼容接口生成 Embedding 并用 FAISS 建本地向量索引；提问时先由 LLM 判断是否属于 HR 范围，通过 RunnableBranch 走“检索并回答”或“直接拒答”分支，携带最近 50 条消息支持多轮对话。提供 FastAPI REST API 与 Web UI。限制：仅解析结构化 Markdown，单路向量检索，无混合检索与重排序；分类护栏非严格安全边界。默认 Base URL 为 DashScope 兼容端点，也支持本地端口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- RunnableBranch 条件路由：HR 问题检索回答，非 HR 问题检索前拒答
- Markdown 按标题切分 + OpenAI 兼容 Embedding + FAISS 本地持久化索引
- 最近 50 条消息的多轮对话上下文与指代理解分类
- FastAPI REST API、Swagger 文档、响应式 Web UI 与单元测试

## 适用场景

- 上传员工手册搭建内部 HR 政策问答
- 演示 LCEL 条件分支与拒答护栏的 RAG 流程编排
- 对接 OpenAI 兼容云端或本地模型服务做问答

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L9: 一个基于 **LangChain LCEL、FAISS 和条件分支**实现的智能 HR 政策问答项目。应用读取 Markdown 员工手册，按标题生成语义片段并建立本地向量索引；收到问题后，先由 LLM 判断是否属于 HR 范围，再
> L45: - 使用 `RunnableBranch` 执行检索回答或拒答分支；
> L65: extract → classify → retrieve → generate

## 星数曲线

```mermaid
xychart-beta
    title "marc-ing/langchain-advanced-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4d2ec7876968` · [字段定义](../../DATASET.md)*
