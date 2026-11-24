# sergioazoc/context-architecture

⭐ 10 · TypeScript · NOASSERTION · 推送 2026-09-23 · [GitHub](https://github.com/sergioazoc/context-architecture) · [官网](https://context-architecture.dev/) · 个人维护

**让仓库结构对 AI 编码代理可读的架构规范站点**

由 Sergio Azócar 于 2025 年 10 月提出的软件架构规范：把仓库组织为对编码代理与人类维护者同时可读的结构，声明与机制绑定，声明失效时机制会失败。本仓库是规范的权威站点（prerendered SSG），每个页面提供人类排版视图与代理消费的 Markdown 视图（同一 .md 源）。可通过 `npx skills add` 把 agent skill 装入 Claude Code、Cursor、Codex、Copilot 等工具，站点自身作为规范的第一个案例研究。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一 .md 源生成人类视图与 agent 视图两种阅读形态
- 提供可一键安装到多种编码代理工具的 SKILL.md
- 全静态预渲染，无 JavaScript 依赖以便爬虫与 LLM 读取
- 规范采用 spec 先于代码、转为代码与 AGENTS.md 后移除的流程

## 适用场景

- 让 AI 编码代理更准确理解仓库结构与约束
- 为已有仓库补齐代理可读的结构与 AGENTS.md
- 以规范驱动的方式开展 AI 辅助开发

## 场景标签

 · 领域:软件工程/AI 编码方法

## 证据(README 行号)

> L3: Context Architecture is a software architecture for the age of AI agents: it structures a repository so
> L31: - Install the agent skill into your tool with one command, `npx skills add sergioazoc/context-architecture`

## 星数曲线

```mermaid
xychart-beta
    title "sergioazoc/context-architecture 星数(近 2 点)"
    x-axis ["2026-11-02", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-02 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `5fde49227164` · [字段定义](../../DATASET.md)*
