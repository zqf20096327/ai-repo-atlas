# cool-japan/oxify

⭐ 14 · Rust · Apache-2.0 · 推送 2026-09-16 · [GitHub](https://github.com/cool-japan/oxify) · [官网](https://github.com/cool-japan/oxify) · 个人维护

**Rust 编写的图式 LLM 工作流编排平台，用 DAG 组合 AI 应用**

OxiFY 是基于 Rust 的工作区项目（13 个 crate），以有向无环图（DAG）定义 LLM 应用：LLM、向量检索、OCR、条件分支、子工作流等 16+ 种节点，经拓扑排序与层级并行执行。提供 OpenAI/Anthropic/Ollama 三类 LLM 接入、Qdrant/pgvector 向量库、MCP 支持、30+ REST 端点、ReBAC/JWT 认证，分布式执行基于 CeleRS，另带 CLI（55+ 命令）。通过 git clone 加 cargo build 安装，无预编译桌面包；Web UI 与 Docker/K8s 部署在 Roadmap 中尚未实现。版本 0.1.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DAG 执行引擎：拓扑排序、层级并行、重试与检查点/暂停恢复
- LLM 提供方：OpenAI、Anthropic、Ollama（含 SSE 流式与响应缓存）
- MCP 原生支持：可作为 MCP server 暴露工作流、调用外部 MCP 工具
- ReBAC（Zanzibar 风格）授权 + JWT/OAuth2 认证 + 30+ REST 端点

## 适用场景

- 以 DAG 编排多步骤 LLM/RAG 工作流并分布式执行
- 本地用 CLI 验证与运行工作流，或部署 API 服务
- 通过 MCP 将工作流暴露为工具供 agent 调用

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **OxiFY** is a graph-based LLM workflow orchestration platform built in Rust, designed to compose complex AI applica
> L30: - **oxify-engine**: DAG execution engine with CeleRS integration

## 星数曲线

```mermaid
xychart-beta
    title "cool-japan/oxify 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a9854389dbf2` · [字段定义](../../DATASET.md)*
