# Merlon-Docs/merlon

⭐ 19 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/Merlon-Docs/merlon) · [官网](https://merlon-docs.github.io/merlon/) · 组织维护

**面向软件项目的文档系统 Agent Skill：分片存储+CI 校验**

以 Agent Skill 加 CLI 工具链形式交付的文档系统：将架构说明、规格、ADR 等存储为 git 仓库内的小型 Markdown 分片（shards），Agent Skill 指示 agent 一次读取一个分片并在改动所描述内容前先更新分片；`merlon compile` 可将分片编译为单文件指南或 README，`merlon check` 在 CI 中校验孤儿分片、内部链接与编译输出，但不校验内容真实性（由人与 agent 在评审中负责）。面向长期维护软件项目的团队与 agent，通过 skills.sh 安装并在 AGENTS.md 中引用。不替代 Docusaurus/MkDocs 这类纯站点生成器。

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

- 小型 Markdown 分片与源码同仓存储，agent 逐片读取
- `merlon check` 在 CI 中校验孤儿分片、链接与编译输出
- `merlon compile` 可编译为 README、单文件指南或供站点生成器使用
- 通过 npx skills 安装，经 AGENTS.md/CLAUDE.md 接入为项目规范

## 适用场景

- 长期维护的软件项目中让人与 agent 共同维护规格、ADR 与 runbook
- 在 CI 中拦截未更新文档或链接失效的改动
- 将分片文档编译为可评审的单文件指南或 README

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L7: **Merlon Docs** is a **documentation system** delivered as an Agent Skill plus a small compile/check toolchain. It i
> L11: Instead of putting every architecture note and spec into one file, Merlon Docs stores that intent as small, validat
> L85: - **[Agent Skill](https://agentskills.io)** ([definition](docs/glossary/agent-skills.md)): instructions your agent 

## 星数曲线

```mermaid
xychart-beta
    title "Merlon-Docs/merlon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `32b36c5d0516` · [字段定义](../../DATASET.md)*
