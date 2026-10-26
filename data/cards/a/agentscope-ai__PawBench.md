# agentscope-ai/PawBench

⭐ 121 · Python · Apache-2.0 · 推送 2026-08-03 · [GitHub](https://github.com/agentscope-ai/PawBench) · [官网](https://agentscope-ai.github.io/PawBench/) · 组织维护 · 中文 README

**评测 LLM×harness 联合性能的 agent 基准（150 任务×9 模型×3 harness）**

面向 agent AI 的模型×harness 联合评测基准：v1.0 覆盖 150 个任务（复用并规范化 claweval、qwenclawbench、pinchbench 等套件，按场景/能力/复杂度/模态/环境五维打标）、9 个模型、3 个 harness（QwenPaw/OpenClaw/Hermes），支持任务切片诊断、轨迹与工作区保存、提交聚合生成排行榜。评测通过 Python 脚本在 Docker 内运行，评分含自动化检查、LLM judge 与混合三种模式，需 Python 3.11+ 与 Docker，默认推荐 DashScope 作为模型提供方。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 150 任务 × 9 模型 × 3 harness 的联合评测矩阵与切片诊断
- 五维任务打标（场景/能力/复杂度/模态/环境）与三种评分模式
- 支持保存 agent 工作区与 Docker 镜像以便回放
- 配套网站提供 Model×Harness 矩阵、切片分析与任务库

## 适用场景

- 选型时对比同一模型在不同 harness 中的表现差异
- 定位回归来源是模型、harness 还是评分器
- 在 harness 改动后重跑同一任务切片验证效果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L25:  A Model × Harness co-evaluation benchmark for agentic AI.
> L37: It evaluates **the model and the harness together** while keeping enough metadata to read both dimensions independe

## 星数曲线

```mermaid
xychart-beta
    title "agentscope-ai/PawBench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 117 --> 122
    line [118, 121, 121]
```

2026-10-18 118 → 2026-10-26 121（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `aff55ac186b1` · [字段定义](../../DATASET.md)*
