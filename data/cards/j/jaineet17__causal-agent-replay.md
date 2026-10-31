# jaineet17/causal-agent-replay

⭐ 14 · Python · 推送 2026-07-09 · [GitHub](https://github.com/jaineet17/causal-agent-replay) · 个人维护

**LLM agent 轨迹的反事实重放与因果归因调试库**

面向 LLM agent 开发与调试场景的 Python 库（CAR）：把录制的 agent 运行建模为结构因果模型，通过在某个步骤上做干预（do_resample/do_action/do_observation/do_policy 等）并向前重放 agent，测量结果分布的偏移，从而定位导致失败结局的因果步骤；归因用对比法与预算受限的蒙特卡洛 Shapley，效应带置信区间。提供 LangGraph/LangChain、OpenAI Agents SDK、CrewAI 三种框架适配器，后端走 Policy 协议，可用本地 Ollama 免 API key 运行。Phases 0–7 完成，v1 适配器范围限于单 agent、每轮一次工具调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- do(·) 干预代数（resample/action/observation/context/policy）+ 向前重放定位因果步骤
- 分布化结果估计与蒙特卡洛置信区间，含 Shapley 归因
- LangGraph/LangChain、OpenAI Agents SDK、CrewAI 适配器一行包装录制
- 通过 Policy 协议支持本地 Ollama 等任意 OpenAI 兼容后端，无需 API key

## 适用场景

- agent 出错时找出哪一步决策真正导致了坏结局
- 测试某步换成其他动作/其他模型后结局是否改变
- 无 API key 用本地模型录制并重放 agent 轨迹做归因分析

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L15: `causal-agent-replay` (CAR) answers it the only principled way: it **intervenes** on a step and
> L81: Record *your* agent and attribute its failures — same one-line wrap on any of the frameworks:
> L131: CAR runs against any backend behind the `Policy` protocol, so you can record and replay agents

## 星数曲线

```mermaid
xychart-beta
    title "jaineet17/causal-agent-replay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `8947dfad449a` · [字段定义](../../DATASET.md)*
