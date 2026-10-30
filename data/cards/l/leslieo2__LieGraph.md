# leslieo2/LieGraph

⭐ 50 · Python · MIT · 推送 2025-11-08 · [GitHub](https://github.com/leslieo2/LieGraph) · 个人维护 · 中文 README

**LangGraph 多智能体「谁是卧底」游戏，AI 玩家推理投票找卧底**

基于 LangGraph StateGraph 实现的多人社交推理游戏「谁是卧底」：全部玩家为自主 AI agent，各自维护概率化信念系统（自我信念置信度、对他人怀疑矩阵），通过 LLM 推理发言、分析对话与投票模式推断身份，并进行虚张声势识别与结盟策略。游戏由 langgraph dev 后端与 npm 前端组成，通过 OpenAI 或 DeepSeek API 配置 LLM。内置指标收集器记录胜负平衡、身份推断准确率与发言多样性，输出 JSON 报告供 prompt 评估流程使用，并附 CLI 聚合分析工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI agent 玩家具备概率化信念系统（怀疑矩阵与自我身份推断）
- LangGraph StateGraph 编排完整游戏生命周期（发词、发言、投票、淘汰）
- 内置指标收集：胜负平衡、身份识别准确率、发言多样性，输出 JSON 报告
- 通过 .env 配置 OpenAI / DeepSeek 作为 LLM 后端

## 适用场景

- 观察多个 LLM agent 在社交推理博弈中的策略与发言行为
- 用游戏指标 JSON 报告评估和对比不同 prompt / 模型表现
- 作为 LangGraph 多智能体编排的实现参考进行学习与改造

## 场景标签

`多智能体` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L6: LieGraph is a multi-agent implementation of the popular social deduction game "Who Is spy," built with LangGraph. It
> L12: - **Autonomous AI Agents:** AI players with unique personalities and strategic thinking capabilities

## 星数曲线

```mermaid
xychart-beta
    title "leslieo2/LieGraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-30 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `61b535fd1a1e` · [字段定义](../../DATASET.md)*
