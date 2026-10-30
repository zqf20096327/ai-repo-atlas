# kyegomez/PROMPTS.md

⭐ 33 · MIT · 推送 2026-04-30 · [GitHub](https://github.com/kyegomez/PROMPTS.md) · [官网](https://swarms.ai) · 个人维护

**面向开发者的 AI 上下文文件机制讲解指南**

一份解释性文档（指南），讲解 CLAUDE.md、MEMORY.md、SKILLS.md、SOUL.md 四类 agent 上下文文件的用途与差异：CLAUDE.md 定义项目级操作指令，MEMORY.md 跨会话持久化事实与偏好，SKILLS.md 以自然语言登记可调用能力，SOUL.md 定义 AI 身份、价值观与沟通风格。面向开发者与高级用户，说明各文件内容结构、加载顺序（SOUL→SKILLS→CLAUDE→MEMORY）及如何组合为系统提示层；内容基于 Claude 生态（Claude Code、Claude.ai、Anthropic 文档），属于知识讲解而非可安装运行的软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐章解释四类上下文文件的定义、内容结构与使用时机
- 给出组合公式 System Prompt = SOUL.md + SKILLS.md + CLAUDE.md + MEMORY.md 及加载顺序
- 覆盖手动/代理辅助/自动记忆系统三种 MEMORY.md 更新方式
- 辨析 Tools（Anthropic）/ Functions（OpenAI）/ Skills（agent 框架）术语差异

## 适用场景

- 为我的 Claude Code 项目编写 CLAUDE.md 前了解应写什么
- 为个人 AI 助手设计持久记忆与人格定义文件
- 理解 SKILLS.md 与正式 tool 定义的关系与分工

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Understanding CLAUDE.md, MEMORY.md, SKILLS.md, SOUL.md, and Related Prompting Mechanisms**
> L7: This guide explains what each of these files is, why they exist, how they differ from one another, and how developer
> L17: Think of these files collectively as a "personality package" or "agent configuration layer." Together they answer f

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/PROMPTS.md 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `03251fca3a85` · [字段定义](../../DATASET.md)*
