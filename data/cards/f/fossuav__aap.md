# fossuav/aap

⭐ 19 · Python · GPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/fossuav/aap) · 组织维护

**ArduPilot 平台的 LLM 代码生成规则手册与技能包**

面向 ArduPilot 自动驾驶仪开发者的指导文档项目：为使用 LLM（Claude Code、Codex、Gemini CLI 或对话式 LLM）生成与修改 ArduPilot 代码提供规则和约束，包括 18 条经确认的架构规则、按子系统组织的 CLAUDE.md 指南文件、多个斜杠命令技能（构建、单元测试、日志分析、PR 检查等）以及通过 PreToolUse/PostToolUse 和 git 钩子强制执行规则的机制。通过 curl 安装脚本部署到 ArduPilot 仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 条经确认的架构规则，每条可单独链接供评审引用
- 覆盖构建/测试/日志分析/PR 审查等斜杠命令技能集
- 钩子机制强制执行规则：git push 需短期授权令牌
- 支持 Claude Code、Codex、Gemini CLI 与对话式 LLM 四种用法

## 适用场景

- 用 LLM 为 ArduPilot 写代码时遵循安全可测试的开发标准
- 在 PR 评审中引用具体架构规则作为依据
- 分析飞行日志、检查 PR CI 失败原因

## 场景标签

`代码生成` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: This project provides guidance documents for using Large Language Models (LLMs) to generate and modify code for the 
> L14: The playbooks contain rules and constraints that ensure generated code is safe, testable, and consistent with ArduP

## 星数曲线

```mermaid
xychart-beta
    title "fossuav/aap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7e3dfcb6f925` · [字段定义](../../DATASET.md)*
