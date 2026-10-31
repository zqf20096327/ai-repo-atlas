# promptmechanic/ai-toolbox

⭐ 14 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/promptmechanic/ai-toolbox) · 个人维护

**可即插即用的 Claude Code 技能合集：周回顾、简历审查等**

由 promptmechanic 维护的开源 Claude Code 技能仓库：每个技能是自包含文件夹（SKILL.md 及辅助脚本），放入 ~/.claude/skills/ 或项目 .claude/skills/ 后由 Claude Code 自动发现并以斜杠命令调用。收录三个技能：week-in-review 挖掘近 7 天 Claude Code 会话生成 HTML 回顾报告；resume-review 按 ATS 规则与目标职位关键词做评分式简历审查；humanize-text 改写 AI 腔文本并附带标准库扫描脚本。需 Python 3（仅标准库）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md + 辅助脚本的自包含技能，Claude Code 自动发现为斜杠命令
- week-in-review：从近 7 天会话转录生成含进一步阅读链接的 HTML 报告
- resume-review：按 ATS 解析规则与目标 JD 关键词的评分式审查
- humanize-text 附带定位机械痕迹行号的标准库扫描器

## 适用场景

- 在 Claude Code 中以斜杠命令复用周回顾、简历审查等工作流
- 把技能提交到仓库随项目携带，团队共享统一的 agent 工作流
- 参考 SKILL.md 结构编写自己的技能

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Open-source Claude Code skills — packaged, reusable agent workflows you can drop into any project. Each skill is a s
> L9: A skill is a Markdown file (`SKILL.md`) with YAML frontmatter — a `name` and a `description` that tells the agent *w

## 星数曲线

```mermaid
xychart-beta
    title "promptmechanic/ai-toolbox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `0e3ff2819cae` · [字段定义](../../DATASET.md)*
