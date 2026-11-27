# bostonaholic/grokbot-skills

⭐ 4 · Shell · 推送 2026-11-24 · [GitHub](https://github.com/bostonaholic/grokbot-skills) · 个人维护

**面向 Grok Bot 与 Cursor agent 的可复用技能手册集**

以 SKILL.md 文件夹形式组织的 agent 技能库：每个技能是一个含 YAML frontmatter（name/description）的 markdown 指令文件，agent 可自行加载。收录约 13 个技能，覆盖例行任务审计、backlog 整理、深度研究、prompt 压缩改进、定时任务设计、写作风格等场景。提供安装脚本把技能文件夹复制到 Grok Bot 的技能库目录，支持 --dest 指定路径与重复执行更新，并在 Settings > Plugins 中确认安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每技能一个 kebab-case 文件夹，SKILL.md 内含 name/description frontmatter
- git clone + shell 脚本一键安装到 Grok Bot 技能库，支持 --dest 与原地更新
- 约 13 个技能覆盖审计、研究、prompt 优化、例行任务等场景
- 同时面向 Cursor 与 Grok Bot 两类 agent

## 适用场景

- 给 Grok Bot 安装现成的例行工作流技能
- 让 coding agent 复用现成的 prompt 编写与改进规范
- 为无人值守定时任务设计防卡死、防误触发的流程

## 场景标签

`提示工程` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L3: Skills for Cursor and Grok Bot agents. Each skill is one folder an agent can load on its own.
> L10: skills/<kebab-slug>/SKILL.md

## 星数曲线

```mermaid
xychart-beta
    title "bostonaholic/grokbot-skills 星数(近 3 点)"
    x-axis ["2026-11-21", "2026-11-22", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-21 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `3915237ef647` · [字段定义](../../DATASET.md)*
