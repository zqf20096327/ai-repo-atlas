# langfuse/experiment-action

⭐ 16 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/langfuse/experiment-action) · 组织维护

**在 GitHub Actions 中运行 Langfuse 实验的 CI 组件**

Langfuse 官方维护的 GitHub Action：在 CI 流水线中加载用户的实验脚本（Python 或 TS/JS），针对 Langfuse 数据集运行，将结果以 PR 评论形式回贴，并可在检测到 RegressionError 或脚本错误时使 CI 任务失败。实验脚本需定义 experiment() 函数，通过注入的 RunnerContext 读取数据集等默认值；每次运行附带 langfuse.* 命名空间的 Git 与工作流元数据。支持并行 matrix 共享同一条 PR 评论，fork PR 因平台限制无法评论。

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

- 针对 Langfuse 数据集运行 Python/TS 实验脚本并回贴 PR 评论
- 检测到回归（RegressionError）或脚本错误时可令 CI 失败
- 自动附带 langfuse.git_sha、branch、pr_url 等运行元数据
- 支持混合 .py 与 .ts/.js 脚本目录与并行 matrix 任务

## 适用场景

- 在 PR 中自动运行 LLM 评测实验并查看结果评论
- 评测分数回归时阻断 CI 合并
- 将实验结果与 Git 提交、工作流运行关联追溯

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: Run a Langfuse experiment in your CI pipeline. The
> L63: Your experiment script must define a function named `experiment`. The action

## 星数曲线

```mermaid
xychart-beta
    title "langfuse/experiment-action 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `1262b08e5057` · [字段定义](../../DATASET.md)*
