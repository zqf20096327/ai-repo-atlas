# SKZL-AI/tscg

⭐ 24 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/SKZL-AI/tscg) · [官网](https://github.com/SKZL-AI/tscg#readme) · 组织维护

**将 JSON 工具 Schema 确定性压缩为紧凑文本的 LLM agent 库**

TSCG（Token-Context Semantic Grammar）是一组 TypeScript npm 包，通过确定性变换（8 个算子，无需模型调用或微调）把 JSON 工具 Schema 编译为紧凑结构化文本，供 LLM agent 在文本模式下使用工具，面向构建 agent 的开发者。包含核心压缩引擎、MCP stdio 透明代理中间件，以及 LangChain/Vercel AI SDK 集成包；另有只压缩 description 字段、保留原生 tool-calling 兼容的模式。README 明确声明准确率效果依模型/profile/基线而异，压缩不执行工具，小模型场景存在回退。附两篇 arXiv 论文，TAB 为作者自建基准，BFCL 为外部 Schema 验证而非官方榜分。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性变换压缩工具 Schema，无需模型调用或微调
- 支持无原生 tool calling 的模型走文本模式工具调用
- MCP stdio 代理对任意 MCP 服务器透明压缩
- description-only 模式保留 JSON Schema 结构，兼容原生 tool-calling API

## 适用场景

- 工具数量多导致 Schema 挤占上下文预算的 agent 部署
- 给不支持原生 function calling 的本地小模型加工具能力
- 通过 MCP 代理为 Claude Code 等 MCP 客户端压缩工具定义
- 受限上下文预算下为 agentic RAG 腾出检索空间

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: **TSCG (Token-Context Semantic Grammar) compiles JSON tool schemas into compact structured text for LLM agents.** De
> L164: `@tscg/mcp-proxy` sits between Claude Code (or any MCP client) and your MCP tool servers, transparently compressin
> L185: import { withTSCG } from '@tscg/tool-optimizer/langchain';

## 星数曲线

```mermaid
xychart-beta
    title "SKZL-AI/tscg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bb778094cb97` · [字段定义](../../DATASET.md)*
