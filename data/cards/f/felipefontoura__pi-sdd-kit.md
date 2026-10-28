# felipefontoura/pi-sdd-kit

⭐ 36 · MIT · 推送 2026-10-21 · [GitHub](https://github.com/felipefontoura/pi-sdd-kit) · [官网](https://felipefontoura.com/get/sdd-book/?utm_source=github&utm_medium=referral&utm_campaign=pi-sdd-kit&utm_content=about) · 个人维护

**Pi 编程 Agent 的规格驱动开发（SDD）技能包**

面向 Pi 编程 Agent 的技能包，实现规格驱动开发工作流：IDEA→PLAN→PRD→SPEC→TASKS→EXEC→REVIEW 流水线。核心机制包括：`.ai/steering/` 作为跨会话的持久项目记忆；每个特性一个 `.status` 文件作为唯一的阶段推进门（人工审批后才允许实现）；EARS 语法撰写功能需求；稳定 ID（US/FR/NFR/TD/T）实现需求到任务的追溯；可选的上游/下游 handoff 简报衔接多包流水线。通过 `pi install` 命令安装，自带可复制模板，运行时按用户聊天语言生成交付物。

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

- .status 文件作为唯一审批门，草稿不解锁阶段推进
- steering 目录保存跨会话复用的项目全局上下文
- EARS 语法需求 + 稳定 ID 的需求→设计→任务→评审追溯
- 上游/下游 handoff 简报支持接入更大的多包流水线

## 适用场景

- 在 Pi 编程 Agent 中按规格驱动流程从想法推进到实现
- 小中型项目中强制人工审批门，避免实现前需求未定
- 跨多次会话保持一致的项目上下文与规范记忆

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A skill pack for the Pi Coding Agent that implements a practical **Specification-Driven Development (SDD)** workflow

## 星数曲线

```mermaid
xychart-beta
    title "felipefontoura/pi-sdd-kit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-28 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e32765301269` · [字段定义](../../DATASET.md)*
