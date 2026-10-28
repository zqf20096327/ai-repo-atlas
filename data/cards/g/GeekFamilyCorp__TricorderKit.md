# GeekFamilyCorp/TricorderKit

⭐ 32 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/GeekFamilyCorp/TricorderKit) · [官网](https://github.com/GeekFamilyCorp/TricorderKit) · 组织维护

**本地优先的 Agentic 知识操作系统，将意图转为可审计工作流**

CLI-first 的代理式知识操作系统：用户意图经 MainBrain 路由器转为可追溯、可测试、可复用的工作流，运行在本地机器上（Ollama/LiteLLM 网关运行代理，Neo4j+Qdrant 作知识库，SQLite 存记忆，Temporal 作工作流引擎）。提供 13 个插件（自主研究、GraphRAG、自改进学习引擎等）与单一 CLI。安全机制包括反提示注入、公私路由门、不可逆操作确认与自改进提案需人工审核。重组件为 Docker 可选 profile，无需 GPU，云端模型可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 意图→可追溯/可审计/可复用工作流的代理路由架构（13 插件）
- 编号版本化规则集与确定性质量门（反提示注入、秘密扫描、公私边界）
- 自改进循环仅产出提案，需测试通过+人工审核才晋升
- 附带离线基准与 634 个 CI 测试，可用 --selftest 复现

## 适用场景

- 在本地机器上搭建不外传数据的代理式知识库工作流
- 对代理的自主操作加治理门（秘密防泄漏、公私边界、不可逆确认）
- 运行自主研究与混合 RAG 工作流并审计其行为

## 场景标签

`Agent 框架` `知识库管理` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L66: Everything is **local-first**: the agent (Claude or a local model via the Ollama/LiteLLM gateway), the knowledge ba
> L90: `cli/tk.py` — one CLI: `status · doctor · skill · workflow · vault · research · project · security · mcp · rapport`
> L98: No. TricorderKit is local-first and runs against a local LLM (Ollama via a LiteLLM gateway with retry + local fallb

## 星数曲线

```mermaid
xychart-beta
    title "GeekFamilyCorp/TricorderKit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-28 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `746cc708d7a7` · [字段定义](../../DATASET.md)*
