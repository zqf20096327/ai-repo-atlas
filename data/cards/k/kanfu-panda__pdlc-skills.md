# kanfu-panda/pdlc-skills

⭐ 18 · Shell · MIT · 推送 2026-10-13 · [GitHub](https://github.com/kanfu-panda/pdlc-skills) · [官网](https://kanfu-panda.github.io/pdlc/) · 个人维护 · 中文 README

**给 AI 编程代理的 PDLC 流程技能插件：以退出码驱动各阶段验收**

面向 Claude Code 的插件（亦作为 Agent Skills 标准技能集一键装入 Codex、Copilot、Cursor、Gemini CLI 等工具），提供 PRD→设计→TDD→实现→评审→发布→部署→复盘的分阶段产品开发工作流。核心机制是仓库内可审计的磁盘状态机：每阶段产物落盘到 docs/、更新特性状态文件，检查结果由脚本从真实命令退出码产生而非模型自报；阶段只能经 pdlc-advance.sh 推进，红测试先行，自动修复至多一次。Claude Code 集成 38 个斜杠命令，其他工具装 36 个技能，行为评测在发布前对真实模型运行。限制：结构较重，部分平台仅验证'可加载'未过状态完整性门。

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

- 检查结果由脚本从真实命令退出码产生，非模型自报
- 阶段推进仅经 pdlc-advance.sh，红测试先行、自动修复至多一次
- Claude Code 提供 38 个斜杠命令 + 状态栏 + 插件内自主循环引擎
- 同一状态机跨工具可迁移，npx skills add 一键装入其他 Agent Skills 工具

## 适用场景

- 让 AI 编程代理按 TDD 与评审流程交付功能并留下可 git diff 的产物
- 无人值守地循环驱动 tdd→implement→review 至收敛
- 团队跨不同 AI 编码工具共享同一套 PDLC 状态

## 场景标签

`工作流自动化` `编码 Agent` · 领域:效率与自动化

## 证据(README 行号)

> L16: **pdlc-skills** is built on one rule: **an AI saying "done" doesn't count — exit codes do.** It's a set of skills —
> L23: - **Portable** — the state machine lives in your repo, so it's tool-agnostic. **Claude Code** has the richest integ
> L184: Because every stage writes **objective checks** — real `unit` / `lint` / `coverage` exit codes from `docs/00_stand

## 星数曲线

```mermaid
xychart-beta
    title "kanfu-panda/pdlc-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2fc3d952347a` · [字段定义](../../DATASET.md)*
