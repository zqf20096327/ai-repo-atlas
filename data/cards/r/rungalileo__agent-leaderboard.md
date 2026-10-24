# rungalileo/agent-leaderboard

⭐ 226 · Jupyter Notebook · MIT · 推送 2026-05-21 · [GitHub](https://github.com/rungalileo/agent-leaderboard) · [官网](https://huggingface.co/spaces/galileo-ai/agent-leaderboard) · 组织维护

**评测 AI agent 在企业场景任务完成与工具调用表现的排行榜框架**

Galileo 维护的 agent 评测框架与公开排行榜：v1 基于 BFCL、τ-bench、xLAM、ToolACE 等数据集评测评工具选择质量（TSQ）；v2 增加合成数据集生成与用户对话模拟引擎，在银行、医疗、投资、电信、保险五个行业各构造 100 个含 5-8 个关联目标的多轮对话场景，度量 Action Completion（AC）与 TSQ 指标。面向模型开发者、企业团队、研究者在部署前验证 agent 表现。README 未给出本产品的安装运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- v2 提供合成场景生成与 agent-用户多轮对话模拟引擎
- 覆盖 5 个行业各 100 个含 5-8 个关联目标的场景
- AC（任务完成）与 TSQ（工具选择质量）两项指标
- v1 基于 4 个公开数据集评测 17+ 模型，含 Hugging Face Spaces 实时榜单

## 适用场景

- 在上线前验证 agent 在特定业务领域的任务完成能力
- 对比各模型在不同行业的工具调用表现
- 研究者研究工具调用能力与 agent 行为

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: An evaluation framework for AI agents across real-world business scenarios.
> L14: - **v2**: Enhanced framework with synthetic dataset generation and a simulation engine for evaluating task completi
> L100: Evaluates language models using standardized benchmarks and the Tool Selection Quality (TSQ) metric.

## 星数曲线

```mermaid
xychart-beta
    title "rungalileo/agent-leaderboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 225 --> 227
    line [226, 226]
```

2026-10-18 226 → 2026-10-24 226（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `10f9f71c9ea0` · [字段定义](../../DATASET.md)*
