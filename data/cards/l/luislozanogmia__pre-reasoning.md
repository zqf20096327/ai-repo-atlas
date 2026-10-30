# luislozanogmia/pre-reasoning

⭐ 19 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/luislozanogmia/pre-reasoning) · [官网](https://mia-labs.com) · 个人维护

**给 LLM/agent 提供 1M 参数前置推理引擎，先结构化问题再作答**

面向 LLM 与 AI agent 的 Python 包：捆绑一个 1M 参数（safetensors）推理引擎。调用流程为 AI 先用表单模板把用户上下文写成结构化形式，引擎分析该形式并返回外部结构化追踪（依赖方向、根阻塞项、解锁顺序、冲突、条件绑定等五类能力族），AI 再带着追踪重新读取原问题后作答。表单少于五个有效块会返回 REPROMPT_REQUIRED 告警。另有 Focus Mode 十分钟定时反思循环与仅验证文本覆盖的 coverage_check。训练代码不在发布内；尚未发布到 PyPI，从本目录安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1M 参数引擎（V3 的 13.74M 缩减 92.6%），safetensors 权重内嵌
- 五类能力族：依赖/冲突/数值需求/条件绑定/传递组合
- Focus Mode 调度器驱动的十分钟反思循环
- 附 SKILL.md agent 协议与 Claude Code 可选 hooks

## 适用场景

- 让 agent 在回答前先获得问题的结构化地图（根阻塞、解锁顺序）
- 长时任务中周期性重读原问题并更新状态
- 为 Claude Code 强制执行 form-first 流程

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: Pre-Reasoning gives an AI a structural checkpoint between forward passes. The AI first interprets the user's context
> L26:   -> 1M pre-reasoning model analyzes the form
> L83: - `pre_reasoning/checkpoints/pre-reasoning-1m.safetensors` — weights-only checkpoint

## 星数曲线

```mermaid
xychart-beta
    title "luislozanogmia/pre-reasoning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `d0a75c33a25d` · [字段定义](../../DATASET.md)*
