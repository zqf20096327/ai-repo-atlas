# nashtech-garage/ntg-agent

⭐ 98 · C# · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/nashtech-garage/ntg-agent) · 组织维护

**C# 多代理 RAG 聊天机器人示例工程（NashTech 出品）**

基于 .NET 10/Aspire 与 Microsoft Agent Framework 构建的聊天机器人实践项目：含 Orchestrator 后端、MCP Server、Blazor 聊天 UI 与管理端，共 5 个服务由 AppHost 编排。文档知识（上传/检索/RAG）由可插拔的 IKnowledgeService 提供，默认为每代理一个 LightRAG 容器，LLM 与 embedding 绑定支持 OpenAI/Ollama/Azure OpenAI/Bedrock/Gemini 等。可选接入 Azure AI Document Intelligence 实现文件上传问答。一条脚本完成本地安装（含 SQL Server 容器与 EF 迁移），Windows 需经 WSL2 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每代理独立 LightRAG 容器，知识后端可经配置插拔
- LLM/embedding 绑定支持 OpenAI、Ollama、Azure OpenAI、Bedrock、Gemini 等
- install.sh 一键完成本地依赖检查、LightRAG 栈启动与密钥配置
- 可选 Azure AI Document Intelligence 实现文档上传问答

## 适用场景

- 学习用 C#/.NET 技术栈构建多代理 RAG 聊天机器人
- 在本地快速跑通带聊天 UI 与管理端的 agent 系统
- 接入自选 LLM 提供商做知识库问答实验

## 场景标签

`Agent 框架` `聊天机器人` `RAG` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L2: This project aims to practice building a chatbot in C#
> L139: Document knowledge (upload, search, RAG) is served by a pluggable provider behind
> L151: - `LightRag` (default) — one LightRAG container per agent, implemented in the

## 星数曲线

```mermaid
xychart-beta
    title "nashtech-garage/ntg-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 97 --> 99
    line [98, 98]
```

2026-10-18 98 → 2026-10-27 98（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `bd9023097227` · [字段定义](../../DATASET.md)*
