# leochiu-a/universal-agents

⭐ 60 · TypeScript · MIT · 推送 2025-12-05 · [GitHub](https://github.com/leochiu-a/universal-agents) · [官网](https://leochiu-a.github.io/universal-agents/) · 个人维护

**跨 AI 编程助手的共享配置标准与脚手架 CLI**

定义以单一 AGENTS.md 为入口、.agents/ 目录存放技能与规则的共享标准，供 Claude Code、Cursor、Codex 等不同 AI 编程助手统一读取项目规则与工作流，避免配置锁定在单一平台。提供 npx CLI 生成 AGENTS.md、脚手架生成 skill 与 rule 文件；并给出在 Claude Code 中通过 /memory 固化读取提示的适配方法，因 Claude Code 不原生支持 AGENTS.md 协议。标准本身为 Markdown，无 DSL 或专用配置格式。

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

- AGENTS.md + .agents/ 目录的单一清单共享标准
- npx CLI 支持 init、创建 skill 与 rule 脚手架
- 声明跨 Claude Code、Cursor、Codex 及未来助手可用
- 四步执行协议：发现→按需加载→强制规则→声明已应用的护栏

## 适用场景

- 团队在多个 AI 编程助手间共享同一套项目规则与技能
- 为新项目快速生成 AGENTS.md 与技能/规则骨架
- 统一 Cursor 风格 rules 与 Claude 风格 skills 的管理方式

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A lightweight standard for sharing agent configurations across all AI coding assistants using a single `AGENTS.md` f
> L36: Universal Agents provides the **lightest, simplest** shared standard: `AGENTS.md` + `.agents/` folder. Any agent—re

## 星数曲线

```mermaid
xychart-beta
    title "leochiu-a/universal-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-24 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `31e5d74414e0` · [字段定义](../../DATASET.md)*
