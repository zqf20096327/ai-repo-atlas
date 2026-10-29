# feuersteiner/contextrie

⭐ 61 · TypeScript · MIT · 推送 2026-10-08 · [GitHub](https://github.com/feuersteiner/contextrie) · [官网](https://discord.gg/2xS7TEzGvc) · 个人维护

**为长程 agent 工作流动态筛选与组装上下文的工具包**

面向 agent 系统的 context-engineering 工具包，提供定义内容源、生成源元数据、按任务打分相关性、组装下一步工作上下文等原语。两种使用方式：以 @contextrie/core 与 @contextrie/parsers 库嵌入自有 agent 系统，或用 @contextrie/cli 本地 CLI 索引项目文件并生成 .contextrie/context.md。解析器支持 .csv/.md/.txt，另有规划中的 coding-agent harness、benchmark 协议与 Python 镜像库。项目自述处于早期开发阶段，可能有不兼容变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CLI 索引本地文件并组装任务专属上下文到 .contextrie/context.md
- 核心原语：源定义、元数据生成、任务相关性打分、上下文组装
- 库形式（@contextrie/core、@contextrie/parsers）可嵌入自有 agent 系统
- 支持 --openai-base-url 指向 OpenAI 兼容提供方

## 适用场景

- 长程 agent 系统中控制每步可见的上下文以减少无关内容
- 为 coding agent 准备任务相关的精简上下文
- 对项目文件建索引并按任务生成上下文文档

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L16: AI agents get worse as irrelevant context piles up. Contextrie helps you select, index, judge, and compose the righ
> L18: Contextrie is a context-engineering toolkit for agent workflows.
> L22: - as a library inside your own agent system with `@contextrie/core` and `@contextrie/parsers`

## 星数曲线

```mermaid
xychart-beta
    title "feuersteiner/contextrie 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 59 --> 62
    line [60, 61, 61]
```

2026-10-18 60 → 2026-10-29 61（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `efcd7dd6877f` · [字段定义](../../DATASET.md)*
