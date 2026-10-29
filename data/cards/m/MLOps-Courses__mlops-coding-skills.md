# MLOps-Courses/mlops-coding-skills

⭐ 23 · MIT · 推送 2026-10-19 · [GitHub](https://github.com/MLOps-Courses/mlops-coding-skills) · [官网](https://mlops-coding-course.fmind.dev/) · 组织维护

**MLOps 编码课程的配套 Agent Skills 技能集合**

由 MLOps Coding Course 派生的 7 个 Agent Skill，每个对应课程一章：初始化、原型、工业化、验证、自动化、协作、可观测性。每个 skill 是含 SKILL.md（YAML frontmatter + Markdown 指令）的文件夹，为 AI 编码助手（Antigravity、Gemini CLI、GitHub Copilot、Claude Code）提供 MLOps 方法论与规范上下文。安装方式为 clone 仓库后按各工具路径 symlink 到 .agents/skills/ 等目录，或用 gemini skills install 命令安装。

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

- 7 个 skill 对应课程 7 章（从初始化到可观测性）
- 遵循开放 SKILL.md 标准，列出 4 种 AI 编码助手的安装路径
- 支持 symlink 共享目录或 gemini skills install 安装
- 贡献流程带 mise 工具链与 frontmatter/规范校验

## 适用场景

- 为 AI 编码助手注入 MLOps 最佳实践上下文
- 跟随课程章节逐步规范 ML 项目工程化
- 让不同编码工具共享同一套技能目录

## 场景标签

`教程课程` `MLOps` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: This project contains a collection of **Agent Skills** designed to accompany the MLOps Coding Course. These skills a
> L9: Agent Skills are specialized context or instructions that you can load into your AI assistant. Each skill is a folde
> L13: Each skill derives from one chapter of the MLOps Coding Course:

## 星数曲线

```mermaid
xychart-beta
    title "MLOps-Courses/mlops-coding-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `da9a1f98dd9b` · [字段定义](../../DATASET.md)*
