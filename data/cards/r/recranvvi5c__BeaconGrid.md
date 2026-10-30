# recranvvi5c/BeaconGrid

⭐ 23 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/recranvvi5c/BeaconGrid) · 个人维护

**Agent 决策回放工作台：重放历史会话并对比修订后策略的差异**

无第三方依赖的回放工具：先记录一次 agent 会话（上下文帧、当时的策略、候选动作与最终选择），再用修订后的策略对每个决策重新确定性打分，输出可分享的 replay dossier——逐决策的原始 vs 回放选择、分歧分类（tool_switch/veto_shift/reweight/all_vetoed）、规则覆盖统计。提供 Python 3.11 包与结果字节兼容的 Go 模块，各含 CLI 与 5 个命令。限制：不运行 agent、不调用工具或模型，仅回放已记录的决策。

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

- 确定性打分：相同输入产生相同分数、选择与追踪记录
- 四种路线分歧分类并附人类可读原因
- 策略覆盖报告（fired/veto/dormant 规则与命中计数）
- Python 与 Go 双运行时字节兼容，仅用各自标准库

## 适用场景

- 上线新策略前用历史会话回归测试，发现被静默改道的决策
- 将回放 dossier 附到工单或合规审查作为决策审计记录
- 找出从未触发的休眠规则并清理

## 场景标签

`LLM 可观测性` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: BeaconGrid is a dependency-free studio for **replaying recorded agent sessions against revised policies**. It answe
> L35: BeaconGrid does **not** run your agent, call your tools, or talk to any model. It replays *recorded* decisions thro

## 星数曲线

```mermaid
xychart-beta
    title "recranvvi5c/BeaconGrid 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-10-26", "2026-10-30"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-23 22 → 2026-10-30 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ce1a46a1d711` · [字段定义](../../DATASET.md)*
