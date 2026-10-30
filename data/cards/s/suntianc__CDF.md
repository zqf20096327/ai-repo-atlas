# suntianc/CDF

⭐ 15 · TypeScript · AGPL-3.0 · 推送 2026-07-30 · [GitHub](https://github.com/suntianc/CDF) · 个人维护 · 中文 README

**离线优先的桌面 Agent 工作台：本地编排 AI 订阅与工作流**

基于 Electron 的本地优先桌面应用，将项目、对话、场景技能、Agent 活动、工作流与产物保存在同一本地上下文（SQLite 存储 + 用户选定目录）。提供 General 与 Research 两种场景，后者含论文库与检索/阅读/审稿技能链。通过 AI Subscriptions 接入用户已有账号（MiniMax Token Plan、Codex OAuth、xAI Grok OAuth），按阶段运行工作流并保留门控决策记录。本地运行需 Node.js 22+ 与 pnpm，从源码构建，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入 MiniMax Token Plan、Codex OAuth、xAI Grok OAuth 三类既有账号路由
- 分阶段工作流运行（Stage Gates）保留审批、失败与输出记录
- Research 场景含本地论文库与内置研究技能链
- 本地 SQLite 存储与最小 preload IPC 边界，Electron 安全隔离

## 适用场景

- 在本地统一管理研究项目的对话、文献与工作流产物
- 用已有模型订阅账号驱动多阶段任务并审查每个决策点
- 日常多模态工作与学术写作/审稿在同一桌面工作台完成

## 场景标签

`工作流自动化` `科研工具` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L9: CDF is an **offline-first desktop Agent workstation** for work that should outlive a chat tab. It keeps a local Proj
> L27: **AI Subscriptions** exposes supported routes from accounts you already use:
> L39: Workflow Runs turn a complex task into named Stages. A selected model drives the Master Agent, Stage Gates pause at

## 星数曲线

```mermaid
xychart-beta
    title "suntianc/CDF 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `0583faa87822` · [字段定义](../../DATASET.md)*
