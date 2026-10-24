# Zleap-AI/Zleap-Agent

⭐ 219 · TypeScript · Apache-2.0 · 推送 2026-08-05 · [GitHub](https://github.com/Zleap-AI/Zleap-Agent) · [官网](https://zleap.com) · 组织维护 · 中文 README

**面向本地小参数模型的 workspace 优先 agent 运行框架**

Node.js 编写的 agent harness，面向本地与 OpenAI 兼容模型。核心机制是 workspace 隔离：每个 workspace 拥有独立的 prompt、工具、技能、记忆、模型与执行历史，上下文按 System Prompt + Workspace Prompt + Tools + Memory + History 布局，避免小模型每步加载全部上下文。记忆按 Person/Event/Experience 分区，存于 PostgreSQL（含 pgvector）。提供 Web UI 与共用同一运行时的 CLI，支持 MCP 工具、审批/全权两种权限模式、任务 worker 与 IM gateway。处于 early preview 阶段，API 与打包可能变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- workspace 级隔离：prompt、工具、技能、模型、记忆、历史独立配置
- 分区式记忆（Person/Event/Experience）基于 PostgreSQL + pgvector 持久化
- Web UI 与 CLI 共用同一运行时
- OpenAI 兼容模型 provider 支持，含 Anthropic provider 代码

## 适用场景

- 在本地小参数模型上运行上下文可控的 agent 工作流
- 按权限与数据边界划分的多 workspace 企业本地部署
- 通过 CLI 对仓库或项目执行一次性 agent 任务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L15: Zleap-Agent is a workspace-first agent harness for local and OpenAI-compatible
> L26: This makes the system easier to reason about when running smaller local models,

## 星数曲线

```mermaid
xychart-beta
    title "Zleap-AI/Zleap-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 218 --> 220
    line [219, 219]
```

2026-10-18 219 → 2026-10-24 219（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `e4b6e1931daa` · [字段定义](../../DATASET.md)*
