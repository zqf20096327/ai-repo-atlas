# zpqiu/rl-infra-notes

⭐ 15 · HTML · 推送 2026-09-08 · [GitHub](https://github.com/zpqiu/rl-infra-notes) · 个人维护 · 中文 README

**LLM 强化学习训练基础设施的源码级分析笔记集合**

结构化记录对 LLM RL 训练框架源码的阅读过程，主题覆盖异步 RL 调度、权重同步、FP8 混合精度、MoE 路由精度等。对比分析 slime、veRL、NeMo-RL 三个框架的异步 RL 设计，并分析 Megatron-LM、TransformerEngine、vLLM 中的 FP8 与 MoE 细节，附代码位置、对比表和架构图。中英双语，英文版位于 docs-en/ 目录，MIT 许可。面向需要理解框架内部实现的研究者与工程师。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对比 slime/veRL/NeMo-RL 三框架的异步 RL 设计（rollout buffer、权重同步、staleness）
- FP8 量化范围、scale 格式与通信精度的源码级分析
- MoE Router dtype 追踪与 bf16 topk 精度风险分析
- 中英双语笔记，docs-en/ 与 docs/ 结构平行

## 适用场景

- 深入理解异步 RL 训练中 rollout 与 training 的调度机制
- 排查 FP8 训练或 MoE 路由的精度问题
- 选型前比较各 RL 框架的设计取舍

## 场景标签

`强化学习` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: > Deep source-code walkthroughs of LLM RL training infrastructure — async RL scheduling, weight synchronization, FP8
> L7: LLM 强化学习训练基础设施的**源码级**深度分析笔记。不止于"是什么"，更关注"为什么这样设计"和"代码里实际怎么做的"。
> L18: 答案只在源码里。这个 repo 就是把"读源码"的过程结构化记录下来，附带代码位置、对比表和架构图。

## 星数曲线

```mermaid
xychart-beta
    title "zpqiu/rl-infra-notes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fae06fa8d4d7` · [字段定义](../../DATASET.md)*
