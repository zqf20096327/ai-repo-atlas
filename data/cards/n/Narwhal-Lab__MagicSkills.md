# Narwhal-Lab/MagicSkills

⭐ 317 · Python · MIT · 推送 2026-04-08 · [GitHub](https://github.com/Narwhal-Lab/MagicSkills) · 组织维护 · 中文 README

**跨 agent 复用 SKILL.md 技能的本地共享技能池基础设施**

面向多 agent 项目的本地优先（local-first）技能管理层：将分散的 SKILL.md 目录安装进一个共享技能池，解析 frontmatter 构建 Skill 对象，再按 agent 组合成命名的 Skills 集合，通过 REGISTRY 持久化。集合可同步写入 AGENTS.md（供 Claude Code、Cursor、Windsurf、Aider、Codex 等读取），或经统一 CLI 工具接口与 Python API（配合 LangChain、AutoGen、CrewAI 等框架）以工具/函数形式暴露。由北京大学 Narwhal-Lab 发起维护，需 Python 3.10-3.13。

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

- install/addskills/syncskills/skill-tool 四步工作流管理技能
- 技能集合可同步 AGENTS.md 或以 CLI/Python 工具接口暴露
- 支持从 Git 仓库或本地目录安装技能到共享池
- 三层核心模型：Skill / Skills / REGISTRY 全局注册表

## 适用场景

- 多个 agent 复用同一技能库，避免技能目录反复复制漂移
- 把技能子集同步进各 agent 的 AGENTS.md
- 为通过工具/函数集成的 agent 框架暴露同一技能集合

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Local-first** skill infrastructure for multi-agent projects
> L40: MagicSkills is a local-first skill infrastructure layer for multi-agent projects.
> L218: MagicSkills provides integration examples for both agent / IDE products that can directly read `AGENTS.md` and mai

## 星数曲线

```mermaid
xychart-beta
    title "Narwhal-Lab/MagicSkills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 315 --> 318
    line [316, 317, 317]
```

2026-10-18 316 → 2026-10-27 317（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0bf5a1955df0` · [字段定义](../../DATASET.md)*
