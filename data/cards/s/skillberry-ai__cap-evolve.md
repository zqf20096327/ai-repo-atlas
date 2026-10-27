# skillberry-ai/cap-evolve

⭐ 66 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/skillberry-ai/cap-evolve) · [官网](https://skillberry-ai.github.io/cap-evolve/) · 组织维护

**AI agent 优化工具：基于评测轨迹迭代优化提示词、工具与技能**

面向已有 agent 与评测的开发者工具：运行『评测→诊断失败→提出修改→保留仅在 held-out 分割上显著提升的候选→提交』的循环，可联合优化系统提示词、工具代码、MCP 工具面与技能包（SKILL.md 等），只修改 agent 读取的内容而非权重。提供 CLI（init/doctor/diff/watch/dashboard）、无 API key 的确定性 toy_calc 示例，以及 Claude Code 插件和 Codex、Cursor 等多种宿主接入路径；自带 adapter 模板（tau2-bench、SWE-bench 等）。结果部分行被标注为 fit metric 而非 held-out，README 明示 caveats。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 循环：评测→诊断→候选修改→显著性门控（Δ > k·SE）→提交
- 可联合优化系统提示词、工具代码、MCP 工具面与技能包
- 每个候选是 git commit，dashboard 展示 diff、血缘与任务×迭代热图
- toy_calc 零 API key 确定性示例与多宿主接入路径

## 适用场景

- 我已有 agent 和评测，想自动优化它的提示词与工具
- 审计 agent 每次优化改动的内容与成本
- 把现有基准（tau2/SWE-bench 等）接入做 agent 能力迭代

## 场景标签

`提示工程` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L14: **cap-evolve improves an AI agent's prompts, tools, and skills by learning from failed
> L17: You bring the agent and the eval you already have. cap-evolve runs the loop — evaluate →
> L42: - **Keep evaluation honest.** Acceptance is a val-only significance gate (Δ > k·SE); the

## 星数曲线

```mermaid
xychart-beta
    title "skillberry-ai/cap-evolve 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 64 --> 67
    line [65, 66, 66]
```

2026-10-18 65 → 2026-10-27 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `36c30ce2fe98` · [字段定义](../../DATASET.md)*
