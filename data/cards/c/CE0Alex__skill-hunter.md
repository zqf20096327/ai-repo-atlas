# CE0Alex/skill-hunter

⭐ 21 · MIT · 推送 2026-02-06 · [GitHub](https://github.com/CE0Alex/skill-hunter) · 个人维护

**分析代码仓库并推荐适配外部 agent 技能栈的技能**

遵循 Agent Skills 格式的 agent 技能：扫描用户项目代码库理解技术栈与约束，询问目标与信任偏好后，从 Context7、skills.sh 与 GitHub 检索技能，核验来源与维护者，给出带置信度的最小技能集推荐，确认后经 Skills CLI 等方式安装。兼容 50+ agent（实测 Claude Code 2.1.34、Codex CLI 0.98.0、Claude Web/Desktop）。仅用于发现新技能，不回答已装技能的用法问题。

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

- 扫描项目代码库后按目标与偏好检索技能注册表
- 核验候选技能的来源、维护者与兼容性
- 给出带置信度与权衡说明的最小技能栈推荐
- 兼容 50+ agent，含 Claude Code/Codex CLI 实测记录

## 适用场景

- 让 agent 为我的项目挑选并安装合适的外部技能
- 发现 TypeScript 测试、CI/CD 等特定方向可用的技能
- 在多个 agent 环境间复用同一技能发现流程

## 场景标签

 · 领域:开发者工具/Agent 技能生态

## 证据(README 行号)

> L5: An agent skill that analyzes your project and recommends a curated stack of **external skills** from trusted registr
> L31: This skill follows the Agent Skills format and works with any agent that supports skills.

## 星数曲线

```mermaid
xychart-beta
    title "CE0Alex/skill-hunter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3e6a3bf548c8` · [字段定义](../../DATASET.md)*
