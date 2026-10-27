# ant-research/meta-agent-challenge

⭐ 24 · Python · 推送 2026-06-04 · [GitHub](https://github.com/ant-research/meta-agent-challenge) · [官网](https://meta-agent-challenge.com) · 组织维护

**评测代码 agent 能否自主构建 agent 的基准（五域两阶段）**

Meta-Agent Challenge（MAC）是一个基准：让元代理（如 Claude Code、Codex、Gemini CLI）阅读任务、编辑 Python agent.py、在开发集上运行并迭代，最终在保密测试集上评分，全过程在双容器沙箱、时间与 API 预算内完成。覆盖 Meta-AIME、Meta-GPQA、Meta-LiveCodeBench、Meta-SWE-Bench、Meta-Terminal-Bench 五个域，每个域提供三个脚手架运行脚本；基于 Harbor 运行，支持贡献新域、新脚手架与新模型上榜。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个域两阶段设计：AIME/GPQA/LiveCodeBench/SWE-Bench/Terminal-Bench
- 双容器沙箱内限时、限 API 预算的自主 agent 构建
- 三种脚手架运行脚本（Claude Code / Codex / Gemini CLI）
- 提供审计脚本与贡献新域/脚手架/模型的机制

## 适用场景

- 评测代码 agent 自主开发 agent 的能力
- 在排行榜上比较不同模型的元代理表现
- 扩展新的评测域或脚手架并复现实验

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: The first benchmark that asks code agents to build agents — then measures how good those agents are. See the leaderb
> L12: The Meta-Agent Challenge (MAC) flips the usual benchmark setup. Instead of asking an AI to solve a task, MAC asks i

## 星数曲线

```mermaid
xychart-beta
    title "ant-research/meta-agent-challenge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `4732c179f0c7` · [字段定义](../../DATASET.md)*
