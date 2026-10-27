# The-Swarm-Corporation/AI-CoScientist

⭐ 132 · Python · MIT · 推送 2026-07-13 · [GitHub](https://github.com/The-Swarm-Corporation/AI-CoScientist) · [官网](https://swarms.ai) · 组织维护

**多智能体科研框架：生成并演化科学假说**

基于 Google 论文 "Towards an AI Co-Scientist" 的多智能体实现，用 Swarms 框架构建，面向科研场景。包含 8 个专门化 Agent（生成、反思评审、排名、演化、元评审、邻近性分析、锦标赛、监督），通过 Elo 锦标赛制的两两比较对假说排名，并以元评审引导的迭代精炼与多样性控制持续改进假说。支持状态保存与恢复。以 Python 包提供，可从 PyPI 或源码安装，需 LLM API key（OpenAI/Anthropic/Google）。

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

- 8 个专门化 Agent 覆盖假说生成、评审、排名与演化流程
- Elo 锦标赛制两两比较进行假说排序
- 元评审引导的迭代精炼与邻近性多样性控制
- 支持保存与恢复研究工作流状态

## 适用场景

- 围绕研究目标生成并迭代改进科学假说
- 对假说进行同行评审式评分与锦标赛排名
- 保存并恢复跨轮次的研究工作流状态

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L7: A multi-agent AI framework for collaborative scientific research, implementing the "Towards an AI Co-Scientist" meth
> L33: 1. **Generation Phase**: Create initial hypotheses based on research goal

## 星数曲线

```mermaid
xychart-beta
    title "The-Swarm-Corporation/AI-CoScientist 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 131 --> 133
    line [132, 132]
```

2026-10-18 132 → 2026-10-27 132（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `aa49419965c2` · [字段定义](../../DATASET.md)*
