# lglucas/ai-dev-operating-system

⭐ 14 · JavaScript · MIT · 推送 2026-10-02 · [GitHub](https://github.com/lglucas/ai-dev-operating-system) · [官网](https://github.com/lglucas/ai-dev-operating-system) · 个人维护 · 中文 README

**面向 SaaS 独立开发者的 Claude Code 运行层与项目向导**

围绕 AI 编码代理搭建的“操作系统”仓库：提供 .claude 运行时（28 个技能、12 个代理、11 个命令、12 条规则），核心机制是 Project Genesis Wizard 五阶段向导，从想法推进到商业计划、HTML 原型实验室、产品简报、技术计划与首个编码冲刺。包含通过钩子机械阻止密钥提交的安全门（需 Node，缺失时跳过）、1,346 项自托管目录、外部仓库注册表，以及面向非开发者的 Vibe Coder 组件包。通过 Use this template 或 git clone 使用，v0.5.2 起也可作为 Claude Code 插件安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Project Genesis Wizard 五阶段向导：想法→商业计划→原型→文档→首个冲刺
- 钩子层机械阻止密钥提交与 .env 写入，不依赖模型配合
- 1,346 项自托管项目目录与外部仓库注册表（按需推荐安装包）
- 面向非开发者的防御层与主动帮助层（成本监控、回滚、部署等）

## 适用场景

- 独立开发者用 Claude Code 从零启动一个 SaaS 项目并获得流程约束
- 非开发者借助向导生成商业计划与可点击原型再进入开发
- 在 AI 编码工作流中强制密钥安全与规范提交

## 场景标签

 · 领域:开发者工具/AI 辅助开发

## 证据(README 行号)

> L11: Clone this repo, open it in your IDE, run Claude Code in the terminal, and let the **Project Genesis Wizard** take 
> L61: - A ready-to-use `.claude/` runtime: **28 skills, 12 agents, 11 commands, 12 rules** — and **hooks that block secre
> L79: |`block-secret-commit.js`|`Bash`, `PowerShell` → any `git commit`|a diff that adds something credential-shaped, or 

## 星数曲线

```mermaid
xychart-beta
    title "lglucas/ai-dev-operating-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `d9f81c556531` · [字段定义](../../DATASET.md)*
