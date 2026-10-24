# dilolabs/nosia

⭐ 214 · Ruby · MIT · 推送 2026-10-23 · [GitHub](https://github.com/dilolabs/nosia) · [官网](https://hub.docker.com/r/dilolabs/nosia) · 组织维护

**自托管的 AI RAG + MCP 平台：用私有数据运行 AI 并对外提供 API**

基于 Ruby on Rails 的自托管 AI 平台：在自己基础设施上运行语言模型与嵌入模型，支持上传 PDF/文本/网站/Q&A 对构建知识库，可选启用 RAG（pgvector 向量检索）增强回答。集成 Model Context Protocol（MCP）连接外部工具与数据源，并提供 OpenAI 兼容 API 供现有客户端调用。安装通过脚本一键部署 Docker Compose，默认使用 Docker Hub AI 上的 Granite 系列模型，可经环境变量切换 Mistral、Llama、Qwen 等模型。支持多租户与流式输出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 API，可作为 OpenAI 客户端的替换端点
- RAG 增强回答，pgvector 向量相似检索，多格式文档导入
- MCP 集成：通过目录或自定义服务器（stdio/SSE/HTTP）扩展 AI 工具调用
- 一键安装脚本 + Docker Compose 部署，模型可经环境变量切换

## 适用场景

- 在自己服务器上搭建私有 RAG 知识库问答系统
- 为现有 OpenAI 客户端应用提供自托管 API 端点
- 通过 MCP 服务器让 AI 调用日历、文件存储等外部工具

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: **Self-hosted AI RAG + MCP Platform**
> L5: Nosia is a platform that allows you to run AI models on your own data with complete privacy and control. Beyond trad
> L10: - **🤖 OpenAI-Compatible API** - Drop-in replacement for OpenAI clients

## 星数曲线

```mermaid
xychart-beta
    title "dilolabs/nosia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 213 --> 215
    line [214, 214]
```

2026-10-18 214 → 2026-10-24 214（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `25f30f707123` · [字段定义](../../DATASET.md)*
