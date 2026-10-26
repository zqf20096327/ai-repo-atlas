# alexey-max-fedorov/gaia-ai

⭐ 53 · Markdown · 推送 2026-10-25 · [GitHub](https://github.com/alexey-max-fedorov/gaia-ai) · [官网](https://gaiacode.pro) · 个人维护

**运行在 Perplexity Spaces 上的 Claude Code 式 agent 提示词系统**

由四个提示词文件驱动四个引擎（门控/行为/记忆规划/回合预算），部署方式是粘贴 SYSTEM_INSTRUCTIONS 到 Space 指令框并上传其余三个文件为 Space Files。提供持久记忆（MEMORY.md，跨自动压缩存活）、计划引擎（PLAN.md+TASKS.md 勾选式任务）、上下文预算与 15 次调用工具预算、GitHub MCP 读写仓库、斜杠命令技能引擎与三种权限模式。推荐模型为 GLM-5.2 或 Claude Sonnet 5.0 Thinking。附 Next.js 营销站。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 持久记忆 MEMORY.md 跨自动压缩存活，支持 export/import memory
- 计划引擎：探索→计划→批准→执行，任务级勾选
- GitHub MCP：读仓库、建分支、推提交、开 PR、管 issue
- 技能引擎：斜杠命令技能，可从 GitHub 仓库直接安装

## 适用场景

- 在 Perplexity Spaces 中搭建带记忆与计划的编码 agent
- 让 agent 通过 GitHub MCP 直接读写我的仓库、开 PR
- 用权限模式控制 agent 的写操作审批粒度

## 场景标签

`提示工程` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: GAIA Code is a Claude Code-inspired prompt system for Perplexity Spaces. It brings persistent memory, a plan engine,
> L23: GAIA Code is **four prompt files** that drive **four engines**.
> L31: Identity, tool philosophy, dependency & version rules (versions are pinned from the registry's JSON API, never a st

## 星数曲线

```mermaid
xychart-beta
    title "alexey-max-fedorov/gaia-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-26 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `988341a9d53b` · [字段定义](../../DATASET.md)*
