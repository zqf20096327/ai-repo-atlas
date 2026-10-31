# chrisallenlane/claude-swe-workflows

⭐ 18 · MIT · 推送 2026-05-18 · [GitHub](https://github.com/chrisallenlane/claude-swe-workflows) · 个人维护

**Claude Code 的可组合软件工程工作流技能集**

面向 Claude Code 的插件，提供一组按命名空间组织的斜杠命令技能：/lead-* 自主编排器（OODA 循环的技术负责人、bug 收敛循环、综合重构、全维度审查）、/implement-* 工单实现、/scope-* 规划出票、/review-* 只读审计（架构/测试/性能/可访问性/安全等）、/think-* 推理技能、以及 /bug-*、/tidy-*、/test-mutation 等。技能采用分层组合：高层技能调用低层技能，可按任务层级进入。通过 claude plugin 命令安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分层组合架构：从单工单到多批次项目使用同一套技能栈
- /lead-project 等自主编排器以 commander's intent 驱动 OODA 循环
- 覆盖规划、实现、审查、推理、bug、整洁与测试的 8 类命名空间技能
- /review-* 技能只审计不改代码，/think-* 只产出反馈不产出工件

## 适用场景

- 让 Claude Code 自主推进整个项目的规划与实现
- 对代码库做架构、安全、测试、可访问性等多维审计
- 以对抗性推理技能压力测试方案与决策

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: A system of composable software engineering workflows for [Claude Code][cc].
> L10: claude plugin marketplace add https://github.com/chrisallenlane/claude-swe-workflows.git

## 星数曲线

```mermaid
xychart-beta
    title "chrisallenlane/claude-swe-workflows 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `89f0eddedb6e` · [字段定义](../../DATASET.md)*
