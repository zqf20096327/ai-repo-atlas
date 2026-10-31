# param087/agent-ml-skills

⭐ 13 · JavaScript · MIT · 推送 2026-06-06 · [GitHub](https://github.com/param087/agent-ml-skills) · 个人维护

**给 AI 编程 agent 的 15 条 ML/MLOps 技能包，一条 npx 命令安装**

面向 Codex、Claude Code、Cursor、OpenCode 等编码 agent 的技能包：每个技能是带 YAML frontmatter 的单个 Markdown 文件，声明适用时机与操作方法，agent 在任务匹配时自动加载。15 个技能覆盖数据准备、建模评估、LLM 微调与 RAG、MLOps 可靠性四类，强调防数据泄漏、可复现与具体代码模式。安装器为纯 Node 零依赖，通过 npx 命令按目标 agent 与范围安装到对应 skills 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个技能，覆盖数据准备/建模/LLM 与 RAG/MLOps 四类
- 技能为 Markdown+YAML frontmatter，agent 按任务匹配自动加载
- 纯 Node 零依赖安装器，npx 一条命令安装到 Codex/Claude Code/Cursor/OpenCode
- 技能间可组合传递（EDA→清洗→特征→管道→评估→服务）

## 适用场景

- 让编码 agent 写 ML 代码时遵循防泄漏、正确评估等工程规范
- 为 RAG 或 LLM 微调任务注入对应技能指引
- 在多个 agent 平台间复用同一套 ML 技能

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L11: Coding agents are great generalists but make the same **ML mistakes over and over**: leaking preprocessing into cro
> L36: A skill is a single Markdown file with YAML frontmatter telling the agent **when** to use it and **how** to do the 
> L45: Agents that support skills load the `description` up front and pull in the full body only when the task matches — s

## 星数曲线

```mermaid
xychart-beta
    title "param087/agent-ml-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5860cb3b62eb` · [字段定义](../../DATASET.md)*
