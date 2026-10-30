# DaizeDong/self-evolve

⭐ 26 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/DaizeDong/self-evolve) · 个人维护 · 中文 README

**面向开发者的技能/仓库迭代改进与确定性评测工具**

self-evolve 是一个 Claude Code Skill，用于通过提议修改、在 Git worktree 中评测、并以证据决定接受与否的方式迭代改进技能或代码仓库。核心机制：冻结评测契约（策略/义务/holdout）、profile→reflect→propose→patch→evaluate→accept 或 review 循环、确定性门控处理证据与接受判定、真实证据存于 PRIVATE Git companion、可审计与回滚。安装方式为 git clone 后 pip 安装 companion resolver，通过 Python CLI（doctor/init/run/status）运行，轮次受 --max-rounds 与熔断机制限制。README 明确列出多项当前限制（如 C 类无回归测量生产者、无 OS 级沙箱）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 冻结评测契约的 A/B 改进循环（profile→reflect→propose→patch→evaluate）
- 确定性门控负责证据核验与接受判定，模型仅提议
- 失败/拒绝/评审均可审计，保留测量总体与候选字节以支持回滚
- 真实证据存放于 PRIVATE Git companion，发布/合并需调用方另行授权

## 适用场景

- 对代码仓库或 agent 技能做可审计的迭代改进
- 防止自我改进循环通过改任务或自评分刷分
- 在隔离 worktree 中评测候选补丁并保留回滚能力

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Improve a skill or repository through proposed changes, evaluation in a Git worktree, and evidence-based acceptance.
> L19: - **Evidence sources.** The loop is

## 星数曲线

```mermaid
xychart-beta
    title "DaizeDong/self-evolve 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `23a3ff6fb36e` · [字段定义](../../DATASET.md)*
