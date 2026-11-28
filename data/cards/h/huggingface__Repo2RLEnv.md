# huggingface/Repo2RLEnv

⭐ 813 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/huggingface/Repo2RLEnv) · [官网](https://huggingface.github.io/Repo2RLEnv/) · 组织维护

**把代码仓库转成可训练可评测的 RL 环境任务**

Repo2RLEnv 将仓库、PR、agent 轨迹和任务种子转换为 Harbor 格式任务，每个任务包含 instruction、起始环境、verifier 与参考解；生成后经审查与校验器探测，任务带 unverified/verified/needs_repair/blocked 标签。内置 pr_diff、pr_runtime、Tasksmith 等多条流水线及 16 种研究配方。代码执行依赖本地 Docker 或 Modal/Daytona 工作节点，PR-diff 评分需模型裁判与 API key。以 PyPI 包发布，任务数据集可发布到 Hugging Face Hub。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 PR/轨迹/种子生成含 instruction、环境、verifier 与参考解的 Harbor 任务
- Tasksmith 用 LangGraph 驱动 agent 自动设计任务与校验器
- 内置 SWE-smith、R2E-Gym 等 16 种研究配方流水线
- 任务带统一质量标签，配套 FineEnvs 数据集集合

## 适用场景

- 为 coding agent 构建可训练的 RL 训练环境
- 从合并的 PR 或 agent 轨迹批量生成评测任务
- 在 Hugging Face Hub 上发布和分享任务数据集

## 场景标签

`模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L21: Repo2RLEnv turns repositories, pull requests, agent trajectories and task seeds into
> L24: Repo2RLEnv generates and reviews the tasks; Harbor runs agents against them.

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/Repo2RLEnv 星数(近 21 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-15", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-28"]
    y-axis "stars" 732 --> 820
    line [742, 743, 753, 755, 757, 758, 759, 762, 739, 779, 782, 786, 788, 790, 796, 798, 804, 806, 808, 812, 813]
```

2026-10-26 742 → 2026-11-28 813（+71）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `0bfdc5fbb4c6` · [字段定义](../../DATASET.md)*
