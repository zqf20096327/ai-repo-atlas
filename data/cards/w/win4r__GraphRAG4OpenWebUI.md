# win4r/GraphRAG4OpenWebUI

⭐ 604 · Python · Apache-2.0 · 推送 2026-11-07 · [GitHub](https://github.com/win4r/GraphRAG4OpenWebUI) · [官网](https://space.bilibili.com/3493277319825652) · 个人维护 · 中文 README

**为 Open WebUI 提供 GraphRAG 检索能力的 API 服务**

面向 Open WebUI 的 API 接口服务，将微软研究院的 GraphRAG（基于图的检索增强生成）技术以 OpenAI 兼容端点形式提供。整合四种检索模式：GraphRAG 本地搜索、全局搜索、Tavily 网络搜索及三者组合的全模型搜索。支持通过 Ollama、LM Studio 接入本地 LLM，以及 SentenceTransformers 本地嵌入模型，可不依赖外部 API 运行。以源码方式安装，python main-en.py 启动，默认监听 8012 端口。限制：graphrag 包可能需按微软研究院特定说明安装，需准备 Parquet 格式输入文件。

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

- 本地/全局/Tavily/全模型四种检索模式
- 支持 Ollama 与 LM Studio 本地 LLM 及本地嵌入模型
- OpenAI 兼容端点 /v1/chat/completions 供 Open WebUI 接入
- 环境变量配置 API key 与模型选择

## 适用场景

- 给 Open WebUI 增加 GraphRAG 检索后端
- 在本地知识库上做图结构检索问答
- 结合本地模型搭建不依赖外部 API 的检索系统

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L11: GraphRAG4OpenWebUI is an API interface specifically designed for Open WebUI, aiming to integrate Microsoft Research
> L15: The main goal of this project is to provide a convenient interface for Open WebUI to leverage the powerful features
> L103:  In the Open WebUI configuration, set the API endpoint to `http://localhost:8012/v1/chat/completions`. This will a

## 星数曲线

```mermaid
xychart-beta
    title "win4r/GraphRAG4OpenWebUI 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-18"]
    y-axis "stars" 603 --> 605
    line [604, 604]
```

2026-11-08 604 → 2026-11-18 604（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-17 · 置信度 high · 依据 README sha `1253566a492b` · [字段定义](../../DATASET.md)*
