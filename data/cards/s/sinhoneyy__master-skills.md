# sinhoneyy/master-skills

⭐ 15 · Python · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/sinhoneyy/master-skills) · [官网](https://master-skills-website.vercel.app) · 个人维护

**面向 Claude/Codex/Cursor 等 agent 的统一技能目录（2,658 条，15 域）**

AI agent 技能（SKILL.md 格式）聚合目录：收录 2,658 个去重技能，按 integrations、backend、prompt-engineering 等 15 个域组织，以单一机器可读清单 skills_index.json 索引，每个技能含稳定 id、版本、域与斜杠触发词。技能运行时无关，可被 Claude Code、Cursor、Codex CLI、Antigravity 等加载 SKILL.md 的宿主使用。通过 npx 命令按宿主安装到指定路径，也可作为插件装至各平台，支持按域与风险等级过滤；克隆后无需构建与网络即可用。目录工具 MIT 许可，捆绑技能保留各自上游条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2,658 个去重技能按 15 个规范化域组织
- 单一清单 skills_index.json 提供稳定 id/版本/触发词索引
- npx 一条命令安装到 10 种宿主工具的默认路径
- 支持按 category 与 risk 过滤及 dry-run 预览

## 适用场景

- 为 Claude Code/Cursor/Codex 等 agent 查找并安装技能
- 按角色主题包（安全、前端、DevOps 等）批量安装技能
- 通过 grep 或程序化读取清单检索技能

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L28: Master Skills is a standardized catalog of **2,658 AI-agent skills**, sorted into
> L29: **15 normalized domains**. Every skill is **runtime-agnostic** — it works with **Claude,

## 星数曲线

```mermaid
xychart-beta
    title "sinhoneyy/master-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2742ea1883cc` · [字段定义](../../DATASET.md)*
