# SomeStay07/code-review-agent

⭐ 29 · MIT · 推送 2026-02-12 · [GitHub](https://github.com/SomeStay07/code-review-agent) · [官网](https://t.me/codeonvibes) · 个人维护

**给 Claude Code 用的代码审查 agent：单 .md 文件，输出具体修复**

一个放入 .claude/agents/ 目录的 Markdown 指令文件，使 Claude Code 具备 TypeScript 与 React 项目的代码审查行为：14 个审查类别（含 OWASP Top 10 安全检查）、4 级严重度加置信度标注、每条发现给出 file:line 与 before→after 修复代码，并提供 A/B/C/D 自动修复选项。含 14 条误报抑制规则、8 条重构启发式、跨会话持久记忆（学习项目约定）。零依赖零配置，通过 curl 下载单个文件安装，要求支持 agent 功能的 Claude Code，默认运行在 sonnet 模型上。

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

- 14 个审查类别、4 级严重度与置信度标注，每条发现给出 file:line 具体修复
- OWASP Top 10 安全检查与误报抑制规则
- 跨会话持久记忆：学习项目编码约定与已知误报
- 自动检测用户语言并以该语言输出审查报告

## 适用场景

- 在 Claude Code 中对 TypeScript/React 的 diff 做提交前审查
- PR 审查时获取带 file:line 和具体修复代码的安全与质量发现
- 让 agent 记住团队约定并按约定持续执行审查

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L30: **Code Reviewer Agent** is a single `.md` file that turns Claude Code into an expert code reviewer. Drop it into `.
> L32: > **What's a Claude Code agent?** An agent is a `.md` file in `.claude/agents/` that gives Claude Code specialized 

## 星数曲线

```mermaid
xychart-beta
    title "SomeStay07/code-review-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `77f6071165a9` · [字段定义](../../DATASET.md)*
