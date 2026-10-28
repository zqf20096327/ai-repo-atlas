# agencyenterprise/GlossoGen

⭐ 27 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/agencyenterprise/GlossoGen) · [官网](https://agencyenterprise.github.io/GlossoGen/) · 组织维护

**运行多 LLM agent 团队受控实验的平台**

GlossoGen 是一个用于在 LLM agent 团队上开展受控实验的平台：场景将多个 agent 置于带角色、频道与工具的模拟任务中，按回合推进，记录每条消息、工具调用与模型响应，并按所选指标打分。内置场景研究压力下的通信：单个 agent 信息不足以独立完成任务，字符数受回合预算约束，agent 由此压缩、缩写并创造速记。提供事件溯源运行日志、swap/fork 干预与事后评估指标。安装需 Python 3.14，不在 PyPI 发布，需从 GitHub 指定 tag 经 uv/pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 agent 场景按回合推进，记录全部消息、工具调用与模型响应
- 事件溯源运行日志，支持 swap 与 fork 干预
- 事后评估指标，可自定义场景与指标包
- 内置通信压力场景（字符预算约束）

## 适用场景

- 研究 LLM agent 团队在资源受限下的通信与涌现速记
- 对多 agent 运行做受控干预实验与事后评估
- 复现或扩展模拟场景与指标

## 场景标签

`多智能体` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L8: A platform for running controlled experiments on teams of LLM agents. A scenario
> L11: response, and scores the run with the metrics you pick. The scenarios shipped

## 星数曲线

```mermaid
xychart-beta
    title "agencyenterprise/GlossoGen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `32bf26e34ce3` · [字段定义](../../DATASET.md)*
