# win4r/GraphRAG4OpenWebUI

⭐ 604 · Python · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/win4r/GraphRAG4OpenWebUI) · [官网](https://www.bilibili.com/video/BV1gPkCYEENe/) · 个人维护 · 中文 README

**将 Microsoft GraphRAG 接入 Open WebUI 的检索 API 服务**

为 Open WebUI 提供 OpenAI 兼容格式的检索 API 服务，封装 Microsoft GraphRAG 的本地检索与全局检索，并可选接入 Tavily 网页搜索，另有组合三种来源的全模式检索。通过环境变量配置 API key、输入目录（Parquet 文件）与模型端点，支持通过 Ollama、LM Studio 使用本地 LLM 与本地 embedding 模型，可在不依赖外部 API 的情况下运行。以 Python 服务形式提供，监听 8012 端口，需先完成 GraphRAG 索引生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供四种检索模式：本地、全局、Tavily 网页搜索与全模型组合检索
- 支持 Ollama 与 LM Studio 运行本地 LLM，支持 SentenceTransformers 本地 embedding
- 暴露 /v1/chat/completions 与 /v1/models 接口，可在 Open WebUI 中直接配置接入
- 通过 API_BASE 等环境变量配置模型端点与数据目录

## 适用场景

- 在 Open WebUI 中接入基于知识图谱的 GraphRAG 问答
- 用本地 LLM 与本地 embedding 构建不依赖外部 API 的检索服务
- 组合本地知识库与网页搜索回答复杂问题

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L10: GraphRAG4OpenWebUI is an API interface specifically designed for Open WebUI, aiming to integrate Microsoft Research
> L14: The main goal of this project is to provide a convenient interface for Open WebUI to leverage the powerful features
> L101: 3. Integration with Open WebUI:

## 星数曲线

```mermaid
xychart-beta
    title "win4r/GraphRAG4OpenWebUI 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-28"]
    y-axis "stars" 603 --> 605
    line [604, 604]
```

2026-11-08 604 → 2026-11-28 604（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `48144a34e573` · [字段定义](../../DATASET.md)*
