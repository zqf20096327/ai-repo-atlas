# hanspeterdietiker/open-agent-skills

⭐ 4 · MIT · 推送 2026-11-15 · [GitHub](https://github.com/hanspeterdietiker/open-agent-skills) · 个人维护

**面向 AI agent 开发者的开源 SKILL.md 技能共享仓库**

一个社区驱动的开放仓库，收录以 SKILL.md 格式编写的 AI agent 技能包（目前 5 条：clean-code、conventional-commits、harness-loop、loop-impl、pull-request）。每条 Skill 由 YAML frontmatter（name/description）加 Markdown 指令组成，agent 按任务描述按需加载。通过 npx skills CLI 安装到 Claude Code 或 Codex、Cursor、Gemini CLI、GitHub Copilot 等其他 agent；内容以葡英双语编写，社区通过 issue/PR 审核贡献，第三方 Skill 需保留原许可与署名。

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

- 以 SKILL.md 格式（YAML frontmatter + Markdown 指令）组织技能包
- npx skills CLI 一键安装到 Claude Code 及多种 agent
- 葡英双语内容，面向巴西及全球社区
- 第三方 Skill 保留原始许可与署名（license/metadata 字段）

## 适用场景

- 为 Claude Code 等 agent 添加提交规范、代码审查类技能
- 发布并分享自己编写的 agent 技能供他人复用
- 学习 prompt engineering 与 context engineering 的教学材料

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L36: Este repositório é um **acervo aberto de Skills**, construído pela e para a comunidade de IA, com quatro pilares:
> L47: - **Descobrir** — reunir em um só lugar Skills úteis, testadas e bem explicadas.
> L105: ### Com o Claude Code
> L132: O formato `SKILL.md` é simples e baseado em Markdown, portanto também pode ser adaptado para outros agentes e fram

## 星数曲线

```mermaid
xychart-beta
    title "hanspeterdietiker/open-agent-skills 星数(近 3 点)"
    x-axis ["2026-11-14", "2026-11-15", "2026-11-28"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-14 3 → 2026-11-28 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `3d3a103e535b` · [字段定义](../../DATASET.md)*
