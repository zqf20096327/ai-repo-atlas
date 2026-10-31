# wonsukchoi/domain-experts

⭐ 23 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/wonsukchoi/domain-experts) · [官网](https://domainexperts.dev/) · 个人维护

**956 个职业专家角色定义库，供 AI agent 按需加载**

开源的职业角色定义库：将从业者心智模型、决策阈值、失败模式结构化为 SKILL.md 格式（当前 956 个角色，927 个映射到 O*NET 职业分类，覆盖 91.2%），任何 AI agent 可加载某个角色并按该专家方式推理。角色通过多遍撰写流水线（来源溯源、对抗性评审、9 维评分、CI lint）生成，并提供可复现评测脚本。通过 npx CLI 安装角色，支持 Claude Code、Codex、Gemini CLI、Cursor 等工具的斜杠命令集成。明确声明不替代受监管职业的执照与责任。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 956 个 SKILL.md 格式角色，映射 O*NET 1,016 个职业中的 927 个
- 多遍撰写流水线：溯源、对抗性评审、9 维评分、CI lint 门禁
- 可复现评测：python3 evals/run_evals.py，反事实对比 13/15 胜
- npx CLI 按需安装角色与 router skill，支持多种 agent 工具的斜杠命令

## 适用场景

- 让编程 agent 在合同审查、财务分析等任务中加载对应专家角色
- 为 agent 工具（Claude Code/Cursor 等）安装 /domain-expert 命令按需路由角色
- 按 O*NET 职业分类查找特定领域专家推理模板

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L18: Open source library of **job role definitions** — the actual mental models, decision thresholds, and failure modes 
> L149: **956 roles drafted** (927 mapped to an O*NET occupation, 29 custom; 956 at spec 2, 0 awaiting upgrade), across 10
> L70: - **A standard, not a database.** `SKILL.md` already runs in 30+ agent tools. Being the largest library in a portab

## 星数曲线

```mermaid
xychart-beta
    title "wonsukchoi/domain-experts 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25", "2026-10-31"]
    y-axis "stars" 20 --> 24
    line [21, 22, 23, 23]
```

2026-10-18 21 → 2026-10-31 23（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `487727c522fa` · [字段定义](../../DATASET.md)*
