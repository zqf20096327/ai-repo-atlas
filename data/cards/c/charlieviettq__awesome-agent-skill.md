# charlieviettq/awesome-agent-skill

⭐ 26 · Python · MIT · 推送 2026-07-20 · [GitHub](https://github.com/charlieviettq/awesome-agent-skill) · [官网](https://charlieviettq.github.io/awesome-agent-skill/) · 个人维护

**面向 AI 编程 agent 的可复用技能库与技能市场（598 个 SKILL.md）**

一个策展式开源技能库，收录 598 个可移植的 SKILL.md 格式 playbook，覆盖规划、TDD、代码审查、QA、安全、数据分析、文档处理与浏览器自动化等领域，供 Cursor、Claude Code、Codex CLI、OpenCode、Gemini CLI 等 SKILL.md 兼容的编程 agent 安装使用。Cursor 目录为源，Claude Code 目录由脚本生成并支持双向转换与一致性校验；提供 skillhub CLI（pip 安装）按 bundle 安装技能，静态技能市场站点部署于 GitHub Pages，含任务推荐与 bundle 关系图。

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

- 598 个可移植 SKILL.md 技能，兼容 Cursor/Claude Code/Codex/OpenCode/Gemini CLI
- skillhub CLI 支持 bundle 推荐、--dry-run 预览与按格式安装
- Cursor↔Claude Code 双向转换脚本与技能一致性校验
- 静态技能市场站点（任务推荐、bundle 图谱、在线预览）

## 适用场景

- 给编程 agent 装上规划、审查、QA、安全等可复用工作流程
- 按数据科学、AI 工程、金融、法务等领域选择 persona bundle
- 在团队项目中只复制需要的技能域

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L16: **Open Skill Marketplace** — search 598 skills, preview `SKILL.md` inline, explore the bundle graph, copy install c
> L26: |Multi-agent compatibility|Works with Cursor, Claude Code, Codex, OpenCode, Gemini CLI, and other `SKILL.md`-aware 
> L67: |Cursor|`.cursor/skills/`|Source of truth in this repo|

## 星数曲线

```mermaid
xychart-beta
    title "charlieviettq/awesome-agent-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `18b0dd98e850` · [字段定义](../../DATASET.md)*
