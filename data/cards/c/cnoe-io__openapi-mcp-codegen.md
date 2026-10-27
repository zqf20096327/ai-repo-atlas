# cnoe-io/openapi-mcp-codegen

⭐ 42 · Python · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/cnoe-io/openapi-mcp-codegen) · [官网](https://cnoe-io.github.io/openapi-mcp-codegen/) · 组织维护

**从 OpenAPI 规范生成 MCP Server 的 Python 代码生成器**

解析 OpenAPI 规范（JSON/YAML），通过 Jinja2 模板渲染生成结构化 Python MCP server：为每个 API 端点生成工具模块、httpx API 客户端代码、配置文件与文档，供 AI 助手调用 API 使用。可选生成 LangGraph React agent（含 A2A server、Makefile）、基于 LangFuse 的评测套件、用配置的 LLM 生成 SYSTEM prompt 与增强 docstring 的 OpenAPI Overlay。SLIM 传输与 A2A proxy 支持标注为实验性。面向构建 agent 工具链的开发者，需 uv 作为依赖管理与执行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从 OpenAPI 规范自动生成 MCP server（STDIO 模式，含工具模块与 httpx 客户端）
- --generate-agent 额外生成 LangGraph React agent 与 A2A server
- --generate-eval 生成 LangFuse 驱动的评测数据集构建与评估脚本
- LLM 增强的 OpenAPI Overlay 文档（描述、参数折叠处理）

## 适用场景

- 把已有 REST API 快速包装成 MCP server 供 AI 助手调用
- 为生成的 agent 配套生成评测数据集与自动评估流程
- 用 LLM 优化复杂 API 的工具描述以提升 agent 选择准确率

## 场景标签

`代码生成` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L13: This tool generates **Model Context Protocol (MCP) servers** from OpenAPI specifications, creating Python packages 
> L47: - Optionally, it generates an accompanying LangGraph agent and A2A server wrapper that can call the generated MCP t

## 星数曲线

```mermaid
xychart-beta
    title "cnoe-io/openapi-mcp-codegen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `339ef10ca64e` · [字段定义](../../DATASET.md)*
