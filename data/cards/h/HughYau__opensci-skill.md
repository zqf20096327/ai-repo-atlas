# HughYau/opensci-skill

⭐ 14 · Python · 推送 2026-02-25 · [GitHub](https://github.com/HughYau/opensci-skill) · 个人维护 · 中文 README

**教 AI Agent 为科学 Python 库生成 SKILL.md 知识文件的元技能**

面向 Agent 的元技能（Meta-Skill）：不绑定特定科学库，而是指导 Agent 为任意科学 Python 库自动生成结构化 Skill 知识文件。流程包括爬取官方文档、提取模块结构与公开 API 签名、构建符号索引、按功能域组织参考文件并输出标准化 SKILL.md。提供 Light/Medium/Heavy 三种深度模式与 Workflow/Dictionary/Hybrid 三种覆盖度档案，附带 6 个辅助脚本。产出可被支持 skill loader 的 Agent 框架（如 Claude Code、OpenCode）加载。使用方式为将仓库目录挂载到 Agent 工作区并触发关键词。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从库的安装包/源码提取 API，签名与版本绑定
- Light/Medium/Heavy 三种深度模式与三种覆盖度档案
- 标准化的 SKILL.md 产物契约与 symbol-index.jsonl 符号索引
- 附 6 个辅助脚本（爬文档、提取 API、验证代码片段等）

## 适用场景

- 为 MNE、scanpy、PyMC 等科学库生成可复用的 Agent 技能文件
- 让 Agent 掌握频繁升级的科学库的最新 API 签名
- 为社区贡献可复用的科学库 Skill 仓库

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3:  一个为 AI Agent 构建科学 Python 库技能的元技能（Meta-Skill）
> L12: **OpenSci Skill** 是一个元技能（Meta-Skill）：它不面向某一个具体的科学库，而是教会 AI Agent **如何为任意一个科学 Python 库生成高质量的、可复用的 Skill 知识文件**。
> L21: 产出的 Skill 可被支持外部知识注入或 skill loader 的 Agent 框架加载（例如Claude Code，OpenCode等），实现对特定领域库的**精准、可更新、可复用**的调用能力。

## 星数曲线

```mermaid
xychart-beta
    title "HughYau/opensci-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `387487de478a` · [字段定义](../../DATASET.md)*
