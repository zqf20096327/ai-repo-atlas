# davidmigloz/langchain_dart

⭐ 689 · Dart · MIT · 推送 2026-10-19 · [GitHub](https://github.com/davidmigloz/langchain_dart) · [官网](http://davidmigloz.github.io/langchain_dart/) · 个人维护

**LangChain 的 Dart/Flutter 移植版：构建 LLM 应用框架**

LangChain.dart 是 LangChain Python 框架的非官方 Dart 移植版，为 Dart/Flutter 开发者提供构建 LLM 应用的组件库：统一的模型 I/O 接口（对接 OpenAI、Google、Mistral、Ollama、Anthropic 等提供商）、检索模块（文档加载、切分、嵌入、向量存储）与 Agent 模块，组件通过 LCEL 组合。采用模块化多包设计（langchain_core/langchain/langchain_community 及各集成专属包），另维护可独立使用的各家 API 客户端包，通过 pubspec.yaml 添加依赖安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 对接多家 LLM 提供商并支持流式/多模态/工具调用
- 检索模块覆盖文档加载、切分、嵌入与多种向量存储（Chroma/Pinecone/Supabase 等）
- 模块化包设计，可只引入所需集成（langchain_openai 等）
- LCEL 表达式语言组合各组件

## 适用场景

- 在 Flutter/Dart 应用中接入 LLM 构建聊天机器人或问答功能
- 用 RAG 流水线基于自有数据生成有据回答
- 构建可调用工具（搜索、计算器）的 Agent

## 场景标签

`Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L13: LangChain.dart is an unofficial Dart port of the popular LangChain Python framework created by Harrison Chase.
> L15: LangChain provides a set of ready-to-use components for working with language models and a standard interface for c
> L39: LangChain.dart has a modular design that allows developers to import only the components they need. The ecosystem c

## 星数曲线

```mermaid
xychart-beta
    title "davidmigloz/langchain_dart 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 688 --> 691
    line [690, 689, 689]
```

2026-10-18 690 → 2026-10-26 689（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `cec7f7b54aa2` · [字段定义](../../DATASET.md)*
