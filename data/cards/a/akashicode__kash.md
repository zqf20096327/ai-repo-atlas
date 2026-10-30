# akashicode/kash

⭐ 16 · Go · 推送 2026-10-24 · [GitHub](https://github.com/akashicode/kash) · [官网](https://akashicode.github.io/kash/) · 个人维护

**把文档目录编译为单容器 GraphRAG agent 的 Go CLI**

Kash 是用 Go 编写的命令行工具：用 `kash build` 将 PDF、Markdown、文本等文档一次性编译成向量（chromem-go）、图（cayley）与 BM25 三个嵌入式索引，产出单个约 50MB 的 Docker 容器，内含 REST API（OpenAI 兼容端点）、MCP server 与离线 dashboard。检索采用四路（向量/BM25/精确引用/图）并做 RRF 融合，图三元组记录来源段落、可用 `kash verify` 审计。支持任意 OpenAI 兼容 API（OpenAI、Ollama、LiteLLM 等），构建与运行时模型通过配置文件与环境变量指定。不做 OCR；增量构建可断点续传。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档一次性编译进单个 ~50MB 容器，向量/图/BM25 索引全部内嵌
- 四路检索（向量/BM25/精确引用/图）RRF 融合
- 知识图谱三元组带段落级溯源，`kash verify` 审计可追溯率
- 提供 REST（OpenAI 兼容）、MCP、A2A（WIP）三种接口与内置 dashboard

## 适用场景

- 把一批内部文档打包成一个可 `docker run` 的问答 agent
- 通过 MCP 将知识库暴露为 Claude/Cursor/Windsurf 的工具
- 以 OpenAI 兼容端点替换现有服务获得 RAG 增强回答

## 场景标签

`RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L5: *A compiler for knowledge. Turn a folder of documents into a self-contained GraphRAG agent you can `docker run`.*
> L24: RAG usually means a Python service, a hosted vector database, a graph server, and glue to hold them together. **Kas
> L203: |🌐 **REST API**|`POST /v1/chat/completions`|Drop-in OpenAI replacement with RAG context injected|

## 星数曲线

```mermaid
xychart-beta
    title "akashicode/kash 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `94f0580486e5` · [字段定义](../../DATASET.md)*
