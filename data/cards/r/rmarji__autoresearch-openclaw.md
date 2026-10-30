# rmarji/autoresearch-openclaw

⭐ 28 · JavaScript · MIT · 推送 2026-04-01 · [GitHub](https://github.com/rmarji/autoresearch-openclaw) · [官网](https://www.npmjs.com/package/autoresearch-openclaw) · 个人维护

**用 AI agent 迭代优化带评分指标的文本文件的 CLI 工具**

受 Karpathy autoresearch 启发、为 OpenClaw 打包的 npm CLI：给定一个文件（提示词/邮件模板/配置/预测市场策略）和返回单一浮点数的指标命令，循环执行 agent 提出单点修改→测分→保留或 git 回退，直至预算耗尽，输出 results.tsv、report.md 与最佳版本。面向开发 prompt 与自动化文本资产的用户，内置 5 个技能（prompt/outreach/content/config/prediction optimizer），需 Node.js>=18、Git 及 Claude CLI 或 OpenAI API。限制：需标量指标、小文件（<10KB）效果最佳、agent 调用串行。

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

- 读文件→agent 单点修改→测分→保留/回退的自动优化循环
- Git 原子提交与回退保障可逆性
- 内置 prompt/outreach/content/config/prediction 五个优化技能
- 生成 results.tsv、report.md、hypothesis_log.jsonl 实验记录

## 适用场景

- 自动迭代系统提示词以提升评测分数
- 优化冷邮件模板的回复率
- 用基准命令调优 YAML/JSON 配置文件

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L27: 1. **Read** your current file
> L98: Optimize system prompts against evaluation scores.
> L233: - Claude CLI or OpenAI API (for the agent)

## 星数曲线

```mermaid
xychart-beta
    title "rmarji/autoresearch-openclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0923d4e86b6b` · [字段定义](../../DATASET.md)*
