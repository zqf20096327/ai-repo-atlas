# microsoft/Trace

⭐ 762 · Python · MIT · 推送 2026-06-17 · [GitHub](https://github.com/microsoft/Trace) · [官网](https://microsoft.github.io/Trace/) · 组织维护

**用自然语言反馈端到端优化 AI Agent 的 Python 库**

Trace 是微软研究团队随 NeurIPS 2024 论文发布的 Python 库，提供类 AutoDiff 的生成式优化：以 node/bundle 原语构建可追踪的计算图，将数值奖励、自然语言反馈、编译器报错等通用反馈沿执行轨迹回传，用 LLM 优化提示词、代码或 Agent 参数。内置 OPRO、TextGrad、OptoPrime 三种优化器，可切换；LLM 调用经 LiteLLM 或 AutoGen 后端管理，需配置 OpenAI/Anthropic 等 API key。要求 Python≥3.9。

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

- node/bundle 原语自动追踪 Python 执行形成计算图
- 支持数值奖励、自然语言、报错等通用反馈的回传优化
- 内置 OPRO/TextGrad/OptoPrime 三种可切换优化器
- PyTorch 风格 API，pip 安装，LiteLLM/AutoGen 双后端

## 适用场景

- 对 LLM Agent 的提示词与代码做自动优化
- 构建能根据环境反馈自我改进的 Agent
- 联合优化 prompt 与代码以提升 BigBench-Hard 等任务表现

## 场景标签

`提示工程` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: Trace is a new AutoDiff-like tool for training AI systems end-to-end with general feedback (like numerical rewards 
> L15: propagating an AI system's execution trace. Trace is implemented as a PyTorch-like Python library. Users write Pyth
> L51: Trace has two primitives: `node` and `bundle`. `node` is a primitive to define a node in the computation graph. `bu

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Trace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 761 --> 763
    line [762, 762]
```

2026-10-18 762 → 2026-10-26 762（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a8ed421870ff` · [字段定义](../../DATASET.md)*
