# metareflection/formal-disco

⭐ 14 · Python · 推送 2026-07-08 · [GitHub](https://github.com/metareflection/formal-disco) · [官网](https://arxiv.org/abs/2607.04631) · 组织维护

**分布式 LLM 工作流框架：大规模生成并自改进形式化验证程序**

面向科研的分布式系统：LLM 驱动的 Initiator/Fixer/Extender 三类 worker 通过共享 agenda（任务队列+对象数据库）协作，对 Dafny、Verus(Rust)、Frama-C 三种验证语言生成、修复并扩展形式化验证程序，以验证器结果作为质量信号。每次 LLM 调用记录为蒸馏样本，通过熵最大化 SFT 微调开源模型实现自改进循环。支持本地单机与集群分布式模式，LLM 提供方经 LangChain 配置可切换。附带论文，生成数据集发布于 HuggingFace。运行需在 PATH 安装对应验证器。

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

- 三类 LLM worker 经共享 agenda 协作生成/修复/扩展验证程序
- 覆盖 Dafny、Verus、Frama-C 三种验证语言后端
- 熵最大化样本选择的自改进 SFT 蒸馏循环
- agenda 服务器协调多节点 worker 的分布式运行模式

## 适用场景

- 生成三种验证语言的大规模合成训练数据集
- 复现论文中的自改进发现实验与图表
- 从 checkpoint 蒸馏微调开源代码模型

## 场景标签

`Agent 框架` `多智能体` `科研工具` `微调` · 领域:Agent 开发

## 证据(README 行号)

> L7: Formal Disco is a distributed system where LLM-based workers collaborate through a shared *agenda* (a task queue + o
> L13: One *run* of the system starts an agenda and schedules three classes of workers (Section 3.2 of the paper), each ba

## 星数曲线

```mermaid
xychart-beta
    title "metareflection/formal-disco 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `230ad266372f` · [字段定义](../../DATASET.md)*
