# TilmanGriesel/chipper

⭐ 485 · Python · MIT · 推送 2026-05-19 · [GitHub](https://github.com/TilmanGriesel/chipper) · [官网](https://chipper.tilmangriesel.com/) · 个人维护

**面向折腾者的本地 RAG 工具：Web/CLI 界面与 Ollama 代理**

基于 Haystack、Ollama、Hugging Face、Docker 与 ElasticSearch 构建的 RAG 服务：提供文档分块、网页抓取、向量索引、可定制 RAG 管道与查询工作流，附 Web 界面和 CLI。可充当 Ollama 客户端（如 Enchanted、Open WebUI）与 Ollama 实例之间的代理，为第三方客户端注入服务端知识库检索，支持本地与 Hugging Face 远程模型、API 密钥与 Bearer 认证、多实例链式分布式处理。作者声明为个人项目，不建议未经评估直接用于商业或生产环境。

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

- 文档分块、网页抓取、ElasticSearch 向量索引与可定制 RAG 管道
- 作为 Ollama API 代理，让任意 Ollama 客户端获得服务端 RAG 能力
- 本地 Ollama 与 Hugging Face 远程模型双支持
- 多实例链式分布式处理与 API 密钥/Bearer 认证

## 适用场景

- 为 Enchanted、Open WebUI 等 Ollama 客户端添加知识库检索
- 本地搭建私有 RAG 问答服务，数据不出本地
- 教学场景中演示与实验 RAG 管道架构

## 场景标签

`RAG` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Chipper** provides a web interface, CLI, and a modular, hackable, and lightweight architecture for RAG pipelines, 
> L31: - **Ollama API Proxy** - Extend Ollama with retrieval capabilities, enabling interoperability with clients like **E
> L75: Enhance every third-party Ollama client with server-side knowledge base embeddings, allowing server side model sele

## 星数曲线

```mermaid
xychart-beta
    title "TilmanGriesel/chipper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 484 --> 486
    line [485, 485]
```

2026-10-18 485 → 2026-10-28 485（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `74584d90ae2c` · [字段定义](../../DATASET.md)*
