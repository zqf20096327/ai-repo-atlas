# qiqihezh/deepresearch-agent

⭐ 169 · Python · 推送 2026-05-11 · [GitHub](https://github.com/qiqihezh/deepresearch-agent) · 个人维护 · 中文 README

**面向复杂研究任务的深度研究 Agent 系统，自动产出带引用研究报告**

以 Python 3.11 编写的多智能体深度研究系统：Planner 将复杂问题拆解为 DAG 子任务，自研 asyncio 编排引擎调度执行，配合语义级上下文压缩（Embedding 三级过滤 + TextRank）、跨 Agent 共享记忆（SQLite + 向量索引、去重与矛盾消解）、Red-Blue 对抗循环抑制幻觉，最终合成结构化研究报告。支持 DeepSeek/MiMo/vLLM/OpenAI 后端热切换，配套 165 次独立运行的评测体系（规则指标、LLM-as-Judge、Bootstrap 统计检验）。提供单次研究、REPL 交互、批量实验三种运行方式，从 git clone 源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自研 asyncio + DAG 编排引擎（9 状态状态机、三级降级策略），不依赖 LangGraph/AutoGen
- Red-Blue 对抗循环：5 维度攻击 + 4 种修复操作，含收敛与震荡检测
- 语义三级上下文压缩与跨 Agent 共享记忆（去重/矛盾检测/LRU）
- 多后端 LLM 热切换与 165 次独立运行的评测体系

## 适用场景

- 对复杂问题自动生成带引用的结构化深度研究报告
- 研究 Agent 系统的编排、压缩、记忆模块设计参考
- 复现带统计显著性检验的 LLM Agent 评测流程

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L3: ### *从复杂 Query 到结构化深度研究报告，全链路自动化*
> L17: 本项目从零构建了一套**面向深度研究任务的 Agent 系统**，覆盖规划、执行、记忆、对抗、进化、评测全链路。
> L27: - 📝 **结构化输出** → 生成带引用、有逻辑、可验证的研究报告

## 星数曲线

```mermaid
xychart-beta
    title "qiqihezh/deepresearch-agent 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24"]
    y-axis "stars" 165 --> 170
    line [166, 167, 169, 169]
```

2026-10-18 166 → 2026-10-24 169（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c0ffaaa313a8` · [字段定义](../../DATASET.md)*
