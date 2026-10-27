# AdamBien/airails

⭐ 59 · MIT · 推送 2026-10-26 · [GitHub](https://github.com/AdamBien/airails) · [官网](https://airails.dev) · 个人维护

**面向 AI 编程 agent 的 Java/Web 开发规范与技能集（SKILLS.md/AGENTS.md）**

由 Adam Bien 维护的 Spec-Driven BCE 规范仓库，提供一套可安装到 Claude、Copilot、Kiro、Goose 等 agent 技能目录的 SKILLS.md 约定，覆盖 Java 25 CLI、MicroProfile 服务端、AWS CDK、无依赖静态 Web 开发及遗留系统迁移。技能按六层（语言/语义/架构/技术/习语/判断）组合，每个技能固定一组决策。安装方式为运行 installSkills 脚本（需 JDK 25 交互式终端）或下载预打包 zip 解压。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 技能分六层组合，每层固定一组开发决策
- 支持安装到 claude/vibe/kiro/copilot/codex/goose/agents 等技能目录
- 覆盖 Java 25 CLI、MicroProfile、AWS CDK、静态 Web 与遗留系统迁移
- 提供预打包 zip，无 JDK/git 也可安装

## 适用场景

- 为我的 AI 编程 agent 注入 Java/Web 项目开发规范
- 按 Spec-Driven BCE 流程将功能拆解为能力规格并收敛代码
- 将遗留企业 Java/Web 系统迁移到现代技术栈

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Home of Spec-Driven BCE (**sbce.space**) — development conventions, SKILLS.md, and AGENTS.md for building modern Jav
> L23: The installer finds all skills and prompts before copying to each supported agent directory (`~/.claude/skills`, `~

## 星数曲线

```mermaid
xychart-beta
    title "AdamBien/airails 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 57 --> 60
    line [58, 59, 59]
```

2026-10-18 58 → 2026-10-27 59（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `19c59d477977` · [字段定义](../../DATASET.md)*
