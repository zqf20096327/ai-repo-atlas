# Reza-esfandiarpoor/the-mcp-company

⭐ 16 · Python · 推送 2025-12-19 · [GitHub](https://github.com/Reza-esfandiarpoor/the-mcp-company) · [官网](https://arxiv.org/abs/2510.19286) · 组织维护

**评测工具调用 agent 的基准：18,000+ MCP 工具任务**

面向 LLM 工具调用 agent 的评测基准：用真实服务的 REST API 构建 MCP 服务器，包含超过 18,000 个工具，并为每个任务提供人工标注的 ground-truth 工具；通过 ground-truth 与工具检索两种设定衡量 agent 表现，并与浏览器型 agent 对照。运行需先部署 TheAgentCompany 的 docker 容器环境或配置 Azure 账号与服务主体，再运行 MCP 服务器并借助 OpenHands 执行评测。附 ArXiv 论文与 BibTeX 引用条目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于真实服务 REST API 构建的 MCP 服务器，含 18,000+ 工具
- 每个任务提供人工标注的 ground-truth 工具
- 支持 ground-truth 工具与工具检索两种实验设定
- 与浏览器型 agent 进行对照评测

## 适用场景

- 评测工具调用 agent 在真实服务任务上的表现
- 研究工具检索对 agent 性能与成本的影响
- 检验模型在大量工具中导航组合的能力

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: > Since the introduction of the Model Context Protocol (MCP), the number of available tools for Large Language Model

## 星数曲线

```mermaid
xychart-beta
    title "Reza-esfandiarpoor/the-mcp-company 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7e1fcfb5c2cf` · [字段定义](../../DATASET.md)*
