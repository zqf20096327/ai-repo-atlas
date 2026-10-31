# milosgajdos/go-embeddings

⭐ 60 · Go · Apache-2.0 · 推送 2026-09-21 · [GitHub](https://github.com/milosgajdos/go-embeddings) · 个人维护

**Go 库：从多家 LLM 提供商获取 embeddings 的 API 客户端**

提供多个 embeddings 提供商的 Go API 客户端实现，支持 OpenAI、Cohere、Google Vertex、VoyageAI、Ollama、AWS Bedrock 六种 API，各客户端可从环境变量读取 API key 初始化默认客户端。另含 document 包，实现字符与递归字符文本分割器，为 Langchain 对应功能的 Go 重写。cmd 目录提供各提供商的示例程序，项目提供 nix flake 构建开发环境。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六种 embeddings 提供商的统一 Go 客户端（OpenAI/Cohere/Vertex/Voyage/Ollama/Bedrock）
- 环境变量读取 API key 初始化默认客户端
- document 包提供 Langchain 文本分割器的 Go 重写
- nix flake 支持一致的开发与构建环境

## 适用场景

- 在 Go 项目中接入多家 embeddings 提供商
- 从 Ollama 等本地运行时获取文本向量
- 对文档做字符/递归字符切分后再向量化

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: This project provides an implementation of API clients for fetching embeddings from various LLM providers.
> L9: Currently supported APIs:

## 星数曲线

```mermaid
xychart-beta
    title "milosgajdos/go-embeddings 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-31 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `28b92e5a8909` · [字段定义](../../DATASET.md)*
