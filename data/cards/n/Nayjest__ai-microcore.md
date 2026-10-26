# Nayjest/ai-microcore

⭐ 108 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/Nayjest/ai-microcore) · 个人维护

**面向 Python 开发者的极简 LLM 适配层，可切换模型与向量库**

Python 库，把 LLM API 与向量数据库/语义搜索封装为统一接口，使业务逻辑与具体服务实现解耦；通过配置即可在文本补全与对话补全模型之间切换。支持 OpenAI、Anthropic、MistralAI、Google、Azure 等 20 余个 API 服务，以及 HuggingFace Transformers 本地推理和命令行 LLM 工具（ollama/claude/gemini）。内置 LLM 无关的 MCP 工具集成（工具定义渲染进提示词、从模型输出解析调用）、Jinja2 提示词模板与 ChromaDB/Qdrant 向量检索函数。MIT 许可，个人维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一接口适配 20+ LLM API 服务，配置即可切换模型
- LLM 无关的 MCP 工具集成，支持无原生 MCP 的提供商
- ChromaDB/Qdrant 向量检索：search/get/save/delete 等函数
- 本地推理：HuggingFace Transformers 与命令行 LLM 工具（ApiType.CLI）

## 适用场景

- 构建需要随时切换 LLM 提供商的 AI 应用
- 为不支持 MCP 的模型接入 MCP 工具服务器
- 搭配 ChromaDB/Qdrant 做轻量语义检索应用

## 场景标签

`RAG` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L12: **MicroCore** is a collection of Python adapters for Large Language Models
> L17: It defines interfaces for features typically used in AI applications,
> L299: MicroCore supports major API providers via various chat completion / text completion APIs.

## 星数曲线

```mermaid
xychart-beta
    title "Nayjest/ai-microcore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-26 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `48eec1729588` · [字段定义](../../DATASET.md)*
