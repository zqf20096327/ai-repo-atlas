# bearlike/Assistant

⭐ 44 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/bearlike/Assistant) · [官网](https://docs.mewbo.com/) · 个人维护

**开源 agent 工作栈：长任务自动化、代码库 wiki 问答与跨工具搜索**

面向企业系统运行长时 agent 的开源栈：以同一 harness 承载 agentic 任务（计划审批后按分支树监控）、基于 AST 三层记忆图谱生成仓库 wiki 并给出带路径行号引用的问答、通过 API/数据库/MCP 服务器接入多系统做 agentic 搜索，以及用同一框架构建 WASM 前端的 agentic 应用。权限按角色在运行前解析，每次模型调用写入带 token 计数的 trace。可通过终端、Web 控制台、Android 客户端与 REST API 访问，安装与部署见 docs.mewbo.com（含 Docker Compose 生产部署章节）。

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

- 仓库 AST 提升为三层记忆图谱，生成 wiki 页面与带路径行号引用的问答
- 长任务以分支树形式监控，可中途引导或停止，含模型回退与重试
- 以 API/数据库/MCP 服务器接入多系统，探针 agent 按可达性图路由搜索
- Agent Skills、agent 定义与 MCP 服务器按开放标准原样加载

## 适用场景

- 让长时 agent 按计划与调度在企业系统中执行任务并审计
- 对自有代码库生成结构化 wiki 并用自然语言提问
- 把分散在多个系统里的数据统一做 agent 搜索与问答

## 场景标签

`Agent 框架` `文档问答` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L14:  Agentic task automation, memory-graph documentation and Q&amp;A, and search across every tool you connect. Any mod
> L38: Indexing lifts a repository's ASTs into a three layer memory graph, so pages are generated from structure rather th

## 星数曲线

```mermaid
xychart-beta
    title "bearlike/Assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `94bc0950adfb` · [字段定义](../../DATASET.md)*
