# off-grid-ai/skills

⭐ 175 · HTML · MIT · 推送 2026-11-17 · [GitHub](https://github.com/off-grid-ai/skills) · [官网](https://getoffgridai.co/download) · 个人维护

**给编码 agent 的 49 个免费技能包，覆盖构建、测试与交付流程**

面向 Claude Code、Codex、Cursor 等 60+ 编码 agent 的技能集合：每个技能是一个含 SKILL.md 的文件夹，agent 在请求匹配时读取其中的操作手册。49 个技能按评审、回归测试、遗留代码改造、UI 设计标准、CTO 决策、发布、增长、收入分析和游戏开发等 9 组组织，涵盖变更影响映射、真实界面测试、设计规范检查等。MIT 许可，可通过 npx、Claude Code/Codex 插件市场或 curl 脚本安装，技能之间互相引用需整套安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 49 个技能分为 9 组，每个技能是一个 agent 读取的 SKILL.md 文件夹
- 支持 Claude Code、Codex、Cursor 及 60+ 其他 agent
- graph-engineering 在一页内展示变更前后所有受影响界面
- MIT 许可，提供 npx / 插件市场 / install.sh 三种安装方式

## 适用场景

- 让编码 agent 在提交前测试变更并检查设计
- 在遗留代码库上先映射影响范围再动手改
- 为独立开发流程补齐评审、测试与发布环节的 agent 能力

## 场景标签

`代码审查` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L13: Each skill is a short playbook your agent reads before it starts, so it tests every change in your real app and che
> L81: ## All 49 skills
> L221: - Each skill is a folder with a `SKILL.md`, plain Markdown your agent reads when your request matches it. Nothing 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `e5cd57521758` · [字段定义](../../DATASET.md)*
