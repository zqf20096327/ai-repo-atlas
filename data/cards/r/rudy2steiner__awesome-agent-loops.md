# rudy2steiner/awesome-agent-loops

⭐ 10 · Python · CC0-1.0 · 推送 2026-10-14 · [GitHub](https://github.com/rudy2steiner/awesome-agent-loops) · [官网](https://agentloophub.com) · 个人维护

**AI 编程 agent 循环工程模式与工具的策展清单**

以「loop engineering」为主题的 awesome 清单：围绕让编程 agent 自主发现工作、执行、验证、持久化状态并决定下一步的循环设计，收录概念指南、起源文章与演讲、五种循环模式（Ralph、maker–checker、队列消耗、定时刷新、子 agent 扇出）、模板与运行时/调度/验证/状态/成本控制各类资源。清单自身通过 agent 循环自动更新、人工审核合并，以 CC0 许可发布，由 agentloophub.com 维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种循环模式分类：Ralph、maker–checker、queue-drain、cron refresh、subagent fan-out
- 七字段格式（goal/trigger/discover/act/verify/persist/exit）的循环模板
- 清单自身由 agent 循环自动更新，人工审批每次合并
- 覆盖调度触发、验证护栏、状态记忆与成本控制四类配套资源

## 适用场景

- 为 Claude Code 等编程 agent 设计自动循环工作流
- 按模式选型自主编码循环的验证与护栏方案
- 查找控制 agent 循环 token 成本与退出条件的方法

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L3: > Loops, not prompts. A curated list of patterns, tools, templates and writing on **loop engineering** — designing s
> L41: - Claude Code - Agentic CLI with built-in `/goal` condition loops; the reference runtime for most loop writing toda

## 星数曲线

```mermaid
xychart-beta
    title "rudy2steiner/awesome-agent-loops 星数(近 2 点)"
    x-axis ["2026-11-20", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-20 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `7865e45a3f60` · [字段定义](../../DATASET.md)*
