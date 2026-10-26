# AbhisumatK/Epstein_Files_RAG

⭐ 51 · Python · MIT · 推送 2026-07-24 · [GitHub](https://github.com/AbhisumatK/Epstein_Files_RAG) · 个人维护

**检索解封 Epstein 案卷文档的 RAG 问答平台**

基于 LangChain、ChromaDB 和 Streamlit 构建的开源 RAG 应用：从 Hugging Face 下载 Apache Parquet 格式的解封 Jeffrey Epstein 法庭文档数据集，建立索引后在 Streamlit 界面中提问，可经系统提示词约束回答范围限定在调查文档内并拒绝无关请求。LLM 支持本地 Ollama 或 Groq/OpenRouter 云端推理。默认仅摄取 0.5GB 数据（完整数据集超 200GB），需在 .env 中配置 API key。

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

- 自动从 Hugging Face 下载并索引 parquet 数据集
- 支持 Ollama 本地或 Groq/OpenRouter 云端推理
- 系统提示词限定回答仅限调查文档范围
- 默认摄取 0.5GB 数据以降低内存与时间开销

## 适用场景

- 向解封的 Epstein 法庭文档提问并获取有据回答
- 在本地离线运行 RAG 检索流程分析案卷
- 作为开源 RAG 管线（LangChain+ChromaDB+Streamlit）的参考实现

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: An open-source Retrieval-Augmented Generation (RAG) platform to explore and analyze the unsealed Jeffrey Epstein cou
> L9: - **Local & Fast**: Support for local execution via Ollama or high-speed cloud inference via Groq/OpenRouter.

## 星数曲线

```mermaid
xychart-beta
    title "AbhisumatK/Epstein_Files_RAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-26 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3983cb4d8357` · [字段定义](../../DATASET.md)*
