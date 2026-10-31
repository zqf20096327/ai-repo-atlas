# duriantaco/sago

⭐ 14 · Python · Apache-2.0 · 推送 2026-04-17 · [GitHub](https://github.com/duriantaco/sago) · 个人维护

**给 AI 编码代理做项目规划与进度管控的 CLI 工具**

面向 AI 编码代理（Claude Code、Cursor、Aider 等）使用者的规划与控制平面工具：用 LLM 从 Markdown 项目描述生成含原子任务、依赖排序与验证命令的 PLAN.md，自身不执行任务；提供 sago plan/replan/checkpoint/watch 等命令跟踪阶段进度，生成浏览器实时仪表盘，并产出 CLAUDE.md 等代理指令文件。LLM 经 LiteLLM 接入任意提供商，仅用于规划与审查。需 Python 3.11+，pip 源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 PROJECT.md/REQUIREMENTS.md 生成结构化 PLAN.md 并做语义校验（循环/重复 ID 检测）
- sago watch 实时浏览器仪表盘：进度、文件活动、阶段树，每秒轮询 STATE.md
- 生成 CLAUDE.md/.cursorrules 等代理指令文件，兼容任意能读文件执行命令的编码代理
- LiteLLM 接入任意提供商，支持 ChatGPT 订阅 OAuth 模式，无 API key

## 适用场景

- 让编码代理按分阶段计划构建整个项目，避免遗漏需求
- 在阶段间审查完成情况并调整计划
- 实时监控代理的任务执行进度

## 场景标签

 · 领域:开发工具/AI 代理编排

## 证据(README 行号)

> L13: Sago is a **planning and control-plane tool**, not a coding agent. It turns your project idea into a structured, ve
> L21: Sago does not execute project tasks itself. The intended workflow is:
> L309: **Sago fills that gap.** It uses an LLM to generate a structured, verified plan with atomic tasks, dependency orde

## 星数曲线

```mermaid
xychart-beta
    title "duriantaco/sago 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8fa37e33b100` · [字段定义](../../DATASET.md)*
