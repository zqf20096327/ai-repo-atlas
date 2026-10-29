# alivecontext/alive

⭐ 131 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/alivecontext/alive) · [官网](https://alivecontext.com) · 组织维护

**Claude Code 的个人上下文管理插件：会话知识文件化沉淀**

面向 Claude Code 用户的上下文管理运行时插件：把用户的工作、决策、人物与知识以纯文件结构（walnut/bundle）存放在本机，会话开始时加载身份与状态，结束时将决策、任务、知识等路由到对应文件，使上下文跨会话累积。运行时可移植于不同底层模型，包含 15 个技能命令、6 个规则文件、hooks 与状态栏。安装经 Claude Code 插件市场，需 Claude Code 与 Python 3，支持 macOS/Linux/Windows(WSL)。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- walnut/bundle 文件结构管理上下文，会话开始加载、checkpoint 保存
- 15 个技能命令（加载/保存/检索/图谱/升级等）
- 上下文为本机纯文件，无云无账号，可 Git 追踪
- 升级命令支持从 v1 起任意旧版本迁移并备份回滚

## 适用场景

- 让 Claude Code 会话继承此前的决策与项目知识，避免重复解释
- 按生活领域（创业项目、人物、实验）组织个人知识
- 将工作流打包为可分享的 bundle 供他人安装

## 场景标签

`知识库管理` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L17:  Personal Context Manager for Claude Code
> L32: Open Claude Code at your `~/world`. The runtime is already loaded.
> L34: ALIVE structures your context into plain files on your machine. Agents read them at session start and save what mat

## 星数曲线

```mermaid
xychart-beta
    title "alivecontext/alive 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 129 --> 132
    line [130, 131, 131]
```

2026-10-18 130 → 2026-10-29 131（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0957e1d9b846` · [字段定义](../../DATASET.md)*
