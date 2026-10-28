# codefromkarl/ContextAtlas

⭐ 30 · TypeScript · MIT · 推送 2026-06-02 · [GitHub](https://github.com/codefromkarl/ContextAtlas) · [官网](https://github.com/codefromkarl/ContextAtlas/tree/main/docs) · 个人维护 · 中文 README

**面向 AI 编码 agent 的代码上下文基础设施：混合检索与项目记忆**

以 CLI、MCP 服务器或可嵌入库形式提供的开源上下文基础设施，服务 AI 编码 agent：用 Tree-sitter 做语义分块，LanceDB 向量检索与 SQLite FTS5 全文检索经 RRF 融合与重排，再做图扩展与 token 预算内的上下文打包；提供项目记忆、长期记忆、跨项目记忆 Hub，以及检索监控、索引健康检查等可观测能力。限定于决定提供什么上下文，不处理 agent 推理与任务编排。npm 全局安装，需 Node.js 20+，配置 embeddings API key 后运行。

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

- 向量+FTS 混合检索、RRR 融合、重排与图扩展
- token 预算内的上下文打包
- 项目记忆/长期记忆/跨项目 Hub 三层记忆体系
- 以 CLI、MCP 服务器、可嵌入库三种方式接入

## 适用场景

- 为 Claude Code、Codex 等编码 agent 提供仓库检索后端
- 通过 MCP 让桌面客户端调用代码检索与记忆工具
- 在脚本、CI 与工作流自动化中作为本地 CLI 检索后端

## 场景标签

`Agent 记忆` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L22: **ContextAtlas** is an open-source context infrastructure for AI coding agents — providing hybrid code retrieval, p
> L54: - As a repository retrieval backend for coding agents
> L72: ContextAtlas decides **what context to provide**, not **how the task should be executed**. It does not handle agent

## 星数曲线

```mermaid
xychart-beta
    title "codefromkarl/ContextAtlas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `47e6a9b1ab06` · [字段定义](../../DATASET.md)*
