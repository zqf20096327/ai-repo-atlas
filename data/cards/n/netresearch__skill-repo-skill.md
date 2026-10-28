# netresearch/skill-repo-skill

⭐ 22 · Shell · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/netresearch/skill-repo-skill) · [官网](https://netresearch.github.io/skill-repo-skill/) · 组织维护

**规范化 agent 技能仓库结构与发布流程的 Claude Code 技能**

Netresearch 维护的一个 Agent Skill（开放标准），用于统一其技能仓库的目录布局、多渠道分发（marketplace/Composer/npm/Release）、拆分式双许可与 CI 校验。提供 validate-skill.sh 结构校验脚本、可复用 GitHub Actions 工作流与仓库模板，兼容 Claude Code、Cursor、GitHub Copilot 等客户端。范围限定于 GitHub 托管的 Netresearch 风格仓库，声明为对 Anthropic skill-creator 的扩展而非替代。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定义统一的技能仓库目录结构与模板
- validate-skill.sh 校验 SKILL.md、许可、composer.json、plugin.json
- 6 种安装/分发渠道（marketplace、skills 目录、npx、Release、Composer、npm）
- 供其他仓库复用的 CI 工作流（validate.yml、release.yml）

## 适用场景

- 为新技能仓库按既定规范生成骨架与配置
- 排查 validate-skill.sh 或打包发布的校验错误
- 把技能仓库迁移到拆分式双许可结构

## 场景标签

 · 领域:AI agent 开发工具/技能规范

## 证据(README 行号)

> L13: - **Value categories:** org/project-specific knowledge (Netresearch repo shape, split licensing, composer type `ai-
> L19: This is an **Agent Skill** following the open standard originally developed by Anthropic and released for cross-pla
> L28: > Skills are portable packages of procedural knowledge that work across any AI agent supporting the Agent Skills sp

## 星数曲线

```mermaid
xychart-beta
    title "netresearch/skill-repo-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `054c1ff3a47c` · [字段定义](../../DATASET.md)*
