# wudao-tech/wudao-kms

⭐ 18 · Vue · AGPL-3.0 · 推送 2026-01-28 · [GitHub](https://github.com/wudao-tech/wudao-kms) · [官网](https://www.wudao-tech.com/knowledge) · 组织维护 · 中文 README

**面向企业的知识库管理与 RAG 智能问答系统（Spring Boot + Vue 3）**

基于 Spring Boot 3.x + Spring AI 与 Vue 3 + Element Plus 的企业级知识库管理系统：支持知识库分层管理与细粒度权限、多种格式文档解析（PDF/Word/Excel/Markdown，可经 MinerU 容器增强，需 GPU）、语义/全文/混合检索与 Rerank 重排，提供基于知识库的 RAG 对话（流式响应、引用溯源）与可配置 AI 助手。对话模型集成阿里通义、DeepSeek、智谱 AI、Moonshot、Ollama 等，通过策略接口可扩展新模型。提供 Docker Compose 部署与本地开发两种方式，后端需 JDK 21+、PostgreSQL 17+、Redis 7+。AGPL-3.0 协议，网络服务部署需开源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 知识库创建、树形知识空间与权限申请审批流程
- 语义/全文/混合三种检索模式配合 Rerank 重排
- RAG 对话流式响应（SSE）与引用溯源标记
- 多模型接入（通义/DeepSeek/智谱/Moonshot/Ollama）并通过 ChatModelStrategy 策略接口扩展

## 适用场景

- 企业内部知识管理与文档问答
- 构建基于自有知识库的智能客服
- 团队共享与权限管控的文档知识空间

## 场景标签

`知识库管理` `文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L16: 物道知识库管理系统（Wudao KMS）是一个开源的企业级知识库管理平台，集成了多种大语言模型，提供完整的知识库创建、文档解析、向量化检索、智能对话等功能。系统采用 RAG（检索增强生成）架构，支持多模态交互，适用于企业知识管理、
> L23: - 💬 **RAG 对话**：基于知识库的智能问答，流式响应，引用溯源
> L74: ### 4. AI 对话与助手

## 星数曲线

```mermaid
xychart-beta
    title "wudao-tech/wudao-kms 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `ab4b3e412f54` · [字段定义](../../DATASET.md)*
