# MorningStar0709/trae-agent-enhancements

⭐ 18 · Python · MIT · 推送 2026-05-12 · [GitHub](https://github.com/MorningStar0709/trae-agent-enhancements) · [官网](https://github.com/MorningStar0709/trae-agent-enhancements) · 个人维护 · 中文 README

**Trae IDE Agent 的规则+技能+记忆增强集合**

面向 Trae IDE 的 AI Agent 增强框架：8 条规则负责任务路由与行为约束，35 个技能覆盖设计→编码→调试→提交→完成→记忆流程，并通过 Core Memory（每作用域 20 条上限、自动淘汰）与 MCP Memory Server 知识图谱构成双轨持久记忆。提供 T 恖码任务分级（S/M/L）与闭环验证机制。支持中文触发词与国内 Git 平台，Windows 环境采用 PowerShell 命令与路径约定。经 npx 安装到用户目录，部分技能需配置 Everything Search、Chrome DevTools 等 MCP Server 才能完整工作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 条规则 + 35 个技能 + 双轨记忆（Core Memory + MCP Memory）三层架构
- T 恖码任务分级 S/M/L，小任务快、大任务严谨
- 中文触发词、国内 Git 平台支持、双语技能文件
- Windows 原生适配：PowerShell 命令、端口冲突恢复、路径约定

## 适用场景

- 让 Trae IDE 中的 Agent 按规则路由并稳定执行开发任务
- 跨会话积累经验教训，避免重复错误
- 用中文指令触发调试、计划、验证、提交等技能

## 场景标签

`Agent 框架` `提示工程` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Trae AI Agent Enhancements** is a Trae AI Agent rules and skills collection for Trae IDE. It provides Rule-based 
> L16: User Input → Rules (Routing & Constraints) → Skills (Execution) → Memory (Learning)
> L22: |**Skills**|35|Professional toolboxes covering design → coding → debugging → commit → completion → memory|

## 星数曲线

```mermaid
xychart-beta
    title "MorningStar0709/trae-agent-enhancements 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7ce841a46ba4` · [字段定义](../../DATASET.md)*
