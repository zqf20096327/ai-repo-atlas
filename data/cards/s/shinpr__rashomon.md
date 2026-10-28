# shinpr/rashomon

⭐ 19 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/shinpr/rashomon) · 个人维护 · 中文 README

**给 agent 开发者：盲评 A/B 对比检验 skill 与 prompt 改动是否有效**

Rashomon 是一个 Claude Code 插件（Codex 侧仅含 prompt-optimization），用于在发布前检验 skill 或 prompt 改动是否真正改善 agent 行为。机制：分析改动、在独立 Git worktree 中隔离执行同一任务的两个版本、重复配对试验、盲评（评判者先看输出后知版本），最终输出 ship/revise/reject 或 Use optimized 等建议，并将差异分为 Structural/Context Addition/Expressive/Variance 四类。依赖 Claude Code、Git 2.5+ 与 Python 3.9+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一任务在 baseline 与改动版本间做盲评 A/B 配对试验
- skill 评估输出 ship/revise/reject 建议，prompt 评估输出四种结论
- 差异四分类：Structural/Context Addition/Expressive/Variance
- 每个版本在独立 Git worktree 中从同一仓库状态执行

## 适用场景

- 发布前验证新 skill 是否比无 skill 更好
- 对比 prompt 优化版与原版的执行质量
- 判断改写是真实改进还是正常模型波动

## 场景标签

`模型评测` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L14: Rashomon tests that possibility. It runs the same task under a baseline and a changed version, then compares the re
> L71: 4. **Compare blind.** The evaluator judges output quality before learning which result came from which version.

## 星数曲线

```mermaid
xychart-beta
    title "shinpr/rashomon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7d5baac2f006` · [字段定义](../../DATASET.md)*
