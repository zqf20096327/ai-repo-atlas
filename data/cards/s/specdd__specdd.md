# specdd/specdd

⭐ 41 · HTML · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/specdd/specdd) · [官网](https://specdd.ai) · 组织维护

**给人类与 AI agent 共用的规格驱动开发框架（.sdd 文件）**

SpecDD 是开源的规格驱动开发框架：在代码、基础设施或文档旁放置小型 .sdd 规格文件，记录意图、边界、任务与完成标准，作为人类开发者与 AI 编码 agent 共享的局部事实来源。通过官方 CLI（需 Node.js 22+，支持 npm/Yarn/Homebrew/Docker 安装）初始化项目，agent 读取 .specdd/bootstrap.md 后按规格链实施。agent 无关，兼容 Codex、Claude Code、Copilot、Cursor 等主流编码 agent；语言无关，无 AI 也可单独使用。含 DSD、Flow、SSG、Zen 四个官方插件，插件可自行开发分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 代码旁的同名 .sdd 规格文件作为人机共享局部事实来源
- agent 无关：兼容 OpenAI Codex、Claude Code、Copilot、Cursor 等主流编码 agent
- 官方 CLI 支持 npm/Yarn/Homebrew/Docker 四种安装途径
- 四个官方插件（DSD/Flow/SSG/Zen）可扩展文档类型与工作流，插件可自建分发

## 适用场景

- 让 AI 编码 agent 依据仓库内评审过的规格实现功能，减少反复纠错
- 为存量项目逐步补充局部规格，保留模块意图与边界
- 新人接手或评审时对照局部契约而非追溯历史讨论

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: SpecDD™ is an open-source framework for **spec-driven development** in software, infrastructure, automation,
> L23: After initialization, place small `.sdd` specs beside the files or project areas they describe. If your AI agent do
> L24: not automatically read the SpecDD bootstrap, tell it to read `.specdd/bootstrap.md` before it starts working. The a
> L250: SpecDD is useful without AI because it gives humans a shared, local, reviewable contract for intent, behavior, and

## 星数曲线

```mermaid
xychart-beta
    title "specdd/specdd 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-25 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ee9d585820af` · [字段定义](../../DATASET.md)*
