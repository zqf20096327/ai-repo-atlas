# Synlabs-ai/synrag

⭐ 7 · Python · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/Synlabs-ai/synrag) · [官网](https://ai.synlabs.pro) · 组织维护

**给 AI Agent 提供本地检索与引用上下文的 CPU 检索引擎**

单进程 RAG 引擎：解析 PDF/DOCX/XLSX 等文档格式，用自带 21M 参数的 Synapse 嵌入模型在 CPU 上做混合检索（BM25+向量+可选重排器），在 token 预算内生成带 [n] 引用的紧凑上下文。以 3 MB 二进制分发（源码未公开，仓库为 Apache 2.0 的 SDK/连接器/MCP 服务等周边），支持 MCP、REST API 与 Python SDK，按 Community/Production/Enterprise/OEM 分版本，社区版免费并允许商业使用，上限 1M chunks。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自带 Synapse 嵌入模型在纯 CPU 运行，无需 GPU 与外部嵌入 API
- 混合检索：BM25（多语言分析器）+ Synapse 向量 + 可选重排器
- token 预算内抽取回答句并附 [n] 引用（来源/章节/页码）
- MCP 服务对接 Claude Desktop/Cursor 等，另有 REST API 与免依赖 Python SDK

## 适用场景

- 让 AI Agent 通过 MCP 检索本地文档并生成带引用的上下文
- 企业内部文档构建本地知识库（数据不出机器）
- 为 OpenAI 兼容 LLM 搭配完整工具调用检索 Agent

## 场景标签

`RAG` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: **CPU-native search and context for AI agents.**
> L42: |🤖 **Agents first**|MCP server for Claude, Cursor and any MCP client; REST API; dependency-free Python SDK; OpenAI-
> L151: The engine ships as a binary in Releases; its source is not published.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `ee6a9b34ea0e` · [字段定义](../../DATASET.md)*
