# SantanderAI/ralph-vault-skill

⭐ 70 · Python · Apache-2.0 · 推送 2026-10-01 · [GitHub](https://github.com/SantanderAI/ralph-vault-skill) · [官网](https://github.com/SantanderAI) · 组织维护

**为代码仓库生成分层知识库（deepwiki）的 agent 技能与 CLI**

Santander AI Lab 开源的 Python CLI/技能：为单个或多个代码仓库创建并维护分层渐进披露的知识库（tiered vault），包含 index、repos、components、relations 等层级，作为 ralph 式 LLM agent 循环的知识源。确定性部分由 scripts/gv.py 承担（无第三方依赖），内容生成由固定提示词驱动 agent 完成；支持 init/add/update/plan/validate 等动作，可安装为 Claude/Codex/Gemini 技能，也可直接运行 CLI。Apache 2.0 许可，非 Banco Santander 官方产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分层知识库结构（index/repos/components/relations/dependencies 等）
- 确定性 CLI（仅标准库）+ 固定提示词的 agent 生成分工
- 生成 plan/plan.md 供 ralph 循环或任意 agent 逐仓库执行
- validate 提供 frontmatter/wikilink/token 预算与无源码检查

## 适用场景

- 让 Claude/Codex/Gemini agent 用自然语言为仓库建知识库文档
- 为多仓库项目维护交叉引用与技术依赖图谱
- 规划并执行知识库增量更新与过期检查

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L3: > **Open source by Santander AI Lab.** A Python **CLI tool / library** to create and maintain a
> L17: A skill + CLI to **create and maintain a progressive-disclosure knowledge vault** (a tiered "deepwiki") for one or 
> L42: The way to use this is **as a skill**. Install it (see below), then just talk to

## 星数曲线

```mermaid
xychart-beta
    title "SantanderAI/ralph-vault-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-25 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0d81a74055e4` · [字段定义](../../DATASET.md)*
