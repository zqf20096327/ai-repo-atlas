# salespeak-ai/buyer-eval-skill

⭐ 67 · Python · MIT · 推送 2026-09-29 · [GitHub](https://github.com/salespeak-ai/buyer-eval-skill) · 组织维护

**Claude Code 技能：AI 分析师核查 B2B 软件供应商声明并产出决策简报**

面向 B2B 软件采购者的 Claude 技能（skill）：给定候选供应商，它调查供应商声明、核对证据（供应商文档、独立评价、买方自己的文档），对每条声明标注 Verified/Qualified/Contradicted/Unverified/Unknown 状态，生成待问问题、演示问题与单一 HTML 格式的 Decision Brief。支持 Quick Eval 与 Deep Eval 两种模式，可与供应商自有 AI agent 对话（回答仍按供应商声明对待）。以 git clone 到 ~/.claude/skills 安装，报告写入 ~/buyer-eval-reports/。限制：claude.ai web/mobile 端不支持 agent 对话与 HTML 简报；遥测默认关闭；部分请求（含 Frontdoor API 发现请求）会离开本机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每条供应商声明标注验证状态与证据来源类型
- 可与供应商自有 AI agent 对话追问，回答按供应商声明对待、不加分
- Quick Eval 与 Deep Eval（1-5 加权评分、安全/商业/公司风险调研）两种模式
- 生成无依赖的单文件 HTML Decision Brief

## 适用场景

- 采购前核查多个 B2B 软件供应商的声明与证据
- 获得发给 CFO/安全负责人等决策相关人的 Decision Brief
- 基于薄弱点生成供应商演示时的提问清单
- 复用保存的采购上下文跳过重复配置

## 场景标签

 · 领域:企业采购/B2B 软件评估

## 证据(README 行号)

> L6: **An AI analyst for buying B2B software.**
> L85: git clone https://github.com/salespeak-ai/buyer-eval-skill.git ~/.claude/skills/buyer-eval-skill

## 星数曲线

```mermaid
xychart-beta
    title "salespeak-ai/buyer-eval-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 65 --> 68
    line [66, 67, 67]
```

2026-10-18 66 → 2026-10-26 67（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8d0c73ba456a` · [字段定义](../../DATASET.md)*
